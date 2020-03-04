print("cdv")
print(10)
'''
komentarz
blokowy
'''
#potęgowanie
potega=2 ** 10
print(potega)
#pobieranie danych z klawiatury
name=input()
#   +konkatenacja
print("Twoje imię: "+name)
surname=input()
print("Twoje imię: "+name+", nazwisko: "+surname)

'''
Uzytkownik podaje z klawiatury swoj wiek,
Wyswietl dane w formacie Twoj wiek: ...lat
'''
print("Podaj swój wiek: ", end="")
age=input()
print(type(age))
# interpolacja
print("Twój wiek: ",age,"lata")

age1=20
print(type(age1))

surname="Kowalski"
firstLetter=surname[0]
print(firstLetter)
length= len(surname)
print(length)

lastLetter=surname[len(surname)-1]
print(lastLetter)

lastLetter=surname[-1]
print(lastLetter)
