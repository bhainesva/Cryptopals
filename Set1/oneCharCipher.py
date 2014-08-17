import string
import sys
import fixedXOR

hexStrXOR = fixedXOR.hexStrXOR

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

def createKeys(length):
	keys = []
	for i in range(128):
		k = createKey(format(i, 'x'), length)
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

if __name__ == "__main__":
        ct = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        keys = createKeys(len(ct))
        print decipher(ct, keys)
