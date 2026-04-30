# Changelog – Aufgabe P8: Minimax-Suche

## Added

### Klasse `MinMax`

Die Klasse `MinMax` wurde hinzugefügt, um einen kompetitiven Minimax-Spieler für „Dots and Boxes“ zu erstellen.

Der Minimax-Spieler berechnet den besten nächsten Zug aus Sicht einer bestimmten Farbe.  
Dabei wird die eigene Farbe als maximierender Spieler betrachtet und die gegnerische Farbe als minimierender Spieler.

---

### Methode `__init__(self, graph: Graph, max_color: str = "green")`

Initialisiert den Minimax-Spieler.

Die Methode speichert den übergebenen Spielgraphen, erstellt daraus ein `Problem`-Objekt und legt fest, welche Farbe der maximierende Spieler ist.

Außerdem wird automatisch bestimmt, welche Farbe der minimierende Gegenspieler hat.

Beispiel:

- Wenn `max_color == "green"` ist, dann ist `min_color == "red"`.
- Wenn `max_color == "red"` ist, dann ist `min_color == "green"`.

---

### Methode `argmax(self, state: State) -> Action | None`

Sucht die beste Aktion für den aktuellen Zustand.

Die Methode geht alle möglichen Aktionen des aktuellen Zustands durch.  
Für jede Aktion wird ein Folgezustand erzeugt und mit dem Minimax-Verfahren bewertet.

Die Aktion mit dem höchsten berechneten Wert wird als beste Aktion gespeichert und zurückgegeben.

Falls keine Aktion möglich ist, wird `None` zurückgegeben.

---

### Methode `MinMax_Decision(self, state: State) -> Action | None`

Startmethode für die Zugentscheidung des Minimax-Spielers.

Diese Methode ruft intern `argmax(state)` auf und gibt die beste gefundene Aktion zurück.

Sie dient als einfache Schnittstelle, um im Spiel den nächsten Zug des Minimax-Spielers zu bestimmen.

---

### Methode `value(self, state: State) -> int`

Berechnet den Minimax-Wert eines Zustands.

Die Methode prüft zuerst, ob der Zustand ein Endzustand ist.  
Falls ja, wird der Zustand mit `utilityValue(state)` bewertet.

Falls der Zustand kein Endzustand ist, wird anhand von `state.current_color` entschieden, ob der aktuelle Zustand eine Max-Ebene oder eine Min-Ebene im Spielbaum ist.

- Wenn `state.current_color == self.max_color` gilt, wird `Max_value(state)` aufgerufen.
- Andernfalls wird `Min_value(state)` aufgerufen.

Diese Methode ist wichtig, weil bei „Dots and Boxes“ ein Spieler nach dem Schließen einer Box erneut am Zug sein kann. Deshalb wird nicht einfach starr zwischen Max und Min gewechselt, sondern immer der aktuelle Spieler aus dem Zustand geprüft.

---

### Methode `terminal_test(self, state: State) -> bool`

Prüft, ob ein Zustand ein Endzustand ist.

Ein Zustand ist terminal, wenn das Spiel beendet ist, also keine weiteren Kanten mehr gesetzt werden können.

Die Methode verwendet dafür die bereits vorhandene Methode `problem.is_terminal(state)`.

---

### Methode `utilityValue(self, state: State) -> int`

Bewertet einen Endzustand aus Sicht des maximierenden Spielers.

Die Bewertung wird berechnet als:

```text
Anzahl eigener Boxen - Anzahl gegnerischer Boxen