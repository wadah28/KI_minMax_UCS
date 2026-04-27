

from typing import List
from termcolor import colored


class GameView:
    """
    Darstellung des Spiels im Terminal.

    Aufgabe:
    - Erstellt das Grid mit Punkten (*)
    - Zeichnet ausgewählte Kanten
    - Färbt Kanten je nach Spieler

    Gehört zur View (Anzeige), nicht zur Spiellogik.
    """

    def __create_print_array(self, grid_size: int) -> List[List[str]]:
        """
    Erstellt ein leeres Spielfeld (2D-Array).

    Punkte (*) liegen an geraden Positionen,
    Zwischenräume sind für Kanten reserviert.
    """
        array = []
        for i in range(grid_size):
            row = []
            for j in range(grid_size):
                row.append("*" if (i % 2 == 0 and j % 2 == 0) else " ")
            array.append(row)
        return array

    def __update_print_array(self, graph: dict) -> None:
        """
   Zeichnet ausgewählte Kanten ins Grid.

   - nutzt Graph als Adjazenzliste
   - zeigt horizontale und vertikale Kanten
   - färbt je nach Spieler
   """
        for point, edges in graph.items():
            for edge in edges:
                if edge.selected:
                    pos = edge.position
                    i, j = int(pos[0]), int(pos[1])
                    # Unterscheide horizontal und vertikal.
                    if edge.point_one.position[0] == edge.point_two.position[0]:
                        self.print_array[i][j] = colored(u'\u2500', edge.color)
                    else:
                        self.print_array[i][j] = colored("|", edge.color)

    def display(self, grid_size: int, graph: dict, boxes: list) -> None:
        """
        Zeigt das Spielfeld an:
        - Grid erstellen
        - Kanten einzeichnen
        - Ausgabe im Terminal
        """
        self.print_array = self.__create_print_array(grid_size)
        self.__update_print_array(graph)
        box_positions = [
            (1, 1),  # Box 0
            (1, 3),  # Box 1
            (3, 1),  # Box 2
            (3, 3)   # Box 3
        ]

        for i, (r, c) in enumerate(box_positions):
            if boxes[i] != " ":
                self.print_array[r][c] = boxes[i]

        # Ausgabe
        for row in self.print_array:
            print("".join(row))