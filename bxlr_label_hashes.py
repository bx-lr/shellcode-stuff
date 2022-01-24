import json
import sys
import ghidra.app.script.GhidraScript
from ghidra.program.model.symbol import SourceType

def main():
	try:
		sc_hashes_file = askFile("Load json file", "Select json").getPath()
	except Exception as e:
		print str(e)
		exit()
	print('loading file: %s' % sc_hashes_file)
	with open(sc_hashes_file, 'r') as f:
		sc_hashes = json.load(f)

	try:
		choice = askChoice('Use Custom Address Range', 'Select Address Range', ['Main executable', 'RAM segment'], 'Main Executable')
	except Exception as e:
		sys.exit(0)
	base = None
	if choice == 'RAM segment':
		try:
			base = askAddress('Segment Base', 'Enter segment base to process')
			ranges = currentProgram.getMemory().getAddressRanges()
		except:
			sys.exit(0)
	else:
		print('Using Main Program Base...')
		ranges = currentProgram.getMemory().getAddressRanges()

	for r in ranges:
		if base:
			if r.getMinAddress() != base:
				continue
		begin = r.getMinAddress()
		length = r.getLength()
		ins = getInstructionAt(begin)
		print('Looking for function hashes at ', begin)
		print('size: ', length)
		while(ins==None):
			ins = getInstructionAfter(ins)
		for i in range(length):

			if ins.minAddress > r.maxAddress:
				break
			hash_func = ins.getDefaultOperandRepresentation(1)
			#print ins.getMinAddress(), hash_func

			if (hash_func):
				try:

					scalar_int = int(str(hash_func), 16)
					#lazy check
					if scalar_int > 0xffff:
						#print scalar_int	
						k = sc_hashes['symbol_hashes'][str(scalar_int)]
						#print k
						symbol_name = k['symbol_name']
						#print symbol_name
						symbol_lib = k['lib_key']
						#print symbol_lib
						hash_type = sc_hashes['hash_types'][str(k['hash_type'])]
						#print hash_type

						equate = '%s_%s_%s' % (symbol_lib, symbol_name, hash_type)
						print('Found hash at addr: ', ins.address, 'hash_func: ', hash_func, 'equate: ', equate)
						#print '\t', equate
						#todo fix this shit ... make bookmarks too
						equate_list = getEquates(ins, 1)
						tmp_list = [e.toString() for e in equate_list]
						if equate not in tmp_list:
							createEquate(ins, 1, equate)
						#createLabel(ins.address, equate, True, SourceType.ANALYSIS)

				except Exception as e:
					#print(e)
					pass

			ins =  getInstructionAfter(ins)
			while(ins==None):
				ins =  getInstructionAfter(ins)

'''
	min_addr = currentProgram.minAddress
	max_addr = currentProgram.maxAddress
	while (int(min_addr.toString(), 16)  <= int(max_addr.toString(), 16) ):
		inst = getInstructionAt(min_addr)
		if (inst):
			hash_func = inst.getDefaultOperandRepresentation(1)
			if (hash_func):
				print hash_func
				try:
					num = int(hash_func, 16)
					print 'hash_func: ', hash_func, num, inst.address

					# createEquate(inst, 1, 'ws2_32.recv.1')
					# createLabel(inst.address, 'ws2_32.recv.1', True, SourceType.ANALYSIS)
					#
				except Exception as e:
					print e
					print inst.address
					min_addr = getInstructionAfter(min_addr).address
		min_addr = getInstructionAfter(min_addr).address
	
'''
if __name__ == '__main__':
	main()