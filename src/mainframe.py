from tkinter import *
from unit import *
from cryptogram import Cryptogram
from random import shuffle, choice
from alphabet import alpha_list
import string

def encrypt(plaintext):

    plaintext = plaintext.upper()
    
    random_chars = alpha_list.copy()
    shuffle(random_chars)

    key = {plain: cipher for plain, cipher in zip(alpha_list, random_chars)}

    ciphertext = ""
    for ch in plaintext:
        if ch in key:
            ciphertext += key[ch]
        else:
            ciphertext += ch
    
    return ciphertext

class MainFrame:
    
    def __init__(self, window, quotes):
        self.quotes = quotes

        self.new_quote() #setup plaintext/ciphertext

        self.frame = Frame()#window, width=600, height=400)

        button = Button(self.frame, text="Enter", command=self.check_answer)
        button.pack(side=BOTTOM)

        self.cryptogram = Cryptogram(self.frame, self.ciphertext)
        self.cryptogram.frame.pack()


    
    def new_quote(self):
        quote = choice(self.quotes)
        self.plaintext = quote
        self.ciphertext = encrypt(quote)
    
    def get_quote(self):

        quote = choice(self.quotes)
        
        return quote


    def check_answer(self):

        user_answer = self.cryptogram.get_answer()

        #all characters not to be read from the plaintext - so punctuation and space
        char_filter = string.punctuation + ' ' 
        
        plaintext_no_punc = self.plaintext.translate(str.maketrans('', '', char_filter))

        if user_answer == plaintext_no_punc.upper():
            print("CORRECT!")
            self.cryptogram.self_destruct()
            self.new_quote()
            self.cryptogram = Cryptogram(self.frame, self.ciphertext)
            self.cryptogram.frame.pack()
            
    

    
    #TODO: make the cryptogram class have its own frame