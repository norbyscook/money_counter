# script to add the total amount of money stated in a text file 
# format of money: $ [number] [unit]
# for example: $ 1 million
# currently takes in "million" and "billion" as units.

def main():
    filePtr = open("text.txt", "r", encoding="utf-8")
    sum = add_loop(filePtr)
    print(str(sum) + " billion")
    filePtr.close()

# loop through document and add money in billions
def add_loop(filePtr):
    character = ' '
    sum = 0

    while (character != ''): # while not at eof
        character = filePtr.read(1)
        if (character == '$'):
            sum += extract_num(filePtr)

    return sum

# helper functions -----------------------------------

def extract_num(filePtr):
    num = read_number(filePtr)
    units = read_identifier(filePtr)
    num = modify_num_size(units, num)

    return num

def modify_num_size(units, num):
    if (units == "million"):
        num /= 1000
    elif (units == "billion"):
        return num
    else: # assume unit is in dollars
        num /= 1000000000

    return num

def read_identifier(filePtr):
    character = ' '
    identifier = ""
   
    while (not character.isalpha()):
        character = filePtr.read(1)

    while (character.isalpha()):
        identifier += character
        character = filePtr.read(1)

    return identifier

def read_number(filePtr):
    character = ' '
    num_str = " "

    while (not is_num_char(character)):
        character = filePtr.read(1)

    while (is_num_char(character)):
        if (character == ','):
            pass
        else:
            num_str += character
        character = filePtr.read(1)

    return float(num_str)

def is_num_char(character):
    if (character.isdigit()):
        return True
    elif (character == ','):
        return True
    elif (character == '.'):
        return True

    return False
    
if (__name__ == "__main__"):
    main()
