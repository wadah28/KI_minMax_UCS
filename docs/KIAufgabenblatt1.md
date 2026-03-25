# Aufgabenblatt 1

Praktikum zum Modul Künstliche Intelligenz

## Ziele

- Einarbeitung in python: In diesem Praktikum erarbeiten Sie Grundlagen und einige Besonderheiten der Programmiersprache python.

- Sie legen die Basis für die Erstellung von KI-Algorithmen im zweiten Praktikum. Dokumentieren Sie hierfür ihren Programmiercode und stellen Sie hierbei auch die verwendeten Konzepte entsprechend dar.

---

## Aufgabe P1 – Einarbeitung in die Programmiersprache python

Um sich mit den Grundlagen der Programmierung in Python vertraut zu machen, empfehlen wir folgende Ressourcen:

### Lernressourcen

**Dive Into Python 3:**

Eine umfassende Einführung in die Python-Sprache finden Sie unter  
*diveintopython3.net*. Diese Webseite bietet detaillierte Beschreibungen und praktische Beispiele, um die Eigenheiten und die Syntax von Python zu verstehen.

**Python Programmierung für Anfänger - Tutorial Video:**

Auf YouTube steht Ihnen ein umfassendes Video zur Verfügung, das grundlegende und fortgeschrittene Konzepte der Python-Programmierung abdeckt. Sehen Sie sich das Video hier an.

**Python Coding Conventions:**

Für Konventionen zur Benennung von Variablen, Funktionen und mehr, besuchen Sie *VisualGit Naming Conventions*.

---

Das Ziel des Praktikums ist das Verständnis der grundlegenden Programmierkonzepte. Die entwickelten Beispielprogramme sollten daher möglichst einfach gehalten werden, ohne auf die Anzahl der Codezeilen zu fokussieren.

### Aufgabenstellungen

#### Einfache Probleme:

- Bearbeiten Sie einfache Problemstellungen, wie z.B. die Berechnung der ersten n Fibonacci-Zahlen.
- Implementieren Sie eine objektorientierte Darstellung und Berechnung elementarer mathematischer Ausdrücke.

### Aspekte in Python

**Zahlen:**

- Erforschen Sie die Handhabung von verschiedenen Zahlentypen, wie ganze Zahlen und reelle Zahlen.

**Operatoren:**

- Arbeiten Sie mit verschiedenen Operatoren, z.B. für Addition, Subtraktion, Multiplikation und Division.
- Experimentieren Sie mit Klammerung und vereinfachten Rechnungen, indem Sie möglicherweise nur Addition und Subtraktion verwenden und die Operatorrangfolge ignorieren.

**Klassen:**

- Untersuchen Sie die Rolle und Struktur von Klassen in der objektorientierten Programmierung.

**Vererbung vs. Duck Typing:**

- Vergleichen Sie die Konzepte der Vererbung und des Duck Typing und ihre Anwendungen innerhalb von Python.

---

## Aufgabe P2 – Dots And Boxes

Repository-URL: <https://git.fh-muenster.de/labki/kisose24>

In dieser Aufgabe sollen Sie sich mit dem vorhandenen Quellcode auseinandersetzen und fehlende Spiellogik implementieren. Folgen Sie den unten stehenden Schritten, um die Implementierung abzuschließen.

### Aufgabenstellung

*Figure 1: DotsAndBoxes Spielverlauf*  
Quelle: <https://en.wikipedia.org/wiki/Dots_and_boxes>

#### 1. Repository-Initialisierung:

Klonen Sie das angegebene Repository und öffnen Sie das Projekt in Ihrer bevorzugten Entwicklungsumgebung.

#### 2. Quellcode-Analyse:

**Ziel:** Verstehen Sie die den Aufbau und die Funktionsweise des vorhandenen Codes.

**Vorgehen:** Durchsuchen Sie den Quellcode und identifizieren Sie zentrale Klassen und Methoden. Kommentieren Sie die relevanten Stellen, um die Funktionalität und ihre Bedeutung im Spielkontext zu beschreiben.

**Hilfestellung:**

- Kommentieren Sie jede Klasse mit ihrer Hauptaufgabe (z.B. Verwaltung der Spielsteuerung, Darstellung der Spiellogik, etc.).
- Kommentieren Sie komplexe oder zentrale Funktionen/Methoden.
- Erläutern Sie die Hauptdatenstrukturen (z.B. wie der Graph oder das Spielfeld modelliert ist).

#### 3. Implementierung der fehlenden Spiellogik:

**Ziel:** Vervollständigen Sie die Spiellogik, sodass der Spielverlauf aus Figure 1 abgebildet werden kann.

**Vorgehen:** Identifizieren Sie die Methoden, die noch unvollständig oder nicht implementiert sind. Ergänzen Sie logische Operationen, die zum vollständigen Spielablauf notwendig sind.

**Fehlende Logik:**

- Implementieren Sie die Methode zur Überprüfung, ob das Spiel beendet ist (z.B. durch einen Sieg oder Unentschieden).
- Ergänzen Sie die Kontrolle, ob nach Auswahl einer Kante ein Box gebildet wurde.
- Validieren Sie Benutzereingaben und stellen Sie sicher, dass nur gültige Aktionen ausgeführt werden können.

**Tipps:**

- Arbeiten Sie testgetrieben, indem Sie kleine Testfälle für Ihre Implementierung schreiben.
- Stellen Sie sicher, dass Ihre Ergänzungen robust gegenüber fehlerhaften Eingaben oder ungewöhnlichen Spielverläufen sind.

#### 4. Dokumentation und Abgabe:

**Ziel:** Stellen Sie sicher, dass Ihre Änderungen gut dokumentiert sind und von Dritten nachvollzogen werden können.

- Verfassen Sie eine kurze Übersicht zu Ihren Änderungen und Verbesserungen in einer README-Datei innerhalb des Repositorys.
- Führen Sie zusätzliche Kommentare im Code ein, wo nötig, um Ihre Implementierungslogik zu erläutern.

---

Hinweis: Diese Aufgabe dient der Vorbereitung des nächsten Aufgabenblatts, dort werden wir einen menschlichen Spieler durch einen KI-Agenten ersetzen. Berücksichtigen Sie diese Zielsetzung durch eine geeignete Code-Struktur.

---

## Aufgabe P3 – Zufallsbasierter Non-Player-Character

Entwickeln Sie im Kontext der vorherigen Aufgabe einen Non-Player-Character (NPC), der zufällige Spielzüge vornimmt und anstelle eines beliebigen menschlichen Spielers antreten kann.

Stellen Sie sicher, dass Sie problemlos zwischen einem menschlichen Mitspieler oder zufälligen NPC-Spieler wechseln können, sowohl für Spieler A als auch für Spieler B.
