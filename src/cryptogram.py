from tkinter import *

def focused(event):
    print("FOCUS!")

class Cryptogram:
    
    def __init__(self, window, text):
        self.text = text
        self.window = window
        self.entries = self.create_entries()
        self.current_focus = None
    
    def update_focus(self, entry):
        print("focus updated")
        self.current_focus = entry

    def character_checks(self, entry_text):
        print(self)
        print(entry_text)
        print(len(entry_text.get()))
        print("character checks")
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[-1])
        
        if entry_text.get() != " " and len(entry_text.get()) > 0:
            self.set_next_focus()

    def create_entries(self):
        entries = []
        for ch in self.text:
            entry_text = StringVar()
            entry = Entry(self.window, width = 3 ,textvariable= entry_text)
            entry.pack(side=LEFT, padx=5, pady=5)
            entries.append(entry)

            #bind update focus function to whenever the focus enters this entry
            entry.bind("<FocusIn>", lambda *args: self.update_focus(entry))

            entry.bind("<Key>", lambda *args: self.character_checks(entry_text))

            #wheenver entry text var changes, perform char checks on it
            entry_text.trace_add("write", lambda *args: self.character_checks(entry_text))

        return entries

    def set_next_focus(self):
        print("setting next focus")
        #find the index of the current focus entry
        index = self.entries.index(self.current_focus)

        #set the current focus to be the next entry in the list. however, if it's the last entry than keep the same focus
        self.current_focus = self.entries[index + 1] if index + 1 < len(self.entries) else self.current_focus

    
    #TODO: maybe create a 'unit' class which has both entry and the text letter above/below it. each unit is in its own canvas