def solve(path):
    valleys, level = 0, 0
    enteredValley = False
    for step in path:
        if step == 'U':
            level += 1
        else:
            level -= 1

if __name__ == "__main__":
    arriba = 0
    abajo = 0
    valle = 0
    cad = input(">>  Ingrese la cadena que represente los pasos que dió \n     donde U es hacia arriba y D hacia abajo")
    for l in cad:
        if l == "U":
            print("cagón")
            arriba += 1
            if abajo-arriba == 0:
                print("Valle")
            elif arriba-abajo == 0:
                print("Montaña")
        elif l == "D":
            print("Mion")
            abajo += 1
            if abajo-arriba == 0:
                print("Valle")
            elif arriba-abajo == 0:
                print("Montaña")
        
       
