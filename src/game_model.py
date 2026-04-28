from dataclasses import dataclass
import random

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

        self.possible_boxes = [
            (0, 1, 3, 4),
            (1, 2, 4, 5),
            (3, 4, 6, 7),
            (4, 5, 7, 8)
        ]

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

    def switch_player(self, current_color: str) -> str:
        if current_color == "red":
            return "green"
        if current_color == "green":
            return "red"
        raise ValueError(f"Unbekannte Farbe: {current_color}")

    def edge_action_by_node_index(self , x : int , y : int):
        p1 = self.graph.nodes[x].position
        p2 = self.graph.nodes[y].position
        return tuple(sorted((p1, p2)))

    def is_box_closed_by_state(self , box , selected_edges) -> bool:
        p1 ,p2,p3,p4 = box
        top = self.edge_action_by_node_index(p1, p2)
        bottom = self.edge_action_by_node_index(p1, p3)
        left = self.edge_action_by_node_index(p2, p4)
        right = self.edge_action_by_node_index(p3, p4)
        if (top in selected_edges
            and bottom in selected_edges
            and left in selected_edges
            and right in selected_edges):
            return True
        else : return False

    #Übergangsfunktion RESULT(s, a)
    def result(self , state : State , action : tuple[tuple[int, int], ...]) -> tuple[tuple[int, int], ...]:
        new_selected_edges = set(state.selected_edges)
        new_selected_edges.add(action) #die neue action als selected betrachten
        new_edge_colors =list(state.edge_colors) #bekommt die farben
        new_edge_colors.append((action , state.current_color)) #für diese action nimm diese color als tupek (  ... ,(action , current color) , ... )   )
        new_box_owner = list(state.box_owner)
        colsed_box= False  #zu prüfen ob ein box fertig ist

        for i in range(len(self.possible_boxes)):
            box = self.possible_boxes[i]
            if new_box_owner[i] != "" :
                continue
            if self.is_box_closed_by_state(box , new_selected_edges):
                new_box_owner[i] = state.current_color
                colsed_box = True

        if colsed_box:
            next_color = state.current_color
        else : next_color = self.switch_player(state.current_color)
        return State(
            selected_edges=frozenset(new_selected_edges),
            edge_colors=tuple(new_edge_colors),
            box_owner=tuple(new_box_owner),
            current_color=next_color
        )



