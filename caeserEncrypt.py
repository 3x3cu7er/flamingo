
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

key = 2

plain = 'common sense is not all that common!'


def enc(key, plain):
    cipher = ''
    counter = 0 

    for pla in range(len(plain)):

        while counter < pla:
            cipher += plain[counter]
            counter += key
    return cipher

print(enc(key,plain))

