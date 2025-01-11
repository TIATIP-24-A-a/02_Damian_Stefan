# Quicksort
Quicksort (englisch quick ‚schnell‘ und to sort ‚sortieren‘) ist ein schneller, rekursiver, nicht-stabiler Sortieralgorithmus,
der nach dem Prinzip Teile und herrsche arbeitet. Er wurde ca. 1960 von C. Antony R. Hoare in seiner Grundform entwickelt
und seitdem von vielen Forschern verbessert. Der Algorithmus hat den Vorteil, dass er über eine sehr kurze innere Schleife verfügt, was die Ausführungsgeschwindigkeit stark erhöht.

## Funktionsprinzip
Zunächst wird die zu sortierende Liste in zwei Teillisten („linke“ und „rechte“ Teilliste) getrennt. Dazu wählt Quicksort ein sogenanntes Pivotelement aus der Liste aus. 
Alle Elemente, die kleiner als das Pivotelement sind, kommen in die linke Teilliste, und alle, die größer sind, in die rechte Teilliste.
Für beide dieser Teillisten wird wiederum jeweils ein Pivotelement definiert und die Teilliste anhand diesem erneut sortiert. Dies wird solange wiederholt, bis die einzelnen
Teillisten eine Länge von 1 oder 0 aufweisen. Diese Selbstaufrufe werden als Rekursion bezeichnet.



Hier Schema Teilen einfügen




Im Anschluss werden die erstellten Teillisten wieder zusammengesetzt. Auf Grund deren Sortierung und der Pivotelemente erhält man nach Abschluss der Zusammenführung ein perfekt sortîertes Array. 


Hier Schema Zusammenfügen einfügen


## Anwendungsfälle
1. Sortierung von Daten
    Allgemeine Datensortierung: Quicksort wird oft in vielen Programmiersprachen und Bibliotheken verwendet, um Arrays oder Listen zu sortieren.


2. Datenbank-Operationen
    Indizierung und Abfragen: In Datenbanken wird Quicksort häufig für das Sortieren von Datensätzen verwendet, um schnelle Abfragen und Indizierungen zu ermöglichen.



3. Suchalgorithmen
    Schnelle Suche durch sortierte Daten: Quicksort wird oft verwendet, um Daten zu sortieren, die dann mit binärer Suche durchsucht werden können.
     Einmal sortierte Daten ermöglichen schnellere Suchoperationen (O(log n) statt O(n) in unsortierten Listen).

    
4. Datenverarbeitung in parallelen und verteilten Systemen
    Verteilte Systeme: In Systemen, die Daten über mehrere Maschinen verteilen, kann Quicksort verwendet werden, um parallel Daten auf verschiedenen Knoten zu sortieren und zu kombinieren.
    

## Vor-  und Nachteile


### Vorteile von Quicksort:

1. Effizienz (im Durchschnitt):
   - Durchschnittliche Zeitkomplexität O(n log n): Quicksort hat eine ausgezeichnete durchschnittliche Laufzeit, was ihn zu einem der effizientesten Sortieralgorithmen für allgemeine Zwecke macht.


2. Gute Performance bei großen Datensätzen:
   - Quicksort funktioniert besonders gut bei großen Datensätzen, weil die rekursive Teilung der Liste und das effiziente Vergleichen von Elementen dazu führen, dass der Algorithmus schnell konvergiert.


3. Einfache Implementierung:
   - Quicksort ist relativ einfach zu implementieren und benötigt wenig Code. In vielen Programmiersprachen wird er direkt oder als Grundlage für die eingebaute Sortierfunktion verwendet.


4. Flexibilität:
   - Der Pivot-Selektionsmechanismus kann angepasst werden, um verschiedene Varianten von Quicksort zu erzeugen, die auf unterschiedliche Datensätze besser abgestimmt sind. Zum Beispiel kann man den Pivot zufällig auswählen oder als Median der drei Elemente wählen, um die Effizienz zu verbessern.


5. Parallelisierbarkeit:
   - Quicksort lässt sich gut parallelisieren. In verteilten Systemen oder bei Multi-Core-Prozessoren kann jeder rekursive Aufruf auf verschiedenen Kernen ausgeführt werden, was zu einer weiteren Leistungssteigerung führt.

### Nachteile von Quicksort:

1. Schlechte Worst-Case-Leistung (O(n²)):
   - Im schlechtesten Fall hat Quicksort eine Zeitkomplexität von O(n²), was auftritt, wenn das Pivot immer das größte oder kleinste Element ist (z. B. bei bereits sortierten Daten oder umgekehrt sortierten Daten). Dies führt zu einer schlechten Performance, da die Liste nicht effizient geteilt wird.


2. Rekursive Natur (Stack Overflows):
   - Quicksort ist ein rekursiver Algorithmus, und bei sehr großen Eingabedaten oder schlecht gewählten Pivot-Elementen kann es zu Stack Overflow-Fehlern kommen, wenn die Rekursion zu tief wird.


3. Nicht stabil:
   - Quicksort ist nicht stabil, was bedeutet, dass gleichwertige Elemente nach der Sortierung ihre ursprüngliche Reihenfolge nicht beibehalten. In Szenarien, in denen die Reihenfolge gleichwertiger Elemente wichtig ist (z. B. bei der Sortierung von Objekten mit mehreren Kriterien), ist Quicksort weniger geeignet.


4. Unregelmäßige Performance bei schlecht strukturierten Daten:
   - Wenn die Daten sehr unregelmäßig oder bereits unsortiert sind, kann Quicksort durch die schlechte Wahl des Pivots ineffizient werden und im schlimmsten Fall eine O(n²)-Leistung erreichen. Dies kann durch den Einsatz spezieller Techniken zur Wahl des Pivots gemildert werden, aber es bleibt ein potenzielles Problem.


## Testing
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
  
In dieser Arbeit wurden die Testfälle mit folgendem Code abgehandelt:

```python


## Python Implementierung