from game_model import State, Problem, Player
from controller import GraphController, PlayerController, Game
from view import GameView
from MinMax import MinMax
import random


def mark_action_on_graph(graph, action, color):
    """
    Markiert die echte Edge im Graph,
    damit GameView sie anzeigen kann.
    """

    for edge in graph.get_edges():
        p1 = edge.point_one.position
        p2 = edge.point_two.position

        edge_action = tuple(sorted((p1, p2)))

        if edge_action == action:
            edge.selected = True
            edge.color = color
            return

    print("WARNUNG: Keine passende Edge gefunden:", action)


def box_owner_for_view(state):
    """
    Wandelt box_owner für die View um.

    ""      -> " "
    "red"   -> "R"
    "green" -> "G"
    """

    boxes = []

    for owner in state.box_owner:
        if owner == "red":
            boxes.append("R")
        elif owner == "green":
            boxes.append("G")
        else:
            boxes.append(" ")

    return boxes


def print_grid(view, graph_controller, state):
    """
    Gibt das aktuelle Grid aus.
    """

    print()
    view.display(
        grid_size=graph_controller.grid_size,
        graph=graph_controller.graph.adjacency,
        boxes=box_owner_for_view(state)
    )


if __name__ == "__main__":
    graph_controller = GraphController(grid_size=5)
    graph = graph_controller.graph

    problem = Problem(graph)
    view = GameView()

    human_player = Player("Human", "red")
    minmax_player = MinMax(graph, max_color="green")

    state = State(
        selected_edges=frozenset(),
        box_owner=("", "", "", ""),
        current_color="red"
    )

    path = []

    print("Startzustand:")
    print(state)
    print_grid(view, graph_controller, state)

    # ==================================================
    # Zwei Kanten am Anfang zufällig belegen,
    # damit MinMax weniger lange rechnen muss
    # ==================================================

    first_action = random.choice(problem.actions(state))

    print()
    print("=" * 40)
    print("Vorbelegter Zug 1")
    print("Farbe:", state.current_color)
    print("Action:", first_action)

    old_color = state.current_color
    path.append((first_action, old_color))

    state = problem.result(state, first_action)

    mark_action_on_graph(graph, first_action, old_color)

    print("Neuer State:")
    print(state)
    print("Boxen:", state.box_owner)
    print_grid(view, graph_controller, state)

    second_action = random.choice(problem.actions(state))

    print()
    print("=" * 40)
    print("Vorbelegter Zug 2")
    print("Farbe:", state.current_color)
    print("Action:", second_action)

    old_color = state.current_color
    path.append((second_action, old_color))

    state = problem.result(state, second_action)

    mark_action_on_graph(graph, second_action, old_color)

    print("Neuer State:")
    print(state)
    print("Boxen:", state.box_owner)
    print_grid(view, graph_controller, state)

    move_number = 3

    # ==================================================
    # Danach Human gegen MinMax
    # ==================================================

    while not problem.is_terminal(state):
        print()
        print("=" * 40)
        print(f"Zug {move_number}")
        print("Aktuelle Farbe:", state.current_color)

        if state.current_color == "red":
            print("Human ist dran.")

            while True:
                node_action = human_player.get_move()

                node1 = node_action[0]
                node2 = node_action[1]

                action = problem.edge_action_by_node_index(node1, node2)

                if action in problem.actions(state):
                    best_action = action
                    break

                print("Ungültiger Zug.")
                print("Diese Kante existiert nicht oder ist schon belegt.")
                print("Mögliche Actions:")
                print(problem.actions(state))

        else:
            print("MinMax ist dran.")
            best_action = minmax_player.MinMax_Decision(state)

        if best_action is None:
            print("Keine Aktion gefunden.")
            break

        print("Gewählte Action:", best_action)

        old_color = state.current_color

        path.append((best_action, old_color))

        state = problem.result(state, best_action)

        mark_action_on_graph(graph, best_action, old_color)

        print("Neuer State:")
        print(state)
        print("Boxen:", state.box_owner)
        print("Red:", state.box_owner.count("red"))
        print("Green:", state.box_owner.count("green"))

        print_grid(view, graph_controller, state)

        move_number += 1

    # ==================================================
    # Ergebnis
    # ==================================================

    print()
    print("=" * 40)
    print("Spiel fertig.")
    print("Endzustand:")
    print(state)

    red_score = state.box_owner.count("red")
    green_score = state.box_owner.count("green")

    print("Red:", red_score)
    print("Green:", green_score)

    if red_score > green_score:
        print("Gewinner: Human / red")
    elif green_score > red_score:
        print("Gewinner: MinMax / green")
    else:
        print("Unentschieden")

    print()
    print("=" * 40)
    print("Replay startet:")

    replay_graph_controller = GraphController(grid_size=5)

    player_controller = PlayerController(
        player1=Player("Human Red", "red"),
        player2=Player("MinMax Green", "green")
    )

    game = Game(
        graph_controller=replay_graph_controller,
        player_controller=player_controller,
        view=GameView()
    )

    game.replay_path(path)