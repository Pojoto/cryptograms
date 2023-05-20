from tkinter import *
from unit import *
from cryptogram import Cryptogram
from random import shuffle, choice
from alphabet import alpha_list, alpha_set
import time
import string


def encrypt_and_key(plaintext):

    plaintext = plaintext.upper()

    key_dict = {}

    for letter in plaintext:
        if letter in alpha_set and letter not in key_dict:
            key_dict[letter] = ""

    #
    main_set = alpha_set.copy()
    for plainkey in key_dict:
        temp_set = main_set.copy()
        try:
            temp_set.remove(plainkey)
        except:
            pass
        ciphertext = choice(tuple(temp_set))
        main_set.remove(ciphertext)
        key_dict[plainkey] = ciphertext

    ciphertext = ""
    for ch in plaintext:
        if ch in key_dict:
            ciphertext += key_dict[ch]
        else:
            ciphertext += ch
    print(ciphertext)
    return ciphertext#, key


class MainFrame:
    
    def __init__(self, window, quotes):
        self.quotes = quotes

        self.new_quote() #setup plaintext/ciphertext

        self.frame = Frame(window)#window, width=600, height=400)

        enter_button = Button(self.frame, text="Enter", command=self.check_answer)
        enter_button.pack(side=BOTTOM)

        clear_button = Button(self.frame, text="Clear", command=self.clear)
        clear_button.pack(side=BOTTOM)

        self.cryptogram = Cryptogram(self.frame, self.ciphertext)
        self.cryptogram.entry_units[0].entry.focus_set()
        self.cryptogram.frame.pack()

        window.bind("<Return>", self.enter_pressed)#print("hi"))

    
    def new_quote(self):
        quote = choice(self.quotes)
        self.plaintext = quote
        self.ciphertext = encrypt_and_key(quote)

    def clear(self):
        self.cryptogram.clear_answer()
    
    def enter_pressed(self, event):
        print(time.time())
        self.check_answer()

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
            self.cryptogram.entry_units[0].entry.focus_set() #set focus to first entry
            self.cryptogram.frame.pack()
        else:
            print("WRONG!")
            
    

    
    #TODO: make the cryptogram class have its own frame