from __future__ import division
from itertools import imap
import operator
import os
import oneCharCipher
import string

def hamDistance(str1, str2):
	str1 =  ''.join(format(ord(i),'b').zfill(8) for i in str1)
	str2 =  ''.join(format(ord(i),'b').zfill(8) for i in str2)
	ne = operator.ne
	return sum(imap(ne, str1, str2))

with open('data/6.txt', 'r') as f:
        ct = f.read().replace('\n','')


def getKeyLength(ct):
        minHam = 3000
        keylen = 0
        for kLen in range(1,9):
                block1 = ct[0:kLen]
                block2 = ct[kLen:kLen*2]
                tmp = hamDistance(block1, block2)/kLen
                if tmp < minHam:
                        minHam = tmp
                        keylen = kLen
        return keylen

def score(text):
	score = 0
        #for char in string.printable:
        #        score += text.count(char)
        for char in text:
                if char not in string.printable:
                        score -= 10
	return score

def decipher(ct, keys):
	spaceMax = -40000
        split = ''.join(ct).encode('hex')
        message = ""
        for key in keys:
                m = oneCharCipher.hexStrXOR(key, split).decode('hex')
                check = score(m)
                if(check > spaceMax):
                        correctKey = key
                        spaceMax = check
                        message = m
        return message

ct = ct.decode('base64')[:20]
keyLength = getKeyLength(ct)
keysizeBlocks = [ct[i:i + keyLength] for i in range(0, len(ct), keyLength)]
transpose = map(None, *keysizeBlocks)
keys = oneCharCipher.createKeys(len(transpose[0]) * 2)


transN = []
for i in transpose:
        t = [x for x in i  if x is not None]
        transN.append(''.join(t))

finals = []
for N in transN:
        finals.append(decipher(N, keys))

print "FOR LOOP:\n"
for i in range(len(finals[0])):
        for x in finals:
                print x[i],
