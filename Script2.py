
if __name__ == "__main__":
    arriba = 0
    abajo = 0
    valle = 0
    cad = input(">>  Ingrese la cadena que represente los pasos que dió \n     donde U es hacia arriba y D hacia abajo")
    for l in cad:
        if l == "U":
          
            arriba += 1
            if abajo-arriba == 0:
                print("Valle")
            elif arriba-abajo == 0:
                print("Montaña")
        elif l == "D":
            
            abajo += 1
            if abajo-arriba == 0:
                print("Valle")
            elif arriba-abajo == 0:
                print("Montaña")
        
       
