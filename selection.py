def selection(liste):
    n = len(liste)
    liste_sorted = []
    for i in range(n):
        m = min(liste)
        liste_sorted.append(m)
        liste.remove(m)
    return liste_sorted

liste = [64, 25, 12, 22, 11]
print(selection(liste))
    