### PROJEKT 2: WTYCZKA DO QGIS

Wtyczka służy do obliczania przewyższenia i pola powierzchni.

#Spis treści
...
costam

#### Wymagania
```
Python 3.11
Biblioteka numpy
System operacyjny Windows 10 lub 11
program QGIS wersja 3.34.4
biblioteka qgis.PyQt
biblioteka qgis.core
biblioteka PyQt5
```
#### Funkcje wtyczki
 ```
 1. Obliczanie przewyższenia pomiędzy dwoma punktami
 2. Obliczanie pola powierzchni pomiędzy punktami
 ```
#### Sposób użycia wtyczki

1. Na samym początku należy pobrać wtyczkę i umieścić ją w katalogu z wtyczkami dla programu QGIS. Następnie należy otworzyć program QGIS, przejść do zakładki Wtyczki>Zarządzanie wtyczkami i na samej górze w pasku wyszukiwania wpisać "Wtyczka". 
Po lewej stronie od jej nazwy pojawi się checkbox, który należy zaznaczyć.
2. Do nowego projektu należy dodać warstwy warstwy z atrybutami geometrii (SHP lub SHX).
3. Należy zaznaczyć wybrane punkty za pomocą narzędzia "Zaznacz obiekty" i uruchomić wtyczkę. (Warstwa z wybranymi punktami musi być aktywna)

###Liczenie przewyższenia