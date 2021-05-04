# Final Project
# CMPEN 462
# James Zukowski, Chris Erhard, Anoop Soodini, Arib Hyder

import os 
import math
import csv
import binascii
from cryptography.fernet import Fernet
import base64


def encrypt(file, name):
	base = os.path.splitext(name)[0]
	string = ""
	BPSK = []
	QPSK = []
	QAM = []

	# Iterate through text file and read in file contents into variable "string"
	while True:
		line = file.readline()
		if not line:
			break
		else:
			string += line
	
	# Convert input into its 8-bit ascii format, store in binaryString
	binaryString = ''.join(format(ord(i), '08b') for i in string)
	
	# Writing binary data after converion from ASCII to binary to txt file
	encoded = open(base+"_toBinary.txt", "w")
	encoded.write(binaryString)

	# Encryption
	# key generation
	key = Fernet.generate_key()
	
	# string the key in a file
	with open('filekey.key', 'wb') as filekey:
		filekey.write(key)

	# opening the key
	with open('filekey.key', 'rb') as filekey:
		key = filekey.read()

	# using the generated key
	fernet = Fernet(key)
	
	# encrypting the binary data
	encrypted = fernet.encrypt(binaryString.encode("utf-8"))
	
	# decode encrypted encoded binary data and convert to binary string
	encrypted = ''.join(format(ord(i), '08b') for i in encrypted.decode('utf-8'))
	
	# write encyrpted binary data to file
	with open(base+'_encryptedBinary_in.txt', 'w') as encrypted_file:
		encrypted_file.write(encrypted)
		
	# Modulate encrypted data
	while True:
		print("What modulation scheme would you like to use to encrypt your file?")
		modulationChoice = int(input("Enter (1) for BPSK, (2) for QPSK, or (3) for 16QAM:\n"))

		if((modulationChoice != 1) and (modulationChoice != 2) and (modulationChoice != 3)):
			print("Invalid Input")
		
		else:
			break

	# BPSK Modulation
	if (modulationChoice == 1):
		for i in encrypted:
			if(i == '0'):
				BPSK.append(complex((1/math.sqrt(2)), (1/math.sqrt(2))))
			elif(i == '1'):
				BPSK.append(complex((-1/math.sqrt(2)), (-1/math.sqrt(2))))
		
		f = open(base+"_BPSK.csv", "w+")

		for i in BPSK:
			f.write(str(complex(i))+",")

		# add modulation scheme and key for decryption
		f.write('\n' + "BPSK" + '\n' + key.decode('utf-8'))
		f.close()

		print("Successfully Encrypted file! Encrypted binary data is stored in " + base +"_encryptedBinary_in.txt.")
		print("OFDM Symbols, modulation type, and encryption key are stored in " + base + "_BPSK.csv\n")


	# QPSK Modulation
	if (modulationChoice == 2):
		for i in range(0, len(encrypted), 2):
			if(encrypted[i:i+2] == '00'):
				QPSK.append(complex((1/math.sqrt(2)), (1/math.sqrt(2))))
			elif(encrypted[i:i+2] == '01'):
				QPSK.append(complex((1/math.sqrt(2)), (-1/math.sqrt(2))))
			elif(encrypted[i:i+2] == '10'):
				QPSK.append(complex((-1/math.sqrt(2)), (1/math.sqrt(2))))
			elif(encrypted[i:i+2] == '11'):
				QPSK.append(complex((-1/math.sqrt(2)), (-1/math.sqrt(2))))

		f = open(base+"_QPSK.csv", "w+")

		for i in QPSK:
			f.write(str(complex(i))+",")
		
		# add modulation scheme and key for decryption
		f.write('\n' + "QPSK" + '\n' + key.decode('utf-8'))
		f.close()

		print("Successfully Encrypted file! Encrypted binary data is stored in " + base +"_encryptedBinary_in.txt.")
		print("OFDM Symbols, modulation type, and encryption key are stored in " + base + "_QPSK.csv\n")

	# 16 QAM
	if (modulationChoice == 3):
		for i in range(0, len(encrypted), 4):
			if (encrypted[i:i+4] == '0000'):
				QAM.append(complex((1/math.sqrt(10)), (1/math.sqrt(10))))
			if (encrypted[i:i+4] == '0001'):
				QAM.append(complex((1/math.sqrt(10)), (3/math.sqrt(10))))
			if (encrypted[i:i+4] == '0010'):
				QAM.append(complex((3/math.sqrt(10)), (1/math.sqrt(10))))
			if (encrypted[i:i+4] == '0011'):
				QAM.append(complex((3/math.sqrt(10)), (3/math.sqrt(10))))
			if (encrypted[i:i+4] == '0100'):
				QAM.append(complex((1/math.sqrt(10)), (-1/math.sqrt(10))))
			if (encrypted[i:i+4] == '0101'):
				QAM.append(complex((1/math.sqrt(10)), (-3/math.sqrt(10))))
			if (encrypted[i:i+4] == '0110'):
				QAM.append(complex((3/math.sqrt(10)), (-1/math.sqrt(10))))
			if (encrypted[i:i+4] == '0111'):
				QAM.append(complex((3/math.sqrt(10)), (-3/math.sqrt(10))))
			if (encrypted[i:i+4] == '1000'):
				QAM.append(complex((-1/math.sqrt(10)), (1/math.sqrt(10))))
			if (encrypted[i:i+4] == '1001'):
				QAM.append(complex((-1/math.sqrt(10)), (3/math.sqrt(10))))
			if (encrypted[i:i+4] == '1010'):
				QAM.append(complex((-3/math.sqrt(10)), (1/math.sqrt(10))))
			if (encrypted[i:i+4] == '1011'):
				QAM.append(complex((-3/math.sqrt(10)), (3/math.sqrt(10))))
			if (encrypted[i:i+4] == '1100'):
				QAM.append(complex((-1/math.sqrt(10)), (-1/math.sqrt(10))))
			if (encrypted[i:i+4] == '1101'):
				QAM.append(complex((-1/math.sqrt(10)), (-3/math.sqrt(10))))
			if (encrypted[i:i+4] == '1110'):
				QAM.append(complex((-3/math.sqrt(10)), (-1/math.sqrt(10))))
			if (encrypted[i:i+4] == '1111'):
				QAM.append(complex((-3/math.sqrt(10)), (-3/math.sqrt(10))))

		f = open(base+"_16QAM.csv", "w+")

		for i in QAM:
			f.write(str(complex(i))+",")
		
		# add modulation scheme and key for decryption
		f.write('\n' + "QAM" + '\n' + key.decode('utf-8'))
		f.close()

		print("Successfully Encrypted file! Encrypted binary data is stored in " + base +"_encryptedBinary_in.txt.")
		print("OFDM Symbols, modulation type, and encryption key are stored in " + base + "_16QAM.csv\n")

	

def decrypt(name, symbols, modulation, key):
	base = os.path.splitext(name)[0]
	# get just string of modulation scheme and get decryption key
	modulation = modulation.strip("[']")
	key = key.strip("[']").encode('utf-8')

	# variable to store output
	out = ''

	# Demodulate based on given modulation scheme
	# BPSK
	if(modulation == "BPSK"):
		for i in symbols:
			if(complex(i) == complex((1/math.sqrt(2)), (1/math.sqrt(2)))):
				out = out + '0'
			else:
				out = out + '1'
	# QPSK
	if(modulation == "QPSK"):
		for i in symbols:
			if(complex(i) == complex((1/math.sqrt(2)), (1/math.sqrt(2)))):
				out = out + '00'
			elif(complex(i) == complex((1/math.sqrt(2)), (-1/math.sqrt(2)))):
				out = out + '01'
			elif(complex(i) == complex((-1/math.sqrt(2)), (1/math.sqrt(2)))):
				out = out + '10'
			elif(complex(i) == complex((-1/math.sqrt(2)), (-1/math.sqrt(2)))):
				out = out + '11'
	# 16 QAM
	if(modulation == "QAM"):
		for i in symbols:
			if(complex(i) == complex((1/math.sqrt(10)), (1/math.sqrt(10)))):
				out = out + '0000'
			elif(complex(i) == complex((1/math.sqrt(10)), (3/math.sqrt(10)))):
				out = out + '0001'
			elif(complex(i) == complex((3/math.sqrt(10)), (1/math.sqrt(10)))):
				out = out + '0010'
			elif(complex(i) == complex((3/math.sqrt(10)), (3/math.sqrt(10)))):
				out = out + '0011'
			elif(complex(i) == complex((1/math.sqrt(10)), (-1/math.sqrt(10)))):
				out = out + '0100'
			elif(complex(i) == complex((1/math.sqrt(10)), (-3/math.sqrt(10)))):
				out = out + '0101'
			elif(complex(i) == complex((3/math.sqrt(10)), (-1/math.sqrt(10)))):
				out = out + '0110'
			elif(complex(i) == complex((3/math.sqrt(10)), (-3/math.sqrt(10)))):
				out = out + '0111'
			elif(complex(i) == complex((-1/math.sqrt(10)), (1/math.sqrt(10)))):
				out = out + '1000'
			elif(complex(i) == complex((-1/math.sqrt(10)), (3/math.sqrt(10)))):
				out = out + '1001'
			elif(complex(i) == complex((-3/math.sqrt(10)), (1/math.sqrt(10)))):
				out = out + '1010'
			elif(complex(i) == complex((-3/math.sqrt(10)), (3/math.sqrt(10)))):
				out = out + '1011'
			elif(complex(i) == complex((-1/math.sqrt(10)), (-1/math.sqrt(10)))):
				out = out + '1100'
			elif(complex(i) == complex((-1/math.sqrt(10)), (-3/math.sqrt(10)))):
				out = out + '1101'
			elif(complex(i) == complex((-3/math.sqrt(10)), (-1/math.sqrt(10)))):
				out = out + '1110'
			elif(complex(i) == complex((-3/math.sqrt(10)), (-3/math.sqrt(10)))):
				out = out + '1111'


	# Writing encrypted binary data after demodulation to txt file
	outputBinary = open(base+"_encryptedBinary_out.txt", "w")
	outputBinary.write(out)

	# retrieve key
	fernet = Fernet(key)
	
	# convert encrypted binary back to ASCII chars for encoding
	# separates the binary by every 8 bits for conversion to ASCII
	byte_array = []
	for i in range(0, len(out), 8):
		byte_array.append(out[i : i+8])
	
	encryptedASCII = ''
	# converts every byte to ASCII char for decryption
	for b in byte_array:
		try:
			n = int(b, 2)
			encryptedASCII = encryptedASCII + str(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
		except:
			continue
	
	# Encoding and then decrypting each byte of the encrypted data
	decrypted = fernet.decrypt(encryptedASCII.encode('utf-8'))

	# write decyrpted binary data to file
	with open(base+'_decryptedBinary.txt', 'wb') as decrypted_file:
		decrypted_file.write(decrypted)

	# separates the decrypted binary by every 8 bits for conversion to ASCII
	byte_array = []
	for i in range(0, len(decrypted), 8):
		byte_array.append(decrypted[i : i+8])
		
	outputText = ''
	# converts every byte of decrypted binary data to ASCII text
	for b in byte_array:
		try:
			n = int(b, 2)
			outputText = outputText + str(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
		except:
			continue
	
	# writes converted ASCII text to base_decryptedText.txt file for final output
	outputTextFile = open(base+"_decryptedText.txt", "w")
	outputTextFile.write(outputText)

	print("Successfully Decrypted file! Results are stored in " + base +"_decryptedText.txt\n")




def main():
	print("Welcome to our Encryption/Decryption Application!\n")
	found = False
	runChoice = True
	
	while runChoice:

		while True:
			# choose what user wants to do 
			choice = int(input("Would you like to Encrypt (1) or Decrypt (2) a file?:\n"))
			
			# check validity of input
			if ((choice != 1) and (choice != 2)):
				print("Invalid Input")
			
			else:
				break

			# begin process
		try:
			fName = input("Please enter the name of the file you wish to encrypt or decrypt:\n")
			if(choice == 1):
				fOpen = open(fName, 'r')
			elif(choice ==  2):
				with open(fName, newline='') as decryptFile:
					reader = csv.reader(decryptFile)
					symbols = []
					for row in reader:
						# store data (there are only 2 rows)
						symbols.append((row))
					
					# get data, moulation scheme, and key for decryption
					modulation = str(symbols[1])
					key = symbols[2][0]
					symbols = symbols[0]
					for i in range(len(symbols)):
						# remove parenthesis
						symbols[i] = symbols[i].strip("()")
					# remove empty entries
					symbols.remove("")
					
		except:
			# error if file not valid
			print("Unable to locate file")

		finally:
			# encrypt
			if(choice == 1):
				encrypt(fOpen, fName)
			# decrypt
			if(choice == 2):
				decrypt(fName, symbols, modulation, key)

			# see if user wants to continue and end if not
			userChoice = int(input("Please enter (0) to encrypt/decrypt again. If not, type any other key.\n"))
		if(userChoice != 0):
			runChoice = False
			print("Encrypt/Decrypt Driver Exited Successfully.")


if(__name__ == '__main__'):
	main()