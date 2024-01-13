#####################################################
#####################################################
#####   cryptographic programming ####################
#####       caeser cipher                      ####################
######################################################
######################################################

plainText = input("Message to be encrypted $")
cipherText = ''


'''wordFrame = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!.?"
key =len(plainText)-1
while key>=0:
    cipherText +=plainText[key]
    key -=1
    
print( "Encrypted form : ",cipherText)'''

encryptKeys = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
    'I' : 8,
    'J' : 9,
    'K' : 10,
    'L' : 11,
    'M' : 12,
    'N' : 13,
    'O' : 14,
    'P' : 15,
    'Q' : 16,
    'R' : 17,
    'S' : 18,
    'T' : 19,
    'U' :20,
    'V' : 21,
    'W' : 22,
    'X' : 23,
    'Y' : 24,
    'Z' : 25
}

KEY = 2
size = len(plainText)-1 

while size>=0:
    convert= plainText.upper()
    cipherText += plainText[size ]
    size +=KEY
    
    # identifying their encrypted keys
    for content in plainText:
        print(encryptKeys[content.upper()])
        
print(cipherText)