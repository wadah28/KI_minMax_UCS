import Objekte

# Funktionen
def vorstellen(objekt):
    return objekt.info()

def getname(objekt):
    return objekt.name

def getalter(objekt):
    return objekt.alter

def getGeruescher(objekt):
    return objekt.bellen()


# Liste
objekteneList = [
    Objekte.Hund("jak", 2), Objekte.Ente("koki", 3), Objekte.Roboter("chatGPT", 4),
    Objekte.Hund("max", 10), Objekte.Ente("Rosa", 5), Objekte.Roboter("Deepseek", 2)
]

# 1. Duck Typing
print("== Duck Typing ==")
for objekt in objekteneList:
    print(objekt.bellen())
print()

# 2. Listen & List Comprehensions
print("== Listen & List Comprehension ==")
namenlist = [objekt.name for objekt in objekteneList]
print("Alle Namen:", namenlist)

jungObjekte = [objekt.name for objekt in objekteneList if objekt.alter < 3]
print("Junge Objekte:", jungObjekte)

alter_plus_eins = [objekt.alter + 1 for objekt in objekteneList]
print("Alter +1:", alter_plus_eins)
print()

# 3. Funktionen als Objekte
print("== Funktionen als Objekte ==")
funktion1 = vorstellen
funktion2 = getname

print("Vorstellen:", funktion1(objekteneList[1]))
print("Name:", funktion2(objekteneList[3]))
print()

# 4. Lambda
print("== Lambda ==")
sortiert = sorted(objekteneList, key=lambda obj: obj.alter)
print("Sortiert nach Alter:", [o.name for o in sortiert])