from dataclasses import dataclass


@dataclass
class Player():
    name: str
    color: str
#programm darf nicht absturzen sonder ein fehler exp geben
    def get_move(self) -> tuple[int, int]:
        while True:
            print(f"Select Point for {self.name} from 0 to 8: ")
            point1 = input("Point1 := ")
            point2 = input("Point2 := ")
            if not point1.isdigit() or not point2.isdigit():
                print("Bitte nur ganze Zahlen 0-8")
                continue
            point1 = int(point1)
            point2 = int(point2)
            if not (0 <= point1 <= 8) and (0 <= point2 <= 8):
                print("Bitte nur ganze Zahlen 0-8")
                continue
            if point1 == point2:
                print("Punkte muessen unterschiedlich sein")
                continue


            return (point1, point2)
