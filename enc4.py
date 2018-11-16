import hashlib
import string

def encrypt(hash_str):
	hash_gen = hashlib.sha256(hash_str).digest().encode("base64")
	return hash_gen

alphabet = string.letters[0:52] + string.digits
rightHash = "AKCkKOEHZuUPfCLbS0ye8WFnXoDEgw9RFYXlw293vbY="

for a in alphabet[48:62]:#first position of the pass
	for b in alphabet:	#second position
		for c in alphabet:	#third position
			for d in alphabet:	#...
				for e in alphabet:
					for f in alphabet:
						for g in alphabet:
							passw = a+b+c+d+e+f+g
							sha = encrypt(passw)
							if sha == rightHash:
								print("Pass: " + passw + " Hash: " + sha)
								exit() 
							else: 
								print("NOT " + passw + " sha " + sha)

							for h in alphabet:
								passw = a+b+c+d+e+f+g+h
								sha = encrypt(passw)
								if sha == rightHash:
									print("Pass: " + passw + " Hash: " + sha)
									exit() 
								else: 
									print("NOT " + passw + " sha " + sha)