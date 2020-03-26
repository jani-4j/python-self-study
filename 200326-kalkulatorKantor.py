#9. Teraz zrobisz "mini kalkulator" do kantoru wymiany walut. 
# Chcemy wyświetlić tabelkę w postaci:

#   cur   exchange amount
#   USD   3.65     64.10958904109589
#   EUR   4.23     55.31914893617021

#w tym celu:

#-najpierw zadeklaruj zmienną amountPLN i wpisz do niej wartość 234

#-następnie wyświetl teksty rozdzielając wartości tabulatorem, 
# tak aby to co zostanie wypisane na ekranie przypominało tabelkę 
# (skorzystaj do tego z kilku poleceń print, jednolinijkowy 
# print byłby zbyt trudny do zrozumienia)

#-wartości w kolumnie amount wylicz dzieląc amountPLN przez 
# aktualny kurs USD i EUR (w tym przykładzie są to 3.65 i 4.23)

amountPLN=234
USD=3.65
EUR=4.23

#print('cur','exchange','amount',sep='\t')              #tez dziala !!!
#print('cur',"\t",'exchange',"\t",'amount')             #tez dziala !!!

print('cur','\t','exchange','\t','amount')              #zbyt dluga ilosc znakow w drogiej kolumnie
print('USD',"\t",USD,"\t\t",amountPLN/USD)              #nalezy dodac kolejny TAB aby tabela byla spujna
print('EUR',"\t",EUR,"\t\t",amountPLN/EUR)              

#10. Zadeklaruj zmienną ValueAsText i wpisz do niej wartość '123.45'
ValueAsText='123.45'

#11. Zadeklaruj zmienną factor o wartości 1.23
factor=1.23
#12. Wyświetl tekst:
#value is  "123.45" factor is "1.23" value*factor= "151.8435" 
#value is  Vslueastext factor is factor value*factor= value*factor .
#podczas obliczania value * factor skonwertuj zmienną ValueAsText na typ float
print('value is ',ValueAsText,'factor is',factor, 'value*factor =',float(ValueAsText)*factor)

print(float(ValueAsText)*factor)

print(int(float(ValueAsText))*factor)
