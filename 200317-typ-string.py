#1. Pracujesz w Urzędzie Stanu Cywilnego i ... korzystasz z Pythona.
#  Dziewczyna o imieniu Kasia i nazwisku Sowa wychodzi za mąz za chłopaka o nazwisku Mrugała.
#  Pani Kasia chce zachować oba nazwiska.

#Zdefiniuj zmienne firstName, famillyName i lastName i przypisz do nich 
# napisy odpowiadające imieniu, nazwisku panieńskim i nowym nazwisku.
# Następnie utwórz zmienną newName i zapisz w niej wynik konkatenacji 
#(czyli złączenia napisów) dla firstname, spacji, familyName, spacji i lastName.
# Wyświetl to nowe nazwisko


FirstName = 'Kasia'
FamilyName = 'Sowa'
LastName = 'Mrugala'

NewName = FirstName+FamilyName+LastName
print(NewName)

NewName1 = FirstName+" "+FamilyName+" "+LastName
print(NewName1)
#print(NewName1)

#2. Zdefiniuj zmienną music o następującej zawartości 
# (są to tytuły i autorzy piosenek z filmu Minionki):

#"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner 
# "I'm a Man" Steve Winwood 

#Uwaga! Ten napis zawiera zarówno apostrof jak i cudzysłów,
#więc musisz zmodyfikować zapis metodami pokazanymi na tej lekcji,
#zeby zdefiniowanie zmiennej się udało.