import string
import sys
import 2FixedXOR

hexStrXOR = 2FixedXOR.hexStrXOR

def createKey(a, length):
	if len(a) == 1:
		a = a*2
	return a * (length/2)

def freq(char, inStr):
	if len(char) == 1:
		char = char.encode('hex')
	count = 0
	for i in range(0, len(inStr), 2):
		if inStr[i:i+2]==char:
			count += 1.0
	return count/(len(inStr)/2)



def createKeys():
	keys = []
	for i in range(128):
		k = createKey(format(i, 'x'), len(ct))
		keys.append(k)
	return keys

def decipher(ct, keys):
	spaceMax = 0
	message = ""
	correctKey = ""
	for key in keys:
		m = hexStrXOR(key, ct)
		check = freq("20", m)
		if(check > spaceMax):
			correctKey = key
			spaceMax = check
			message = m

	return message.decode('hex')


