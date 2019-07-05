#Substitution cipher
#Source: https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_simple_substitution_cipher

import random, sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
   message = ''
   #If a file is provided the it is open and the message inside assigned to the message variable
   if len(sys.argv) > 1:
      with open(sys.argv[1], 'r') as f:
         message = f.read()
    #if no file was provided then the user is asked for input
   else:
      message = raw_input("Enter your message: ") #getting the message to be encrypted/decrypted
   mode = raw_input("E for Encrypt, D for Decrypt: ") #encrypt or decrypt the message
   key = ''
   
   #if the key is not invalid then the user is asked for a key of 26 characters or to leave it empty to get a random one
   #if the key is not 26 characters or left empty then an error is showed
   while checkKey(key) is False:
      key = raw_input("Enter 26 ALPHA key (leave blank for random key): ")
      if key == '':
         key = getRandomKey()
      if checkKey(key) is False:
		print('There is an error in the key or symbol set.')
    #calling the function to encrypt or decrypt the message provided
   translated = translateMessage(message, key, mode)
   #print the key used. Very useful if the key is randmonly created
   print('Using key: %s' % (key))
   
   #if a file was provided then the encrypted/decrypted message is written into the file
   #if a message was provided by user input then the encrypted/decrypted message is printed
   if len(sys.argv) > 1:
      fileOut = 'enc.' + sys.argv[1]
      with open(fileOut, 'w') as f:
         f.write(translated)
      print('Success! File written to: %s' % (fileOut))
   else: print('Result: ' + translated)

# Store the key into list, sort it, convert back, compare to alphabet. Checks if the key is valid (has 26 characters)
def checkKey(key):
   keyString = ''.join(sorted(list(key)))
   return keyString == LETTERS
#function that encrypt or decrypt the message using the key provided. indexes of characters are used for the substitution
def translateMessage(message, key, mode):
   translated = ''
   charsA = LETTERS
   charsB = key
   
   # If decrypt mode is detected, swap A and B
   if mode == 'D':
      charsA, charsB = charsB, charsA
   for symbol in message:
      if symbol.upper() in charsA:
         symIndex = charsA.find(symbol.upper())
         if symbol.isupper():
            translated += charsB[symIndex].upper()
         elif symbol.islower():
            translated += charsB[symIndex].lower()
         else:
            translated += symbol
   return translated

#function that generates a random key with 26 characters. It shuffles the alphabet to do so.
def getRandomKey():
   randomList = list(LETTERS)
   random.shuffle(randomList)
   return ''.join(randomList)
if __name__ == '__main__':
   main()
