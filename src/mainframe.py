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

        self.button_frame = Frame(self.frame)
        self.button_frame.pack(side=BOTTOM)



        self.enter_button = Button(self.button_frame, text="Enter", command=self.check_answer)
        self.enter_button.pack(side=LEFT)

        self.clear_button = Button(self.button_frame, text="Clear", command=self.clear)
        self.clear_button.pack(side=LEFT)

        self.skip_button = Button(self.button_frame, text="Skip", command=self.skip)
        self.skip_button.pack(side=LEFT)

        self.prev_time = Label(self.frame, text="Previous Solve Time: ")
        self.prev_time.pack(side=BOTTOM)

        self.start_time = time.time()

        self.new_cryptogram()

        window.bind("<Return>", self.enter_pressed)

    def new_cryptogram(self):
        self.new_quote()
        self.cryptogram = Cryptogram(self.frame, self.ciphertext, self.freqs)
        self.cryptogram.entry_units[0].entry.focus_set() #set focus to first entry
        self.cryptogram.frame.pack()
        diff = time.time() - self.start_time
        self.prev_time.configure(text="Previous Solve Time: " + str(diff))
        self.start_time = time.time()
    
    def new_quote(self):
        quote = choice(self.quotes)
        self.plaintext = quote
        self.ciphertext, self.key_dict, self.freqs = encrypt_key_freq(quote)

    def clear(self):
        self.cryptogram.clear_answer()
    
    def enter_pressed(self, event):
        print(time.time())
        self.check_answer()
    
    def skip(self):
        self.cryptogram.self_destruct()
        self.new_cryptogram()
            
    def check_answer(self):

        if self.cryptogram.key_dict == self.key_dict:
            print("CORRECT!")
            self.cryptogram.self_destruct()
            self.new_cryptogram()
        else:
            print("WRONG!")
