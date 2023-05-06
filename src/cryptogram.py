from tkinter import *
from unit import *
from units import Units
import string


class Cryptogram:
    
    def __init__(self, window, ciphertext, plaintext):
        self.ciphertext = ciphertext
        self.plaintext = plaintext
        self.main_frame = Frame(window, width=600, height=400)

        self.units = Units(self.main_frame, ciphertext)
        self.units.frame.pack()

        button = Button(self.main_frame, text="Enter", command=self.check_answer)
        button.pack()

    def check_answer(self):
        user_answer = ""

        for unit in self.units.entry_units:
            entry = unit.entry
            user_answer += entry.get().lower()
        
        #all characters not to be read from the plaintext - so punctuation and space
        char_filter = string.punctuation + ' ' 
        
        plaintext_no_punc = self.plaintext.translate(str.maketrans('', '', char_filter))

        if user_answer == plaintext_no_punc.lower():
            print("CORRECT!")
    

    
    #TODO: make the cryptogram class have its own frame