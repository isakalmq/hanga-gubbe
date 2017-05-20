"""gÃ¶r om ordet till en lista"""
def word_to_list (k):
    letterno = 0
    letter_list = []

    while len(letter_list) != len(k):
        letter_list.append(k[letterno])
        letterno = letterno + 1

    return letter_list

"""kollar om bokstav finns med i ordet"""
def check_letter(n, b):
    letterno = 0

    while len(n) != letterno:
        if n[letterno] == b:
            return letterno
        else:
            letterno = letterno + 1

    return False

"""Gör en lista med så många tecken som ordet har"""

def disp_list (l):

    disp = []
    
    while len(disp) != len(word):
        disp.append("_")
        

    return disp

"""hej = word_to_list(word)
print hej

guess_letter = raw_input("gissa ett ord: ")

if check_letter(hej, guess_letter):
    print "rÃ¤tt"
else:
    print "fel"
"""
word = raw_input("Skriv ett ord: ")
max_guesses = raw_input("Hur många gissningar: ")

guesses = 0
list_word = word_to_list(word)

display_word = disp_list(len(word))

print display_word

while guesses != max_guesses:
    
    guess = raw_input("Gissa en bokstav: ")
    if type(check_letter(list_word, guess)) == int :
        print "rÃ¤tt"
        display_word[check_letter(list_word, guess)] = guess
        print display_word
    else:
        print "fel"
        print display_word 
        guesses = guesses + 1
        
print "Du förlorade"


hej = raw_input("hej")
