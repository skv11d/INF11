liste = [1, "a", 0, 0, "a", 1, 1, "a", 0, 1, 0, "a"]

element = input("Geben Sie ein Element ein: ")
zaehler = -1
posListe = []

if element.isdigit():
    element = int(element)

for i in range(len(liste)):
    zaehler += 1
    if liste[i] == element:
        posListe += [zaehler]

print("Das Element", element, "kommt zum ersten Mal an Position", posListe[0], "vor und zum letzten Mal an Position", posListe[len(posListe) - 1])
    
