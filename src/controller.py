from termcolor import colored

from game_model import Player, RandomPlayer
from model import Graph, Point, Edge
from view import GameView


class GraphController:
    """
    Spezifische Logik für ein Spiel, das ein 5x5-Grid verwendet.
    Nutzt intern einen allgemeinen Graphen (GameGraph).
    Angenommen, bei einem 5x5-Raster (UI-Raster mit Knoten und Kanten) ergeben sich 9 Knoten, die folgendermaßen
    angeordnet sind (zeilenweise):
    0   1   2
    3   4   5
    6   7   8
   """

    def __init__(self, grid_size: int = 5) -> None:
        self.graph = Graph()
        self.grid_size = grid_size
        self.boxes = []
        self.last_seleced_edge = None
        self.setup_grid()
        self.completed_boxes = set()


    def setup_grid(self) -> None:

        point_index = 0
        # Knoten an den "geraden" Positionen hinzufügen.
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if i % 2 == 0 and j % 2 == 0:
                    node = Point((i, j), f"P{point_index}")
                    self.graph.add_node(node)
                    point_index += 1
        self.add_edges()



    def add_edges(self) -> None:
        """     Hier wird fest codiert, welche Nachbarpunkte verbunden sind.
                Das entspricht den möglichen Linien, die Spieler auswählen dürfen.
                Diese Methode funktioniert aktuell nur für genau 9 Punkte,

        """
        points = self.graph.nodes
        if len(points) == 9:
            edges = [
                Edge(points[0], points[1]), Edge(points[0], points[3]),
                Edge(points[1], points[2]), Edge(points[1], points[4]),
                Edge(points[2], points[5]), Edge(points[3], points[4]),
                Edge(points[3], points[6]), Edge(points[4], points[5]),
                Edge(points[4], points[7]), Edge(points[5], points[8]),
                Edge(points[6], points[7]), Edge(points[7], points[8])
            ]

            for edge in edges:
                self.graph.add_edge(edge.point_one, edge.point_two)

    def __select_edge(self, a: Point, b: Point, color: str) -> bool:
        """
        Markiert eine Kante zwischen zwei Punkten als gewählt
        Ein Spieler wählt im Spiel zwei Punktnummern.
        Diese Methode sucht die passende Kante und markiert sie als besetzt.
        Rückgabe:
        - True, wenn die Kante existiert und markiert wurde
        - False, wenn keine passende Kante gefunden wurde
        Problem im aktuellen Code:
        Es wird nicht geprüft, ob die Kante schon ausgewählt wurde.
        Dadurch könnte dieselbe Kante mehrfach gewählt werden.
        #TODO check if edge already selected
        """
        edge = Edge(a, b)
        edges = self.graph.get_edges()

        for e in edges:
            if edge == e:
                if e.selected : #extra check if one edge already selected
                    print("Fehler: Diese Kante wurde bereits gewählt.")
                    return False
                e.select(color)

                return True
        print("Fehler diese Kante/edge ex. nicht ")
        return False

    def select_edge_point_number(self, a: int, b: int, color: str):
        """
        Der Spieler gibt z.B. '0' und '1' ein.
        Daraus werden self.graph.nodes[0] und self.graph.nodes[1].
        """
        if not(0<= a < len(self.graph.nodes) and 0<= b < len(self.graph.nodes)):
            print("Fehler punktnummer muss zwischen 0 und 8 sein ")
            return False
        if a == b:
            print("Fehler es ex. keine Kante ein Node mit sich selbst!")
            return False

        return self.__select_edge(self.graph.nodes[a],
                                  self.graph.nodes[b],
                                  color)

    def check_box(self):
        """
        Prüft, ob durch die letzte Kante ein Kästchen geschlossen wurde.
        """
        possible_boxes = [
            (0, 1, 3, 4),
            (1, 2, 4, 5),
            (3, 4, 6, 7),
            (4, 5, 7, 8)
        ]
        new_boxes = 0

        for i, box in enumerate(possible_boxes):
            if box in self.completed_boxes:
                continue

            p1, p2, p3, p4 = box
            top = self.graph.get_edge(self.graph.nodes[p1], self.graph.nodes[p2])
            left = self.graph.get_edge(self.graph.nodes[p1], self.graph.nodes[p3])
            right = self.graph.get_edge(self.graph.nodes[p2], self.graph.nodes[p4])
            bottom = self.graph.get_edge(self.graph.nodes[p3], self.graph.nodes[p4])

            if all(edge is not None and edge.selected for edge in (top, left, right, bottom)):
                self.completed_boxes.add(box)
                self.boxes.append(i)
                new_boxes += 1

        return new_boxes

    def is_game_over(self) -> bool: #new
        return all(edge.selected for edge in self.graph.get_edges())

    def __repr__(self) -> str:
        """wie tostring in Java"""
        return repr(self.graph)

class PlayerController:
    """Verwaltet die Spielerreihenfolge und den aktuellen Spieler."""
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.other_player = player2

    def get_player_edge(self):
        edge = self.current_player.get_move()
        return edge

    def switch_player(self):
        tmp = self.current_player
        self.current_player = self.other_player
        self.other_player = tmp

    def get_color(self):
        return self.current_player.color

    def add_score(self, points: int):
        self.current_player.score += points


class Game:
    """
    Zentrale Spielsteuerung.
    Spielkontext:
    Diese Klasse verbindet:
    - GraphController = Spiellogik / Spielfeld
    - PlayerController = Spielerverwaltung
    - GameView = Darstellung

    Sie enthält die Hauptspielschleife.
    """
    def __init__(self, graph_controller: GraphController,
                 player_controller: PlayerController,
                 view: GameView):

        self.graph_controller = graph_controller
        self.player_controller = player_controller
        self.view = view
        self.boxes = [" "] * 4

    def start(self):
        self.view.display(
            self.graph_controller.grid_size,
            self.graph_controller.graph.adjacency,
            self.boxes
        )


        while not self.graph_controller.is_game_over():
            edge = self.player_controller.get_player_edge()

            if self.graph_controller.select_edge_point_number(
                    edge[0], edge[1],
                    self.player_controller.get_color()):

                boxes_completed = self.graph_controller.check_box()
                for box_index in self.graph_controller.boxes:
                    if self.boxes[box_index] == " ":
                        self.boxes[box_index] = colored("X", self.player_controller.current_player.color)


                if boxes_completed > 0:
                    self.player_controller.add_score(boxes_completed)
                    print(
                        f"Box geschlossen! {self.player_controller.current_player.name} bekommt {boxes_completed} Punkt(e).")
                    print(f"{self.player_controller.current_player.name} ist nochmal dran.")
                else:
                    self.player_controller.switch_player()

                self.view.display(
                    self.graph_controller.grid_size,
                    self.graph_controller.graph.adjacency,
                    self.boxes
                )


        p1 = self.player_controller.player1
        p2 = self.player_controller.player2

        print("Spiel beendet.")
        print(f"{p1.name}: {p1.score}")
        print(f"{p2.name}: {p2.score}")

        if p1.score > p2.score:
            print(f"Sieger: {p1.name}")
        elif p2.score > p1.score:
            print(f"Sieger: {p2.name}")
        else:
            print("Unentschieden")


if __name__ == "__main__":

    graph_controller = GraphController(grid_size=5)

    player_controller = PlayerController(
        player1=Player("Player 1", "red"),
        player2=RandomPlayer("NPC", "green", graph_controller.graph)
    )

    game = Game(
        graph_controller=graph_controller,
        player_controller=player_controller,
        view=GameView()
    )

    game.start()
