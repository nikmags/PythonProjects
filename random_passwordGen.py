#Purpose of this program is to provide users with a password generator that provides 8 units of len and has num, letter_cap, letter_lower, and sign inputs.

import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

def main():
    uppercaseLetter1 = chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
    uppercaseLetter2 = chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
    sign = chr(random.randint(35,42)) #Generate a random sign value letter (based on ASCII code)
    numvalue = chr(random.randint(48,57)) #Generate a random numerical value letter (based on ASCII code)
    lowercaseLetter1 = chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)
    sign2 = chr(random.randint(35,42)) #Generate a random sign value letter (based on ASCII code)
    numvalue2 = chr(random.randint(48,57)) #Generate a random numerical value letter (based on ASCII code)
    lowercaseLetter2 = chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)

    #Generate password using all the characters, in random order
    password = uppercaseLetter1 + uppercaseLetter2 + sign + numvalue + lowercaseLetter1 + sign2 + numvalue2 + lowercaseLetter2
    password = shuffle(password)

    #Output
    print(password)

main()

