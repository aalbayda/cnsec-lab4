#
#	CNSEC Exer 4, Task 7
#

from Crypto.Cipher import AES
from Crypto.Util import Padding

# Get user input
plaintext = bytes(input("Enter plaintext: "), "utf-8")
ciphertext = input("Enter ciphertext: ")
iv = bytes.fromhex(input("Enter IV: "))
dictionary = input("Enter dictionary filename: ")

# Open dictionary
f_dictionary = open(dictionary, "r")


# Use each word in dictionary to guess key
for word in f_dictionary:

	# Remove newline
	word = word.rstrip()

	# Key must be exactly 16 bytes, pad if not
	key = word
	n_paddings = 16-len(key) 
	if len(key) < 16:			
		key += "#" * n_paddings
	else:
		continue
	key = bytes(key, 'utf-8')

	# Encrypt plaintext with PyCrypto, 16-byte blocks
	cipher = AES.new(key, AES.MODE_CBC, iv)
	guessed_ciphertext = cipher.encrypt(Padding.pad(plaintext, 16)).hex()

	# Found the key
	if guessed_ciphertext == ciphertext:
		print("The key is", word)
		f_dictionary.close()
		break

f_dictionary.close()