# write a function named plaintext that takes a single parameter of a string encoded in this format: before
# each charachter of the message, add a digit and a series of other charachters. the digit should correspond to the
# number of charachters that will precede teh messages actual, meaningful charachter.
# it should return teh decoded word in string form

"""  my pseudocode:
	#convert string to a list
	#enumerate list
	#parse string where the element and the index plus one returns the desired index
	#return decoded message of desired indexes  """

encoded_message = "0h2ake1zy"
#encoded_message ="2xwz"
#encoded_message = "0h2zyi2467"

def plaintext(string):
	while(True):
		#encoded_message = raw_input("enter encoded message:")
		?? index, character in enumerate(list(encoded_message)):
			character = int(character)
			decoded_msg = index + character + 1
		print decoded_msg

def main():
	
	plaintext("0h2ake1zy")
	
if __name__ == '__main__':
	main()