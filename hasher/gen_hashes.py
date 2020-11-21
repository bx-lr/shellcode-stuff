import sys
import os
import argparse
import time
import json
import pefile

from Queue import Queue
from threading import Thread
from collections import OrderedDict


class Worker(Thread):
	""" Thread executing tasks from a given tasks queue """
	def __init__(self, tasks):
		Thread.__init__(self)
		self.tasks = tasks
		self.daemon = True
		self.start()

	def run(self):
		while True:
			func, args, kargs = self.tasks.get()
			try:
				func(*args, **kargs)
			except Exception as e:
				# An exception happened in this thread
				print(e)
			finally:
				# Mark this task as done, whether an exception happened or not
				self.tasks.task_done()


class ThreadPool:
	""" Pool of threads consuming tasks from a queue """
	def __init__(self, num_threads):
		self.tasks = Queue(num_threads)
		self.qresult = None
		self.nwork = None
		for _ in range(num_threads):
			Worker(self.tasks)

	def add_task(self, func, *args, **kargs):
		""" Add a task to the queue """
		self.tasks.put((func, args, kargs))

	def map(self, func, args_list):
		""" Add a list of tasks to the queue """
		for args in args_list:
			self.add_task(func, args)

	def wait_completion(self):
		""" Wait for completion of all the tasks in the queue """
		file = sys.stdout
		size = 60
		prefix = ''
		count = self.nwork
		def show(j):
			x = int(size*j/count)
			file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
			file.flush()        
		show(0)
		while ( self.nwork > self.qresult.qsize()):
			show(self.qresult.qsize()+1)
		file.write("\n")
		file.flush()
		self.tasks.join()


def load_hash_funcs():
	cwd =  os.getcwd()
	cwd += os.sep
	cwd += 'hash_funcs' + os.sep
	path = list(sys.path)
	sys.path.insert(0, cwd)
	dirlist = os.listdir(cwd)
	mods = []
	for fn in dirlist:
		if fn.endswith('.py'):
			print 'Importing hash function: ', fn
			#todo try catch here
			try:
				mods.append(__import__(fn.split('.')[0]))
			except Exception as e:
				print 'error loading: ', fn
				pass
	sys.path = path
	return mods


def do_hash(fn, hash_funcs):
	hashes=[]
	#load pe
	#todo try catch here
	peFile = pefile.PE(fn)
	#get exports if there
	if ((not hasattr(peFile, "DIRECTORY_ENTRY_EXPORT")) or (peFile.DIRECTORY_ENTRY_EXPORT is None)):
		#print 'Skipping file ', fn
		return

	#get our syms
	for sym in peFile.DIRECTORY_ENTRY_EXPORT.symbols:
		if sym.name is not None:
			#run each hash func on the symbol
			for i in xrange(0, len(hash_funcs)):
				try:
					h = hash_funcs[i].run(sym.name, fn.split(os.path.sep)[-1])
				except Exception as e:
					print 'exception in: ', hash_funcs[i]
					print e
				hash_val = [h,i,fn.split(os.path.sep)[-1],sym.name]
				hashes.append(hash_val)
	return hashes


def test_hash(qwork):
	while not qwork.empty():
		work = qwork.get()
		fn = work[0]
		qresult = work[1]
		hash_funcs = work[2]

		result = do_hash(fn, hash_funcs)
		qresult.put(result)
		qwork.task_done()
	return 



def main(all_files, out_file):
	if len(all_files) < 1:
		print 'Nothing to do'
		return 
	print 'Loading hash functions...'
	hash_funcs = load_hash_funcs()
	hash_types_dict = {}
	for i in xrange(0, len(hash_funcs)):
		#maybe make this {i:[hash_funcs[i].get_name(), hash_funcs[i].get_pseudocode()]}
		hash_types_dict.update({i:hash_funcs[i].get_name()})
	print 'Done\n'

	source_libs_dict = {}
	for i in xrange(0, len(all_files)):
		source_libs_dict.update({i:all_files[i].split(os.path.sep)[-1]})
	
	qwork = Queue(maxsize=0)
	qresult = Queue(maxsize=0)
	nthreads = min(50, len(all_files))
	for fn in all_files:
		qwork.put([fn, qresult, hash_funcs])

	pool = ThreadPool(nthreads)
	pool.map(test_hash, (qwork,))
	pool.nwork = len(all_files)
	pool.qresult = qresult
	print 'Generating hashes...'
	pool.wait_completion()
	print 'Done\n'

	print 'Building output...'
	symbol_hashes_dict = {}
	while not pool.qresult.empty():
		hashes = pool.qresult.get()
		try:
			for hash_val in hashes:
				symbol_hashes_dict.update({hash_val[0]:{"hash_type":hash_val[1], "lib_key":hash_val[2], "symbol_name":hash_val[3]}})
		except:
			pass

	#make our absolutely massive json...
	all_hashed = {
	'hash_types':hash_types_dict,
	'source_libs':source_libs_dict,
	'symbol_hashes':symbol_hashes_dict
	}

	#poop it out
	with open(out_file, 'w') as f:
		json.dump(all_hashed, f)
	return 

if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument('-d', '--dir', required=True, help='Path to file or directory')
	ap.add_argument('-o', '--out', required=True, help='Output file to write')

	args = vars(ap.parse_args())
	file_or_path = args['dir']
	all_files = []
	print 'Generating file list...'
	if os.path.isdir(file_or_path):
		for root, dirs, files in os.walk(file_or_path, topdown=False):
			for name in files:
				#todo fix this lazyness
				if name.endswith('.dll'):
					all_files.append(os.path.join(root, name))
	else:
		all_files.append(file_or_path)

	print 'Done\n'
	main(all_files, args['out'])
	print 'All done'