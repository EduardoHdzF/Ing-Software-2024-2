
if __name__ == "__main__":

    print("--- Marcador de partido tennis ---")
    
    while True:        
        try:
            a = input(" Ingrese el nombre del jugador 1: ")
            #print("\n El jugador 1 es ", a)
            if a == "" or a == None:
                raise Exception   
            else:
                break     
        except Exception:
            print("   No puede dejar el nombre vacío, intente de nuevo. ")

    while True:
        try:
            b = input(" Ingrese el nombre del jugador 2: ")
            #print("\n El jugador 2 es ", b)
            if b == "" or b == None:
                raise Exception
            else:
                break       
        except Exception:
            print("   No puede dejar el nombre vacío, intente de nuevo. ")

    print("\n --- El mejor de 3 sets gana --- ")

    set = 0
    e = 0
    
    while set < 3:
        puntuacion1 = 0
        puntuacion2 = 0
        diferenciaJuegos = 0
        juego1 = 1
        juego2 = 1
        maximo = 0

        while True:
            #Si tenemos 40-0, gana si e otro wey llega a 50, solo se aplica adv cuando van 40-40
            if maximo >= 6 and diferenciaJuegos == 2:
                break
            while True:
                try:
                    print(f"\n ---------- \nLa puntuación actual es {a} {puntuacion1} - {puntuacion2} {b}\n ---------")
                    print("\nIngrese el número que corresponda al jugador que ganó el punto: ")
                    print(" El jugador 1 es ", a)
                    print("\n El jugador 2 es ", b)
                    c = int(input("-> "))
                    if c > 2 or c < 0:
                        raise Exception()
                    break                
                except Exception:
                    print("-----\n Escriba una opción correcta por favor\n -----")
          

            if c == 1:
                if puntuacion1 < 30:
                    puntuacion1 += 15
                else:
                    puntuacion1 += 10
                juego1 += 1
            else:
                if puntuacion2 < 30:
                    puntuacion2 += 15
                else:
                    puntuacion2 += 10
                juego2 += 1
            
            diferenciaJuegos = abs(juego1-juego2)
            print(juego1)
            print(juego2)
            print(diferenciaJuegos)
            maximo = max(juego1,juego2)
            """if puntuacion2 > 30:
                puntuacion2 = "adv" """

            #print(f"\n ---------- \nLa puntuación actual es {a} {puntuacion1} - {puntuacion2} {b} : ---------")
            
            #f += 1

        if maximo == juego1:
            print("\n-----\nEl set lo hace\n-----", a)
        else:
            print("\n-----\nEl set lo hace\n-----", b)
        print(f"\n ---------- \nLa puntuación quedó {a} {puntuacion1} - {puntuacion2} {b} : ---------")
        set += 1
        