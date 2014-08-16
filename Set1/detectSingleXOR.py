import string
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

def score(text):
	score = 0
	score += text.count(" ")
	score += text.count("a")
	score += text.count("e")

	return score

if __name__ == "__main__":
        keys = []

        lines = [line.strip() for line in open('data/4.txt')]

        for i in range(128):
                k = createKey(format(i, 'x'), 60)
                keys.append(k)


        spaceMax = 0
        message = ""
        correctKey = ""
        for line in lines:
                for key in keys:
                        m = hexStrXOR(key, line).decode('hex')
                        check = score(m)
                        if(check > spaceMax):
                                correctKey = key
                                spaceMax = check
                                message = m

        print message
