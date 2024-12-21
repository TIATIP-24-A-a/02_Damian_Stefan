# Quicksort-Algorithmus: Schritt-für-Schritt-Erklärung durch ChatGPT

## Python-Code für Quicksort:

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
```

## Ausführliche Erklärung des Codes:
1. Definition der Quicksort-Funktion:

````python
    def quicksort(arr):
````
- Wir definieren eine Funktion quicksort, die ein Array (Liste in Python) als Eingabe nimmt.
- Diese Funktion wird rekursiv aufgerufen, um das Array zu sortieren.

2. Basisfall: Prüfen, ob das Array zu klein ist, um weiter geteilt zu werden

````python
    if len(arr) <= 1:
        return arr
````

- Hier wird ein Basisfall definiert: Wenn die Länge des Arrays kleiner oder gleich 1 ist, wird es sofort zurückgegeben. 
- Warum?
  - Ein leeres Array ([]) oder ein Array mit nur einem Element ([x]) ist per Definition bereits sortiert. Es gibt nichts weiter zu tun.
  - Dieser Basisfall ist wichtig, um die Rekursion zu beenden. Ohne ihn würde die Funktion endlos weiterlaufen.

3. Auswahl des Pivot-Elements:

````python
    else:
        pivot = arr[len(arr) // 2]
````

- Wenn das Array mehr als ein Element enthält, wird ein Pivot-Element ausgewählt. 
- Hier verwenden wir das mittlere Element des Arrays:
  - arr[len(arr) // 2]: 
  - Wir berechnen den Index des mittleren Elements, indem wir die Länge des Arrays durch 2 teilen und den Ganzzahlergebniswert nehmen.
    - Beispiel: Für ein Array [10, 5, 2, 3, 8, 7, 1, 9] mit 8 Elementen ist das mittlere Element arr[8 // 2] = arr[4] = 8.

Das Pivot-Element dient als Bezugspunkt, um das Array in kleinere Teile zu zerlegen.
4. Das Array in drei Teile aufteilen:

Jetzt teilt der Algorithmus das Array in drei separate Listen:

````python
        left = [x for x in arr if x < pivot]
````

- Left: Wir erstellen eine Liste, die alle Elemente enthält, die kleiner als das Pivot-Element sind. Dies geschieht durch eine sogenannte List-Comprehension:
    - left = [x for x in arr if x < pivot] 
    - Bedeutet: Für jedes Element x im Array arr, füge es zur Liste left hinzu, wenn x kleiner als das Pivot-Element ist.
      - Beispiel: Wenn das Array [10, 5, 2, 3, 8, 7, 1, 9] ist und das Pivot 8, dann wird left zu [5, 2, 3, 7, 1], weil diese Elemente alle kleiner als 8 sind.

- Middle: Hier erstellen wir eine Liste, die alle Elemente enthält, die gleich dem Pivot-Element sind.
  - middle = [x for x in arr if x == pivot]
  - Da unser Pivot-Element 8 ist, wird middle zu [8].
  - Oft gibt es nur ein Pivot-Element, aber wenn es mehrfach im Array vorkommt, würden alle Vorkommen in middle gespeichert werden.

- Right: Schließlich erstellen wir eine Liste, die alle Elemente enthält, die größer als das Pivot-Element sind.
    - right = [x for x in arr if x > pivot]
    - Für das Array [10, 5, 2, 3, 8, 7, 1, 9] mit Pivot 8 wird right zu [10, 9], weil diese Elemente größer als 8 sind.

5. Rekursiver Aufruf von Quicksort:

````python
        return quicksort(left) + middle + quicksort(right)
````

Nun sortieren wir die left- und right-Teile rekursiv weiter, indem wir wieder die Funktion quicksort() auf sie anwenden. 
  - Das ist das Herzstück des Quicksort-Algorithmus.

Die rekursiven Aufrufe teilen das Array immer weiter in kleinere Teile auf, bis jedes Teil-Array nur noch ein oder kein Element enthält 
(was ja der Basisfall ist).

  
Sobald die Rekursion fertig ist, werden die drei Teile (left, middle und right) wieder zusammengesetzt:
- Die sortierten linken Elemente, 
- Dann das Pivot 
- Und schließlich die sortierten rechten Elemente.

Durch die Rekursion sind die Teillisten bereits sortiert, und das Zusammenfügen ergibt das sortierte Gesamtergebnis.

Beispiel-Schritt-für-Schritt mit dem Array [10, 5, 2, 3, 8, 7, 1, 9]:
- Erster Aufruf:

```python
    Array: [10, 5, 2, 3, 8, 7, 1, 9]
    Pivot: 8
    Left: [5, 2, 3, 7, 1]
    Middle: [8]
    Right: [10, 9]
    Rekursive Aufrufe für Left und Right.
````

- Rekursion auf der linken Seite ([5, 2, 3, 7, 1]):
````python
    Array: [5, 2, 3, 7, 1]
    Pivot: 3
    Left: [2, 1]
    Middle: [3]
    Right: [5, 7]
    Rekursion auf Left ([2, 1]) und Right ([5, 7]).
````

- Rekursion auf der linken Seite von Left ([2, 1]):

````python
    Array: [2, 1]
    Pivot: 1
    Left: [] (keine Elemente kleiner als 1)
    Middle: [1]
    Right: [2] (nur ein Element größer als 1)
    Da die Teil-Arrays nur noch ein oder null Elemente haben, kehren wir hier zurück:
        Sortiertes Ergebnis für diesen Schritt: [1, 2].
````

- Rekursion auf der rechten Seite von Left ([5, 7]):

````python
    Array: [5, 7]
    Pivot: 7
    Left: [5]
    Middle: [7]
    Right: []
    Da diese Arrays auch klein genug sind, kehren wir zurück:
        Sortiertes Ergebnis für diesen Schritt: [5, 7].
````

- Zusammensetzen der linken Seite:
    - Jetzt setzen wir die Ergebnisse für die linke Seite zusammen:
  
````python
        Left ([1, 2]), Middle ([3]), Right ([5, 7]).
        Ergebnis: [1, 2, 3, 5, 7].
````

- Zusammensetzen der rechten Seite:

````python
    Array: [10, 9]
    Pivot: 9
    Left: []
    Middle: [9]
    Right: [10]
    Da die Arrays klein sind, kehren wir zurück:
        Ergebnis: [9, 10].
````

- Endergebnis zusammensetzen:
    -Jetzt setzen wir das Endergebnis zusammen:

````python
        Left: [1, 2, 3, 5, 7]
        Middle: [8]
        Right: [9, 10]
        Ergebnis: [1, 2, 3, 5, 7, 8, 9, 10]
````

- Das Array ist nun vollständig sortiert!

## Fazit:

- Der Quicksort-Algorithmus teilt das Problem rekursiv in kleinere Teilprobleme auf (divide-and-conquer).
- Jedes Teil-Array wird durch ein Pivot-Element geteilt, und die Teile werden separat sortiert.
- Durch den rekursiven Ansatz und das schrittweise Zusammensetzen der Teilergebnisse wird das gesamte Array sortiert.