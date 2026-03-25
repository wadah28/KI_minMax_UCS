# Aufgabenblatt 1

Praktikum zum Modul Künstliche Intelligenz

## Ziele

- Einarbeitung in python: In diesem Praktikum erarbeiten Sie Grundlagen und einige Besonderheiten der Programmiersprache python.

- Sie legen die Basis für die Erstellung von KI-Algorithmen im zweiten Praktikum. Dokumentieren Sie hierfür ihren Programmiercode und stellen Sie hierbei auch die verwendeten Konzepte entsprechend dar.

---

TODO:: Testaufgabe für Gitlab Abtestat struktur.
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
