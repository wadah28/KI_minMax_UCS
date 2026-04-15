from dataclasses import dataclass


@dataclass
class Player():
    name: str
    color: str

    def get_move(self) -> tuple[int, int]:

        print(f"Select Point for {self.name} from 0 to 8: ")
        point1 = input("Point1 := ")
        point2 = input("Point2 := ")

        return (point1, point2)
