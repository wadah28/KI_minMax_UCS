import random

from controller import GraphController, PlayerController, Game
from game_model import Player, State, Problem, UniformCostSearch
from view import GameView


def test_ucs_with_preselected_edge():
    """
    Test:
    Im Graph ist schon eine zufällige Kante von einem zufälligen Spieler belegt.
    Dieser Zustand wird als Initial State an Uniform-Cost-Search übergeben.
    """

    graph_controller = GraphController(grid_size=5)
    uniform_cost_search = UniformCostSearch()
    problem = Problem(graph_controller.graph)

    players = ["red", "green"]
    preselected_color = random.choice(players)
    preselected_action = random.choice(problem.all_actions)

    preselected_node1, preselected_node2 = PlayerController.action_to_node_numbers(graph_controller.graph,
                                                                                   preselected_action)
    graph_controller.select_edge_point_number(preselected_node1,
                                              preselected_node2,
                                              preselected_color)

    empty_state = State(selected_edges=frozenset(),
                        box_owner=("", "", "", ""),
                        current_color=preselected_color)

    # Dadurch berechnet Problem selbst, wer danach dran ist.
    initial_state = problem.result(empty_state,preselected_action)

    print("Startzustand mit bereits belegter Kante:")
    print(
        f"{preselected_color} hat schon gesetzt: "
        f"Node {preselected_node1} - Node {preselected_node2} | "
        f"Koordinaten: {preselected_action}"
    )
    print(f"Danach ist {initial_state.current_color} dran.")
    rest_path = uniform_cost_search.search(problem, initial_state)

    if rest_path is None:
        print("Keine Lösung ab diesem Startzustand gefunden.")
        return

    player_controller = PlayerController(
        player1=Player("UCS Red", "red"),
        player2=Player("UCS Green", "green")
    )

    game = Game(
        graph_controller=graph_controller,
        player_controller=player_controller,
        view=GameView()
    )
    game.replay_path(rest_path)

if __name__ == "__main__":
    test_ucs_with_preselected_edge()