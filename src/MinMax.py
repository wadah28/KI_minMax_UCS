from game_model import State, Action, Problem, Player
from model import Graph
from controller import GraphController ,PlayerController, Game
from view import GameView
import random

class MinMax:
    def __init__(self, graph: Graph, max_color: str = "green"):
        self.graph = graph
        self.problem = Problem(graph)
        self.max_color = max_color

        if max_color == "green":
            self.min_color = "red"
        else:
            self.min_color = "green"

    def argmax(self, state: State) -> Action | None:
        best_action = None
        best_value = float("-inf")

        for action in self.problem.actions(state):
            state1 = self.problem.result(state, action)
            value = self.value(state1)
            print(f"Action {action} -> Wert {value}")
            if value > best_value:
                best_value = value
                best_action = action

        return best_action

    def MinMax_Decision(self , state : State) -> Action | None:
        return self.argmax(state)

    def value(self, state: State) -> int:
        if self.terminal_test(state):
            return self.utilityValue(state)

        if state.current_color == self.max_color:
            return self.Max_value(state)
        else:
            return self.Min_value(state)

    def terminal_test(self,state : State) -> bool:
        if self.problem.is_terminal(state):
            return True
        return False

    def utilityValue(self , state : State) -> int:
        value = state.box_owner.count(self.max_color) - state.box_owner.count(self.min_color)
        return value

    def Max_value(self,state : State) -> int:
        if self.terminal_test(state):
            return self.utilityValue(state)
        _V = float("-inf")
        for action in  self.problem.actions(state):
            _V = max(_V, self.value(self.problem.result(state, action)))
        return _V



    def Min_value(self , state : State) -> int:
        if self.terminal_test(state):
            return self.utilityValue(state)
        v = float("inf")
        for action in self.problem.actions(state):
            state2 =self.problem.result(state, action)
            v = min(v, self.value(state2))
        return v
from controller import GraphController


if __name__ == "__main__":
    graph_controller = GraphController(grid_size=5)
    graph = graph_controller.graph

    problem = Problem(graph)

    red_minmax = MinMax(graph, max_color="red")
    green_minmax = MinMax(graph, max_color="green")

    # Startzustand: Red beginnt
    state = State(
        selected_edges=frozenset(),
        box_owner=("", "", "", ""),
        current_color="green"
    )

    path = []

    print("Startzustand:")
    print(state)

    # =========================
    # Zufälliger Zug für RED
    # =========================
    red_random_action = random.choice(problem.actions(state))
    path.append((red_random_action, state.current_color))

    print("\nRandom-Zug 1:")
    print("Farbe:", state.current_color)
    print("Action:", red_random_action)

    state = problem.result(state, red_random_action)

    # ===========================
    # Zufälliger Zug für GREEN
    # ===========================
    green_random_action = random.choice(problem.actions(state))
    path.append((green_random_action, state.current_color))

    print("\nRandom-Zug 2:")
    print("Farbe:", state.current_color)
    print("Action:", green_random_action)

    state = problem.result(state, green_random_action)

    print("\nZustand nach 2 Random-Zügen:")
    print(state)

    # ===========================
    # Danach Minimax gegen Minimax
    # ===========================
    move_number = 3

    while not problem.is_terminal(state):
        print()
        print("=" * 40)
        print(f"Minimax-Zug {move_number}")
        print("Aktuelle Farbe:", state.current_color)

        if state.current_color == "red":
            best_action = red_minmax.MinMax_Decision(state)
        else:
            best_action = green_minmax.MinMax_Decision(state)

        if best_action is None:
            print("Minimax konnte keine Aktion finden.")
            break

        print("Gewählte Action:", best_action)

        path.append((best_action, state.current_color))
        state = problem.result(state, best_action)

        print("Neuer State:")
        print(state)

        move_number += 1

    print()
    print("=" * 40)
    print("Spiel fertig berechnet.")
    print("Endzustand:")
    print(state)
    print("Boxen:", state.box_owner)
    print("Red:", state.box_owner.count("red"))
    print("Green:", state.box_owner.count("green"))

    if state.box_owner.count("red") > state.box_owner.count("green"):
        print("Gewinner: red")
    elif state.box_owner.count("green") > state.box_owner.count("red"):
        print("Gewinner: green")
    else:
        print("Unentschieden")

    # ===========================
    # Replay mit Farben anzeigen
    # ===========================
    print()
    print("=" * 40)
    print("Replay startet:")

    replay_graph_controller = GraphController(grid_size=5)

    player_controller = PlayerController(
        player1=Player("MinMax Red", "red"),
        player2=Player("MinMax Green", "green")
    )

    game = Game(
        graph_controller=replay_graph_controller,
        player_controller=player_controller,
        view=GameView()
    )

    game.replay_path(path)