from Objekte import *
def vorstellen (Objekt):
    return Objekt.info()

def getname(Objekt):
    return Objekt.name

def getalter(Objekt):
    print(Objekt.alter)
def getGeruescher(Objekt):
    print(Objekt.bellen())
objekteneList = [
    Hund("jak" , 2 ), Ente("koki" , 3) , Roboter("chatGPT" , 4),
    Hund("max" , 10) , Ente("Rosa", 5), Roboter("Deepseek", 2)
]
print("___Liste Info über for-loop___")
for objekt in objekteneList:
    print(objekt.bellen())
print()

print("___Liste nur Namen werden gefiltert und und einer namenlist gespeichert werden___")
namenlist = [ objekt.name for objekt in objekteneList ]
print("alle Namen:" , namenlist)
print()
print("___List Comprehension zum Filtern___")
jungObjekte = [objekt.name for objekt in objekteneList if objekt.alter <3]
print("Jungere (Objekte <3" , jungObjekte)
print()

print("___List Comprehension zum Erzeugen neuer Werte___")
alter_plus_eins = [ objekt.alter +1 for objekt in objekteneList ]
print("Alter in einem Jahr:" , alter_plus_eins)
print()

print("==Funktionen als Objekte==")
funktion1 = vorstellen
funktion2 = getname

print("erste Objekt vorstellen: " , funktion1(objekteneList[1]))
print("erste Objekt name:" , funktion2(objekteneList[3]))


