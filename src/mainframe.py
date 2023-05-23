from tkinter import *
from unit import *
from cryptogram import Cryptogram
from random import shuffle, choice
from alphabet import alpha_list, alpha_set
from collections import Counter
import time
import string


def encrypt_key_freq(plaintext):

    plaintext = plaintext.upper()

    key_dict = {}

    freq_dict = {}

    freqs = Counter()

    main_set = alpha_set.copy()

    for letter in plaintext:
        if letter in alpha_set:

            if letter not in key_dict:
                temp_set = main_set.copy()
                try:
                    temp_set.remove(letter)
                except:
                    pass
                ciphertext = choice(tuple(temp_set))
                main_set.remove(ciphertext)
                key_dict[letter] = ciphertext

            freqs[key_dict[letter]] += 1
    
    print(freqs)

    ciphertext = ""
    for ch in plaintext:
        if ch in key_dict:
            ciphertext += key_dict[ch]
        else:
            ciphertext += ch

    key_dict = {key_dict[k]:k for k in key_dict}

    return ciphertext, key_dict, freqs


class MainFrame:
    
    def __init__(self, window, quotes):
        self.quotes = quotes

        self.new_quote() #setup plaintext/ciphertext

        self.frame = Frame(window)#window, width=600, height=400)

        enter_button = Button(self.frame, text="Enter", command=self.check_answer)
        enter_button.pack(side=BOTTOM)

        clear_button = Button(self.frame, text="Clear", command=self.clear)
        clear_button.pack(side=BOTTOM)

        self.cryptogram = Cryptogram(self.frame, self.ciphertext, self.freqs)
        self.cryptogram.entry_units[0].entry.focus_set()
        self.cryptogram.frame.pack()

        window.bind("<Return>", self.enter_pressed)#print("hi"))

    
    def new_quote(self):
        quote = choice(self.quotes)
        self.plaintext = quote
        self.ciphertext, self.key_dict, self.freqs = encrypt_key_freq(quote)

    def clear(self):
        self.cryptogram.clear_answer()
    
    def enter_pressed(self, event):
        print(time.time())
        self.check_answer()
            
    def check_answer(self):

        print(self.cryptogram.key_dict)
        print(self.key_dict)

        if self.cryptogram.key_dict == self.key_dict:
            print("CORRECT!")
            self.cryptogram.self_destruct()
            self.new_quote()
            self.cryptogram = Cryptogram(self.frame, self.ciphertext, self.freqs)
            self.cryptogram.entry_units[0].entry.focus_set() #set focus to first entry
            self.cryptogram.frame.pack()
        else:
            print("WRONG!")

    
    #TODO: make the cryptogram class have its own frame