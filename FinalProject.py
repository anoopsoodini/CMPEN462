# Final Project
# James Zukowski, Chris Erhard, Anoop Soodini, Arib Hyder

import os 
import math
import csv

def encrypt(file, name):

	string = ""
	BPSK = []

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
	counter = 0
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


	







def decrypt(file):
	pass




def main():

	found = False

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
		with open('FileHandle.csv', 'r') as f1:
			csvRead = csv.reader(f1)
			line = 0
			for row in csvRead:
				if(row[0]==fName):
					print("File found in database")
					found = True
					break
		
		if not (found):
			with open('FileHandle.csv', 'w') as f2:
				csvWrite = csv.writer(f2)

				csvWrite.writerow(fName)
					

		if(choice == 1):
			encrypt(fOpen, fName)

		if(choice == 2):
			decrypt(fOpen)



if(__name__ == '__main__'):
	main()

