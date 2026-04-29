from dataclasses import dataclass
import random
from dataclasses import dataclass, field
import heapq
import itertools
from model import Graph, Edge

Position = tuple[int, int]
Action = tuple[Position, Position]

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
    selected_edges: frozenset[Action]
    box_owner: tuple[str, ...]
    current_color: str

@dataclass(frozen=True)
class SearchNode:
    state: State
    parent: "SearchNode | None"
    action: Action | None
    path_cost: int


class Problem:
    def __init__(self, graph):
        self.graph = graph

        self.possible_boxes = [
            (0, 1, 3, 4),
            (1, 2, 4, 5),
            (3, 4, 6, 7),
            (4, 5, 7, 8)
        ]

        self.all_actions = []

        for edge in self.graph.get_edges(): #damit nicht jedes mal get_edges aufgerufen wird
            p1 = edge.point_one.position
            p2 = edge.point_two.position
            action = tuple(sorted((p1, p2)))
            self.all_actions.append(action)

    def actions(self, state: State) -> list[Action]:
        available_actions = []
        for action in self.all_actions: #all_action die liste alle möglichen edges
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
        left = self.edge_action_by_node_index(p1, p3)
        right = self.edge_action_by_node_index(p2, p4)
        bottom = self.edge_action_by_node_index(p3, p4)
        if (top in selected_edges
            and bottom in selected_edges
            and left in selected_edges
            and right in selected_edges):
            return True
        else : return False

    #Übergangsfunktion RESULT(s, a) => neue Zustand
    def result(self, state: State, action: Action) -> State:
        new_selected_edges = set(state.selected_edges)
        new_selected_edges.add(action) #die neue action als selected betrachten

        #new_edge_colors =list(state.edge_colors) #bekommt die farben
        #new_edge_colors.append((action , state.current_color)) #für diese action nimm diese color als tupek (  ... ,(action , current color) , ... )   )

        new_box_owner = list(state.box_owner)
        closed_box = False

        for i in range(len(self.possible_boxes)):
            box = self.possible_boxes[i]
            if new_box_owner[i] != "" :
                continue
            if self.is_box_closed_by_state(box , new_selected_edges):
                new_box_owner[i] = state.current_color
                closed_box = True

        if closed_box:
            next_color = state.current_color
        else : next_color = self.switch_player(state.current_color)
        return State(
            selected_edges=frozenset(new_selected_edges),
            box_owner=tuple(new_box_owner),
            current_color=next_color
        )

    def is_terminal(self, state: State) -> bool:
        return len(self.actions(state)) == 0 #ob das Ende erreictt wurde
    def is_draw(self , state : State) -> bool:
        player1 = state.box_owner.count("green")
        player2 = state.box_owner.count("red") #wird gezahlt zb. ("red","green","red","green")
        if player1 == player2: #dann ist hier 2 == 2 ist true
            return True
        else: return False

    def goal_test(self ,state : State) -> bool:
        return self.is_terminal(state)   and self.is_draw(state)
    def step_cost(self, state: State, action: Action, next_state: State) -> int:
        return 1




class UniformCostSearch:

    def search(self,problem: Problem,initial_state: State ) -> list[tuple[Action, str]] | None:

        start_node = SearchNode(
            state=initial_state,
            parent=None,
            action=None,
            path_cost=0
        )

        counter = itertools.count()
        frontier = []

        heapq.heappush(
            frontier,
            (start_node.path_cost, next(counter), start_node)
        )

        frontier_states = {
            initial_state: start_node.path_cost
        }

        explored = set()

        while True:
            if not frontier:
                return None

            current_cost, _, node = heapq.heappop(frontier)

            if node.state in explored:
                continue

            if problem.goal_test(node.state):
                return self.solution(node)

            explored.add(node.state)

            for action in problem.actions(node.state):
                child_state = problem.result(node.state, action)

                new_cost = node.path_cost + problem.step_cost(
                    node.state,
                    action,
                    child_state
                )

                child_node = SearchNode(
                    state=child_state,
                    parent=node,
                    action=action,
                    path_cost=new_cost
                )

                old_cost = frontier_states.get(child_state)

                if child_state not in explored and old_cost is None:
                    frontier_states[child_state] = child_node.path_cost

                    heapq.heappush(
                        frontier,
                        (child_node.path_cost, next(counter), child_node)
                    )

                elif child_state not in explored and new_cost < old_cost:
                    frontier_states[child_state] = child_node.path_cost

                    heapq.heappush(
                        frontier,
                        (child_node.path_cost, next(counter), child_node)
                    )

    def solution(self, node: SearchNode) -> list[tuple[Action, str]]:
        path = []

        while node.parent is not None:
            color = node.parent.state.current_color
            path.append((node.action, color))
            node = node.parent

        path.reverse()
        return path