import random
import string
from pickle import FALSE, TRUE
def gen_pass(minLength,numbers=True,speical_chars=True):
    letters=string.ascii_letters
    digits=string.digits
    speical=string.punctuation
    characters=letters
    if numbers:
        characters+=digits
    if speical_chars:
        characters+=speical
    
    psword=""
    meet=False
    has_speical=False
    has_number=False
    
    while not meet or len(psword) <minLength:
        new_char=random.choice(characters)
        psword+=new_char
        
        if new_char in digits:
            has_number=True
        elif new_char in speical:
            has_speical=True
            
        meet=True
        if numbers:
            meet=has_number
        if speical_chars:
            meet=meet and has_speical
            
    return psword

minLength=int(input("Enter the minimum length : "))
has_number=input("Do you want to have numbers ? (y/n) : ").lower()=="y"
has_speical=input("Do you want to have speical characters ? (y/n) : ").lower()=="y"

psword=gen_pass(minLength,has_number,has_speical)
print("the password is : "+psword)












