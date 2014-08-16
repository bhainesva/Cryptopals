def hexTo64(hexStr):
	return hexStr.decode('hex').encode('base64')

if __name__ == "__main__":
        hexStr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        print hexTo64(hexStr)
