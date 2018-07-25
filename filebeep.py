import os

def abrearq(arq):	
	f = open("/home/pi/hom/{0}.txt".format(arq), "r")
	raw = f.readlines()
	f.close()
	return raw


def processaPrograma(raw):
	programa = list()
	for line in raw:
	    if line[0] != "#" and len(line) > 1:
	        nota, dur = line.split(',')
	        programa.append((nota, dur))
	return programa


def filebeep():
	arq = 'testador'
	raw = abrearq(arq)	
	programa = processaPrograma(raw)
	for item in programa:
	    duration = float(item[1])
	    freq = float(item[0])
	    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
