
from dataclasses import dataclass
from typing import Tuple, List, Dict


@dataclass(frozen=True, slots=True)
class Point:
    position: Tuple[int, int]
    name: str

    def __repr__(self) -> str:
        return f"{self.name}({self.position})"

    """ 
    alte Implementierung
    def __eq__(self, o):
        if self.position[0] == o.position[0] and self.position[1] == o.position[1]:
            return True
        return False
    """
    #ungerichtete Kanten Zwischen Punkt 0 und 1 ist dieselbe Linie wie zwischen 1 und 0.
    def __eq__(self, o):
        same_direction = self.point_one == o.point_one and self.point_two == o.point_two
        reverse_direction = self.point_one == o.point_two and self.point_two == o.point_one
        return same_direction or reverse_direction


@dataclass
class Edge:
    point_one: Point
    point_two: Point
    selected: bool = False
    color: str = ""

    @property
    def position(self) -> Tuple[int, int]:
        p1 = self.point_one.position
        p2 = self.point_two.position
        # Berechne die mittlere Position zwischen den Punkten
        if abs(p1[0] - p2[0]) <= 1:
            # x - Achse
            return (p1[0], min(p1[1], p2[1]) + 1)
        else:
            # Y - Achse
            return (min(p1[0], p2[0]) + 1, p1[1])

    @property
    def name(self) -> str:
        return f"{self.point_one.name} - {self.point_two.name}"

    def select(self, color: str) -> None:
        self.selected = True
        self.color = color

    def __eq__(self, o):
        print(o, self)
        if self.point_one == o.point_one and self.point_two == o.point_two:
            return True
        return False


class Graph:
    """
    Eine allgemeine Graph-Klasse, die Knoten und Kanten verwaltet.
    """

    def __init__(self) -> None:
        self.adjacency: Dict[Point, List[Edge]] = {}
        self.nodes: List[Point] = []

    def add_node(self, node: Point) -> None:
        self.adjacency.setdefault(node, [])
        self.nodes.append(node)

    def add_edge(self, a: Point, b: Point) -> None:
        edge_ab = Edge(a, b)
        edge_ba = Edge(b, a)
        self.adjacency[a].append(edge_ab)
        self.adjacency[b].append(edge_ba)

    def get_edges(self) -> List[Edge]:

        edge_list = []
        for ed_list in self.adjacency.values():
            for edge in ed_list:
                """
                       Damit jede echte Linie nur einmal zurückgegeben wird.
                """
                if not any(edge == existing for existing in edge_list):
                    edge_list.append(edge)
        return edge_list

    def get_edge(self, a: Point, b: Point):
        target = Edge(a, b)
        for edge in self.get_edges():
            if edge == target:
                return edge
        return None

    def __repr__(self) -> str:
        out = "Graph adjacency list:\n"
        for node, edges in self.adjacency.items():
            edge_names = [edge.name for edge in edges]
            out += f"{node.name}: {edge_names}\n"
        return out
