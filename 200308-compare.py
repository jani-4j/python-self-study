#Utwurz zmienna MyText i przypisz jej nastepujaca wartosc:
# 'A good programmer is someone who always looks both ways 
# before crossing a one-way street'

MyText='A good programmer is someone who always looks both ways before crossing a one-way street'
MyText.upper()

#Wyswietl tekst napisany tylko wielkimi literami
MyText.lower()

#Sprawdz czy tekst kończy sie slowem 'street'
MyText.endswith('street')

#Sprawdz czy tekst jest zapisany wielkimi literami
MyText.isupper()

#Sprawdz, czy tekst skonwertowany do wielkich liter jest 
# zapisany wielkimi literami (Zastosuj zlozenie funkcji)
MyText.upper().isupper()

#Poszukaj na ktzrej pozycji (liczac od zera) znajduje sie 
# w tekście slowo 'one'
MyText.find('one')

#Zamień w tekście slowo 'one' na '1'
MyText.replace('one','1')

#Zamień w tekście slowo 'one' na '1' a slowo 'both' na 2
MyText.replace('one','1').replace('both','2')

#Sprawdz czy napis jest liczba, liczba dziesietna, napisem bez cyfr, napisem z literami i cyframi
jakasliczba = 1000
jakasliczba.isalpha()



