from random import randrange, shuffle
from datetime import datetime

oddelovac = '-' * 40
print(oddelovac)
print('Hi, there')
print(oddelovac)
print('''I've generated a random 4 digit number for you.
Let's play a bulls and cows game.''')
print(oddelovac)

#selection of random four digit number to set (uniqueness)
setik = set()
while len(setik) < 4:
        setik.add(randrange(0,9))

#creation of a list from the set above and shuffle if there is a zero number on first index. Probability of four zeros is a ghost of a chance.
tajne_cislo = list(setik)
while tajne_cislo[0] == 0:
    shuffle(tajne_cislo)
print('tajné číslo =', tajne_cislo)
    
cislo_hrace = []
pocitadlo_pokusu = 0
#while loop until the user gets the right number
while cislo_hrace != tajne_cislo:
    pocitadlo_pokusu +=1
    cislo_hrace = []
    cas_zacatku = datetime.now() 

    try:
        cislo = int(input('Enter a number: '))
    except ValueError:
        print('Not all entries are numbers, try again')
        continue

    cislo = list(str(cislo))
    for i in cislo:
        cislo_hrace.append(int(i))

# user inserted number consisting ofless or more then four digits, or inserted number starting with zero.
    if len(cislo_hrace) < 4 or len(cislo_hrace) > 4:
        print('Try it again, with 4 digit number. Note: Zero number is not allowed as first digit')
        continue

#verification of unieqness of users given number.
    cislo_hrace_set = set(cislo_hrace)
    if len(cislo_hrace_set) < 4:
        print('Some of your numbers are duplicates, try it again')
        continue

    bulls = 0
    for index, cislo in enumerate(cislo_hrace):
        if cislo == tajne_cislo[index]:
            bulls += 1
        if bulls == 1:
            bejci = 'Bull'
        else:   
            bejci = 'Bulls'

    cows = 0
    for indx, cisl in enumerate(cislo_hrace):
        if cisl in tajne_cislo and tajne_cislo[indx] != cisl:
            cows += 1
        if cows == 1:
            kravy = 'Cow'
        else:
            kravy = 'Cows'
    print( bulls, bejci, cows, kravy)
    print(oddelovac)
#Evaluation of success
if pocitadlo_pokusu <= 5:
    hodnoceni = 'awesome.'
elif pocitadlo_pokusu <= 10:
    hodnoceni = 'awerage.'
elif pocitadlo_pokusu <= 12:
    hodnoceni = 'not so good.'
else:
    hodnoceni = 'really bad mate.'

print(f'Correct!! You guessed the number in {pocitadlo_pokusu} step/s, in total time: {datetime.now() - cas_zacatku}')
print(f'That is {hodnoceni}')


