def hexStrXOR(a, b):
	a = a.decode("hex")
	b = b.decode("hex")
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b)).encode('hex')

if __name__ == "__main__":
        a = "1c0111001f010100061a024b53535009181c"
        b = "686974207468652062756c6c277320657965"
        c = "746865206b696420646f6e277420706c6179"
        
        print hexStrXOR(a,b) == c
