def toTranspositionEncryption(key, message):
        
        ciphertext =''
        
        for columns in range(key):
            
            while columns < len(message):
                ciphertext += message[columns]
                columns +=key
        return ''.join(ciphertext)


key = int(input('Enter encryption key $'))
message = input('Enter encryption message $')
text = toTranspositionEncryption(key,message)

print(text)
    
