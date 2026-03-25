# Künstliche Intelligenz Praktikum





# Ablauf 

Willkommen zum KI-/Abtestat-Projekt!  
Jedes Team arbeitet in einem eigenen GitLab-Repository.  
Dieses Dokument erklärt, wie ihr Aufgaben bearbeitet, Merge Requests erstellt und Updates vom zentralen Repository übernehmt.

---

## Grundprinzip

- **`main` ist geschützt:**  
  Sie könnten dort nicht direkt pushen – nur Merge Requests.
- **Ihr arbeitet in eigenen Branches:**  
  z. B. `aufgabe_1`, `aufgabe_2`, `aufgabe_3`, …
- **Neue Aufgaben oder Bugfixes** kommen aus dem *Parent-Repository* („upstream“).

---

## Einrichtung

Nach dem ersten Klonen eures Team-Repos:
```bash
git clone https://git.fh-muenster.de/labki-lehre-studierende/sose26/<team-repo>.git
cd <team-repo>
```
<!-- TODO: Links Anpassen!(muss sein damit die Studis pullen können)-->

Fügt dann einmalig das zentrale Repository als Upstream hinzu:
```bash
git remote add upstream https://git.fh-muenster.de/labki-lehre-studierende/sose26/ki-praktikum
git fetch upstream
```

---

## Workflow pro Aufgabe 
<!-- (TODO: Branch pro Aufgabe oder pro Arbeitsblatt?)-->

###  Neuen Branch anlegen
```bash
git checkout -b aufgabe_1
```

###  Änderungen umsetzen
Bearbeitet die entsprechenden Dateien, fügt neue Skripte oder Ergebnisse hinzu.

### Committen
```bash
git add .
git commit -m "Lösung Aufgabe 1"
git push origin aufgabe_1
```

### Merge Request erstellen
Erstellt in GitLab einen **Merge Request** von `aufgabe_1` → `main`.

Dieser Merge Request entspricht eurem **Abtestat**.

---

##  Updates vom Parent-Repo holen
Wenn im zentralen Repo etwas geändert oder ergänzt wurde (z. B. neue Aufgaben, Bugfixes), könnt ihr diese Änderungen übernehmen:

```bash
git fetch upstream
git merge upstream/main
```

Wenn es Konflikte gibt, löst Sie bitte lokal und pusht danach wieder auf euren Branch.

---

## Tipps

- Nutzt sprechende Commit-Messages  
- Arbeitet als Team auf demselben Branch pro Aufgabe  
- Der Merge Request wird zur Bewertung genutzt  
- Ihr könnt mehrere Commits pushen, bevor ihr merged  

---

##  Beispielübersicht

| Aufgabe | Branch-Name | Merge-Request-Ziel |
|----------|--------------|--------------------|
| Aufgabenblatt 1 | `aufgabe_1` | `main` |
oder aufgabe??
| Aufgabenblatt 2 | `aufgabe_2` | `main` |
| Aufgabenblatt 3 | `aufgabe_3` | `main` |

---

##  Hilfe
Falls ihr das Upstream-Repo falsch gesetzt habt:
```bash
git remote remove upstream
git remote add upstream https://git.fh-muenster.de/ki-sandbox/<parent-repo>.git
```

Oder prüft eure Remotes:
```bash
git remote -v
```

---

## Mitwirken
Weiterentwicklungen zu diesem Projekt sind willkommen.
Bitte verwenden Sie Pull Requests für Änderungen.
