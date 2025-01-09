# 0_Dokumentation-Testing
Für unseren Algorithmus haben wir folgende Testfälle identifiziert:

1. Leeres Array
    - Ein leeres Array ist per Definition bereits sortiert.
    - Bsp:
      - Input: []
      - Erwarteter Output: []
   

2. Array mit einem Element
    - Ein Array mit nur einem Element ist bereits sortiert.
    - Bsp:
      - Input: [42]
      - Erwarteter Output: [42]
    

3. Bereits sortiertes Array
    - Ein bereits sortiertes Array muss nicht nochmals sortiert werden
    - Bsp:
      - Input: [1, 2, 3, 4, 5]
      - Erwarteter Output: [1, 2, 3, 4, 5]
      

4. Rückwärts sortiertes Array
   - Ein Array, das in absteigender Reihenfolge vorliegt, sollte korrekt aufsteigend sortiert werden.
   - Bsp:  
     - Input: [5, 4, 3, 2, 1]
     - Erwarteter Output: [1, 2, 3, 4, 5]


5. Array mit doppelten Elementen
   - Doppelte Elemente sollten in der endgültigen sortierten Liste korrekt auftauchen.
     - Input: [3, 1, 2, 3, 4, 3]
     - Erwarteter Output: [1, 2, 3, 3, 3, 4]
 

6. Array mit negativen Zahlen
   - Der Algorithmus sollte auch mit negativen Zahlen umgehen können und sie korrekt sortieren.
     - Input: [0, -1, 3, -5, 2]
     - Erwarteter Output: [-5, -1, 0, 2, 3]
  

7. Array mit allen gleichen Elementen
   - Ein Array, in dem alle Elemente gleich sind, sollte unverändert bleiben, da es bereits sortiert ist.
     - Input: [7, 7, 7, 7, 7]
     - Erwarteter Output: [7, 7, 7, 7, 7]
        

8. Array mit gemischten positiven und negativen Zahlen
   - Ein Array, das sowohl positive als auch negative Zahlen enthält, sollte korrekt sortiert werden.
     - Input: [3, -2, 5, -1, 0, 4, -3]
     - Erwarteter Output: [-3, -2, -1, 0, 3, 4, 5]
   

9. Array mit Zahlen in zufälliger Reihenfolge
   - Eine zufällig gemischte Liste sollte korrekt sortiert werden.
     - Input: [8, 3, 1, 7, 0, 10, 2]
     - Erwarteter Output: [0, 1, 2, 3, 7, 8, 10]
     

10. Array mit vielen doppelten Elementen
    - Der Algorithmus sollte korrekt mit mehrfach vorkommenden Elementen umgehen.
      - Input: [4, 5, 4, 4, 6, 4, 5, 5]
      - Erwarteter Output: [4, 4, 4, 4, 5, 5, 5, 6]


11. Array mit Floats
    - Der Quicksort-Algorithmus sollte auch mit Gleitkommazahlen umgehen können.
      - Input: [2.1, 3.5, 1.2, 5.7, 0.5]
      - Erwarteter Output: [0.5, 1.2, 2.1, 3.5, 5.7]


 12. Eingabe in Array muss Integer oder Float sein 
    - Bei der Eingabe von anderen Elementen als Zahlen soll eine Fehlermeldung geworfen werden und der User aufgefordert, Zahlen einzugeben
     - Input: [D, $, &, 1, 7]
     - Fehlermeldung: "Als Eingabe dürfen nur Zahlen verwendet werden!"
        