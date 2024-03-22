#!/usr/bin/env python

import struct

infile_path = "/dev/input/js0"
EVENT_SIZE = struct.calcsize("llHHI")
try:
	file = open(infile_path, "rb")	
except IOError as inst:
	if "No such file or directory" in str(inst):
		print("Aucune manette détectée")
	else:
		print("Erreur : ", inst)
else:
	event = file.read(EVENT_SIZE)
	while event:
		print(event)
		print(struct.unpack("llHHI", event))
		(tv_sec, tv_usec, type, code, value) = struct.unpack("llHHI", event)
		event = file.read(EVENT_SIZE)
