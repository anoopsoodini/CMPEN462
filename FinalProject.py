# Final Project
# James Zukowski, Chris Erhard, Anoop Soodini, Arib Hyder

import os 
import math
import csv
import binascii


fields = ['FileName', 'BPSK', 'QPSK', '16QAM']

def encrypt(file, name, fileData):

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
	
	# Used for testing. Just writing binary data after converion from ASCII to txt file to check correctness
	encoded = open("encoded.txt", "w")
	encoded.write(binaryString)

	#
	#
	# TO DO: Encrypt the binary data before modulating
	#
	#

	while True:
		print("What modulation scheme would you like to use to encrypt your file?")
		modulationChoice = int(input("Enter (1) for BPSK, (2) for QPSK, or (3) for 16QAM:\n"))

		if((modulationChoice != 1) and (modulationChoice != 2) and (modulationChoice != 3)):
			print("Invalid Input")
		
		else:
			break

	# BPSK Modulation
	if (modulationChoice == 1):
		for i in binaryString:
			if(i == '0'):
				BPSK.append(complex((1/math.sqrt(2)), (1/math.sqrt(2))))
			elif(i == '1'):
				BPSK.append(complex((-1/math.sqrt(2)), (-1/math.sqrt(2))))
		
		base = os.path.splitext(name)[0]
		f = open("BPSK"+base+".csv", "w+")

		for i in BPSK:
			f.write(str(complex(i))+",")

		# add modulation scheme for decryption
		f.write('\n' + "BPSK")
		f.close()

		fileData["BPSK"] = "BPSK"+base+".csv"


	# QPSK Modulation
	if (modulationChoice == 2):
		for i in range(0, len(binaryString), 2):
			if(binaryString[i:i+2] == '00'):
				QPSK.append(complex((1/math.sqrt(2)), (1/math.sqrt(2))))
			elif(binaryString[i:i+2] == '01'):
				QPSK.append(complex((1/math.sqrt(2)), (-1/math.sqrt(2))))
			elif(binaryString[i:i+2] == '10'):
				QPSK.append(complex((-1/math.sqrt(2)), (1/math.sqrt(2))))
			elif(binaryString[i:i+2] == '11'):
				QPSK.append(complex((-1/math.sqrt(2)), (-1/math.sqrt(2))))

		base = os.path.splitext(name)[0]

		f = open("QPSK"+base+".csv", "w+")

		for i in QPSK:
			f.write(str(complex(i))+",")
		
		# add modulation scheme for decryption
		f.write('\n' + "QPSK")
		f.close()

		fileData["QPSK"] = "QPSK"+base+".csv"

	# 16 QAM
	if (modulationChoice == 3):
		for i in range(0, len(binaryString), 4):
			if (binaryString[i:i+4] == '0000'):
				QAM.append(complex((1/math.sqrt(10)), (1/math.sqrt(10))))
			if (binaryString[i:i+4] == '0001'):
				QAM.append(complex((1/math.sqrt(10)), (3/math.sqrt(10))))
			if (binaryString[i:i+4] == '0010'):
				QAM.append(complex((3/math.sqrt(10)), (1/math.sqrt(10))))
			if (binaryString[i:i+4] == '0011'):
				QAM.append(complex((3/math.sqrt(10)), (3/math.sqrt(10))))
			if (binaryString[i:i+4] == '0100'):
				QAM.append(complex((1/math.sqrt(10)), (-1/math.sqrt(10))))
			if (binaryString[i:i+4] == '0101'):
				QAM.append(complex((1/math.sqrt(10)), (-3/math.sqrt(10))))
			if (binaryString[i:i+4] == '0110'):
				QAM.append(complex((3/math.sqrt(10)), (-1/math.sqrt(10))))
			if (binaryString[i:i+4] == '0111'):
				QAM.append(complex((3/math.sqrt(10)), (-3/math.sqrt(10))))
			if (binaryString[i:i+4] == '1000'):
				QAM.append(complex((-1/math.sqrt(10)), (1/math.sqrt(10))))
			if (binaryString[i:i+4] == '1001'):
				QAM.append(complex((-1/math.sqrt(10)), (3/math.sqrt(10))))
			if (binaryString[i:i+4] == '1010'):
				QAM.append(complex((-3/math.sqrt(10)), (1/math.sqrt(10))))
			if (binaryString[i:i+4] == '1011'):
				QAM.append(complex((-3/math.sqrt(10)), (3/math.sqrt(10))))
			if (binaryString[i:i+4] == '1100'):
				QAM.append(complex((-1/math.sqrt(10)), (-1/math.sqrt(10))))
			if (binaryString[i:i+4] == '1101'):
				QAM.append(complex((-1/math.sqrt(10)), (-3/math.sqrt(10))))
			if (binaryString[i:i+4] == '1110'):
				QAM.append(complex((-3/math.sqrt(10)), (-1/math.sqrt(10))))
			if (binaryString[i:i+4] == '1111'):
				QAM.append(complex((-3/math.sqrt(10)), (-3/math.sqrt(10))))

		base = os.path.splitext(name)[0]
		f = open("16QAM"+base+".csv", "w+")

		for i in QAM:
			f.write(str(complex(i))+",")
		
		# add modulation scheme for decryption
		f.write('\n' + "QAM")
		f.close()

		fileData["16QAM"] = "16QAM"+base+".csv"


	with open('FileHandle.csv', 'w+') as fh:
		csvWrite = csv.DictWriter(fh, fieldnames = fields)
		csvWrite.writeheader()
		csvWrite.writerow(fileData)
	

def decrypt(symbols, modulation):

	# get just string of modulation scheme
	modulation = modulation.strip("[']")

	# variable to store output
	out = ''

	# Demodulate based on given modulation scheme
	# BPSK
	if(modulation == "BPSK"):
		for i in symbols:
			if(complex(i) == complex((1/math.sqrt(2)), (1/math.sqrt(2)))):
				out = out + '0'
			# elif(complex(i) == complex((-1/math.sqrt(2)), (-1/math.sqrt(2)))):
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


	# Used for testing. Just writing binary data after demodulation to txt file to check correctness
	outputBinary = open("outputBinary.txt", "w")
	outputBinary.write(out)

	#
	#
	# TO DO: Decrypt the binary data after demodulating
	#
	#


	# separates the binary by every 8 bits for conversion to ASCII
	byte_array = []
	for i in range(0, len(out), 8):
		byte_array.append(out[i : i+8])
		
	outputText = ''
	# converts every byte to ASCII
	for b in byte_array:
		try:
			n = int(b, 2)
			outputText = outputText + str(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
		except:
			continue
	
	# writes converted ASCII characters to output.txt file
	outputTextFile = open("outputText.txt", "w")
	outputTextFile.write(outputText)


def main():

	found = False

	fileData = {'FileName': 'NULL', 'BPSK': 'NULL', 'QPSK': 'NULL', '16QAM': 'NULL'}

	while True:
		choice = int(input("Would you like to Encrypt (1) or Decrypt (2) a file?:\n"))
		
		if ((choice != 1) and (choice != 2)):
			print("Invalid Input")
		
		else:
			break

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
				
				# get data into single array and moulation scheme into string variable
				modulation = str(symbols[1])
				symbols = symbols[0]
				for i in range(len(symbols)):
					# remove parenthesis
					symbols[i] = symbols[i].strip("()")
				# remove empty entries
				symbols.remove("")
				
	except:
		print("Unable to locate file")

	finally:
		fileData['FileName'] = fName

		with open('FileHandle.csv', 'w') as fh:
			csvWrite = csv.DictWriter(fh, fieldnames = fields)
			csvWrite.writeheader()
			csvWrite.writerow(fileData)

		if(choice == 1):
			encrypt(fOpen, fName, fileData)

		if(choice == 2):
			decrypt(symbols, modulation)



if(__name__ == '__main__'):
	main()

