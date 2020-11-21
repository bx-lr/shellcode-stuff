import ctypes
import argparse
import os

def main(fpath):
	fd = open(fpath, 'rb')
	data = fd.read()
	fd.close()

	ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(data)), ctypes.c_int(0x3000), ctypes.c_int(0x40))
	buf = (ctypes.c_char * len(data)).from_buffer_copy(data)

	ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr), buf, ctypes.c_int(len(data)))

	raw_input('waiting for you in: %d at: %s' %( os.getpid(),hex(ptr)))

	hthread = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0), ctypes.c_int(0), ctypes.c_int(ptr), ctypes.c_int(0), ctypes.c_int(0), ctypes.pointer(ctypes.c_int(0)))

	ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(hthread), ctypes.c_int(-1))

if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument('-b', '--bin', required=True, help='Path to bin to execute')
	args = vars(ap.parse_args())

	main(args['bin'])