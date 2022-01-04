wejscie = []            #utworzenie list w których jest przechowywana liczba zwycięzców w zależnosći od otrzymanych kart
winners = []
winners_2 = []
max=0
n = input("enter length ")
for i in range(0, int(n)):
    k=input()
    wejscie.append(k) # push your entered value

for i in range(0, len(wejscie)):
    a=list(wejscie[i])    #podział listy na pojedyncze znaki
    wynik=0
    liczba_asów=0         #liczba asów w kartach
    for j in range(0, len(a)):      #przypisanie kolejnych wartośći w zależnośći od wylosowanych figur
        if a[j]=="2":
            wynik+=2
        elif a[j]=="3":
            wynik+=3
        elif a[j]=="4":
            wynik+=4
        elif a[j]=="5":
            wynik+=5
        elif a[j]=="6":
            wynik+=6
        elif a[j]=="7":
            wynik+=7
        elif a[j]=="8":
            wynik+=8
        elif a[j]=="9":
            wynik+=9
        elif a[j]=="T" or a[j]=="J" or a[j]=="Q" or a[j]=="K":
            wynik+=10 
        elif a[j]=="A": 
            liczba_asów+=1


    if liczba_asów>0:                       #zliczanie asów pozostawiono na koniec ponieważ to 
        for k in range(0,liczba_asów-1):    #czy doliczymy 1 cz 11 punktów zależy od sumy dotychczasowych punktów
            wynik+=1
        if wynik<=10:
            wynik+=11
        else: 
            wynik+=1
   
    print(wynik)                            #instrukacja warunkowa, która decyduje czy wyświetlamy zwycięzców z liczbą 21 punktów
    if wynik <21 and wynik>max:             #czy zawodników, którzy byli najbliżej tej wartosći ale nie przekroczyli liczby 21
        max=wynik
        winners_2.clear()
        winners_2.append(i+1)
    
    elif wynik <21 and  wynik == max:
       max = wynik
       winners_2.append(i+1) 

    elif wynik == 21:
        winners.append(i+1)

                                            #wyświetlanie wyników
if len(winners)>0:
    print(len(winners))
    for i in range (0, len(winners)):
        print(winners[i], end=' ')
else:
    print(len(winners_2))
    for i in range (0, len(winners_2)):
        print(winners_2[i], end=' ')



