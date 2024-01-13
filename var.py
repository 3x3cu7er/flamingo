import sys

word =input("A statement to chack $ ")
def valid(word):
    ignore = ['~', '!', '@', '#', '$', '%'," ", '^', '&', '*', '|']
    accept = ['?','_']
    islogic = False
    for let in word:
        if let.isalpha():
            if let.isdigit():
                if let in accept:
                    print("is a valid argument")
                    islogic = True
                continue
            islogic = True

        elif let in ignore:
            print("is not a valid argument")
            sys.exit()
        else:
            return  False
        return islogic

print(valid(word))