''' Zanigma Card Cipher'''
''' by KryptoMagick (Karl Zander) '''
from random import shuffle

class ZANIGMA:
    def __init__(self):
        self.red = list(range(26))
        self.black = list(range(26))
        
    def gen_rand_decks(self):
    	shuffle(self.red)
    	shuffle(self.black)
    	
    def step(self):
         self.black.insert(self.red[self.red[0]], self.black.pop(0))
         self.red.insert(self.black[self.black[0]], self.red.pop(0))
    		
    		
    def encrypt_letter(self, letter):
        self.step()
        num = ord(letter) - 65
        num = self.red[num]
        num = self.black[num]
        return chr(num + 65)
        
    def decrypt_letter(self, letter):
        self.step()
        num = ord(letter) - 65
        num = self.black.index(num)
        num = self.red.index(num)
        return chr(num + 65)

    def encrypt(self, letters):
        ctxt = []
        for x in range(len(letters)):
            letter = self.encrypt_letter(letters[x])
            ctxt.append(letter)
        return "".join(ctxt)

    def decrypt(self, letters):
        ptxt = []
        for x in range(len(letters)):
            letter = self.decrypt_letter(letters[x])
            ptxt.append(letter)
        return "".join(ptxt)
        
zanigma = ZANIGMA()
zanigma.gen_rand_decks()
msg = "HELLOWORLD"
ctxt = zanigma.encrypt(msg)
print(ctxt)
