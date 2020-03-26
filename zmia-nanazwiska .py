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
