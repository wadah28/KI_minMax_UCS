from asyncio import graph
from dataclasses import dataclass
import random
from operator import pos

from model import Graph, Edge


@dataclass
class Player:
    name: str
    color: str
    score: int = 0

    def get_move(self) -> tuple[int, int]:
        while True:
            print(f"Select Point for {self.name} from 1 to 9: ")
            point1 = input("Point1 := ")
            point2 = input("Point2 := ")

            if not point1.isdigit() or not point2.isdigit():
                print("Bitte nur ganze Zahlen 1-9")
                continue

            point1 = int(point1)
            point2 = int(point2)

            if not (1 <= point1 <= 9) or not (1 <= point2 <= 9):
                print("Bitte nur ganze Zahlen von 1 bis 9")
                continue

            if point1 == point2:
                print("Punkte müssen unterschiedlich sein")
                continue

            # Umrechnung auf 0–8
            point1 -= 1
            point2 -= 1

            return (point1, point2)



class RandomPlayer(Player):
    """
    NPC-Spieler, der zufällige gültige Spielzüge auswählt.
    """
    def __init__(self, name: str, color: str, graph):
        super().__init__(name, color)
        self.graph = graph

    def get_move(self) -> tuple[int, int]:
        """
        Wählt zufällig eine noch nicht belegte Kante.
        """
        edges = self.graph.get_edges()

        # Nur freie Kanten
        available_edges = [e for e in edges if not e.selected]

        edge = random.choice(available_edges)

        # Index der Punkte bestimmen
        p1 = self.graph.nodes.index(edge.point_one)
        p2 = self.graph.nodes.index(edge.point_two)

        print(f"{self.name} (NPC) wählt: {p1 + 1} - {p2 + 1}")

        return (p1, p2)
@dataclass(frozen=True)
class State:
    #Alle Kanten, die schon gesetzt wurden.
    #Beispiel: frozenset({(0, 1), (1, 2), (3, 4)})
    selected_edges: frozenset[tuple[int, int]]
    #Welche Farbe jede gesetzte Kante hat.
    edge_colors: tuple[tuple[tuple[int, int], str], ...]
    #Welche Box wem gehört.
    #Beispiel bei 4 Boxen:
    #("", "", "green", "red")
    box_owner: tuple[str, ...]
    #Wer jetzt dran ist.
    current_color: str

class Problem:
    def __init__(self, graph):
        self.graph = graph

    def actions(self, state: State) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        available_actions = []
        Alledges = self.graph.get_edges()
        for edge in Alledges:
            p1 = edge.point_one.position
            p2 = edge.point_two.position

            action = tuple(sorted((p1, p2)))

            if action not in state.selected_edges:
                available_actions.append(action)

        return available_actions #liste von freie punkten koordinaten
