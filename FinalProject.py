# Final Project
# James Zukowski, Chris Erhard, Anoop Soodini, Arib Hyder

import os 

def encrypt(file):

	string = ""

	while True:

		line = file.readline()

		if not line:
			break
		else:
			string += line

	double(string)

	binaryString = bin(string)





def decrypt(file):
	pass




def main():
	choice = int(input("Would you like to Encrypt (1) or Decrypt (2) a file?:\n"))

	if((choice != 1) and (choice != 2)):
		raise Exception("Invalid Input, Enter 1 to Encrypt or 2 to Decrypt")

	fName = input("Please enter the name of the file you wish to encrypt or decrypt:\n")

	try:
		fOpen = open(fName, 'r')
	except:
		print("Unable to locate file")

	finally:
		if(choice == 1):
			encrypt(fOpen)

		if(choice == 2):
			decrypt(fOpen)



if(__name__ == '__main__'):
	main()

