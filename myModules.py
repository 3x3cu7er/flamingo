"""
CREATE YOUR OWN IF WHAT YOU SEEK DOESN'T EXIST
"""


class String:

    def __init__(self, elements):

        self.elements = elements

    def strips(self):
        letterWord = ''
        for letters in self.elements:
            if letters == " ":
                continue
            else:
                letterWord += letters
        return letterWord

    def splits(self):
        counter =0
        length = len(self.elements)
        for letter in self.elements:
            while counter < length:
                print(self.elements[counter],end=' ')
                counter += 1

   
