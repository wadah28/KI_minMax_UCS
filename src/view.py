

from typing import List
from termcolor import colored


class GameView:
    """
    Verwaltet die Darstellung des Spiels (Grid-Ansicht).
    """

    def __create_print_array(self, grid_size: int) -> List[List[str]]:

        array = []
        for i in range(grid_size):
            row = []
            for j in range(grid_size):
                row.append("*" if (i % 2 == 0 and j % 2 == 0) else " ")
            array.append(row)
        return array

    def __update_print_array(self, graph: dict) -> None:

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

    def display(self, grid_size: int, graph: dict) -> None:
        self.print_array = self.__create_print_array(grid_size)
        self.__update_print_array(graph)
        for row in self.print_array:
            print("".join(row))
