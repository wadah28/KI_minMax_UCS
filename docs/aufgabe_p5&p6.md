## Problembeschreibung
ein Problem besteht aus folgende Sachen:
- 1- Initial State
- 2- Set of Actions
- 3- Transition Model
- 4- Goal Test Function
- 5- Path Cost Function

## Das Spiel „Dots and Boxes“ als ein Problembeschreibung:

Ein Zustand beschreibt das aktuelle Spielfeld, also welche Kanten gesetzt sind und welche Farbe sie haben.

- Initial State : leeres Spielfeld bei dem keine Knate gesetzt ist. (Initialisierung des Spielfelds)
- Set of Actions : setze eine noch nciht gesetzte Kante und markiere es mit aktuelle Farbe
- Transition Model : die gewählte kante wird als gesetzt markiert , die farbe wird gespeichert
                     falls durch die Aktion ein oder mehrer Kätchen geschlossen wurden , werden diese die entsprechende farbe bekommen
- Goal Test Function : alle Kanten gesetzt ? gleich viel boxen in den jeweiligen farben?
- Path cost Function : Jede aktion kostet 1


## Spielzustand "Unentschieden" erreciehn

- Ein Agent übernimmt de Rolle beide spieler*innen, udn führt die Aktionen abwechselnd für die vershciedene Farben
- Agent = nimmt Zustand → gibt Aktion zurück
- Der Agent wählt in jedem Zustand eine gültige Aktion aus der Menge der möglichen Aktionen und wendet diese an, bis ein Zielzustand erreicht ist.
- Anzahl mögliche Aktionen : 
  - E = alle Kanten (graph_get_edges)
  - K = gesetzte Kanten
  - Anzahl möglcihe Kanten = E - K

## Beispielpfades
- S0: leeres Spielfeld
- a1: grüne kante setzen
- S1: eine grüne kante ist gesetzt
- a2: rote kante setzten
- S2: zwei kanten gesetzt

immer abwechselnd

- Sn: alle Kanten gesetzt & gleiche Anzahl Boxen für grün und rot -> unentschieden


## Baum vs Graph-Suche
derselbe Spielzustand kann über verscheidene Wege entstehen.
also mehrere wege -> gleicher Zustand.
und vom logik des Spieles kann ein Agent aknn nur Kanten setzten die noch nicht gesetzt wurden
Daher ist eine Graph-Suche sinnvoll, um doppelte Zustände zu vermeiden.
