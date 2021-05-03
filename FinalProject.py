# Final Project
# James Zukowski, Chris Erhard, Anoop Soodini, Arib Hyder

import os 
import math
import csv



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
	binaryString = ''.join(bin(ord(c)) for c in string).replace('b', '')

	while True:
		print("What modulation scheme would you like to use to encrypt your file?")
		modulationChoice = int(input("Enter (1) for BPSK, (2) for QPSK, or (3) for 16QAM: "))

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

		f.close()

		fileData["BPSK"] = "BPSK"+base+".csv"



	# QPSK Modulation
    # indexing in python is non-inclusive
	if (modulationChoice == 2):
		for i in range(0, len(binaryString)):
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

		f.close()

		fileData["QPSK"] = "QPSK"+base+".csv"

	if (modulationChoice == 3):
		for i in range(0, len(binaryString), 4):
			if (binaryString[i:i+4] == "0000"):
				QAM.append(complex((1/math.sqrt(10)), (1/math.sqrt(10))))
			if (binaryString[i:i+4] == "0001"):
				QAM.append(complex((1/math.sqrt(10)), (3/math.sqrt(10))))
			if (binaryString[i:i+4] == "0010"):
				QAM.append(complex((3/math.sqrt(10)), (1/math.sqrt(10))))
			if (binaryString[i:i+4] == "0011"):
				QAM.append(complex((3/math.sqrt(10)), (3/math.sqrt(10))))
			if (binaryString[i:i+4] == "0100"):
				QAM.append(complex((1/math.sqrt(10)), (-1/math.sqrt(10))))
			if (binaryString[i:i+4] == "0101"):
				QAM.append(complex((1/math.sqrt(10)), (-3/math.sqrt(10))))
			if (binaryString[i:i+4] == "0110"):
				QAM.append(complex((3/math.sqrt(10)), (-1/math.sqrt(10))))
			if (binaryString[i:i+4] == "0111"):
				QAM.append(complex((3/math.sqrt(10)), (-3/math.sqrt(10))))
			if (binaryString[i:i+4] == "1000"):
				QAM.append(complex((-1/math.sqrt(10)), (1/math.sqrt(10))))
			if (binaryString[i:i+4] == "1001"):
				QAM.append(complex((-1/math.sqrt(10)), (3/math.sqrt(10))))
			if (binaryString[i:i+4] == "1010"):
				QAM.append(complex((-3/math.sqrt(10)), (1/math.sqrt(10))))
			if (binaryString[i:i+4] == "1011"):
				QAM.append(complex((-3/math.sqrt(10)), (3/math.sqrt(10))))
			if (binaryString[i:i+4] == "1100"):
				QAM.append(complex((-1/math.sqrt(10)), (-1/math.sqrt(10))))
			if (binaryString[i:i+4] == "1101"):
				QAM.append(complex((-1/math.sqrt(10)), (-3/math.sqrt(10))))
			if (binaryString[i:i+4] == "1110"):
				QAM.append(complex((-3/math.sqrt(10)), (-1/math.sqrt(10))))
			if (binaryString[i:i+4] == "1111"):
				QAM.append(complex((-3/math.sqrt(10)), (-3/math.sqrt(10))))

		base = os.path.splitext(name)[0]
		f = open("16QAM"+base+".csv", "w+")

		for i in QAM:
			f.write(str(complex(i))+",")

		f.close()

		fileData["16QAM"] = "16QAM"+base+".csv"


	with open('FileHandle.csv', 'w+') as fh:
		csvWrite = csv.DictWriter(fh, fieldnames = fields)
		csvWrite.writeheader()
		csvWrite.writerow(fileData)
	


def decrypt(file):
	pass




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
		fOpen = open(fName, 'r')
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
			decrypt(fOpen)



if(__name__ == '__main__'):
	main()

