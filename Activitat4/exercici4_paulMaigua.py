import numpy as np

def exercici4():

    # 1.Crear la matriu 3x4 amb nombres aleatoris entre 0 i 80
    arr = np.random.randint(81, size=(3,4))

    print("-> EXERCICI 4")
    print("-- CREEM LA MATRIU 3X4 AMB RANDINT ENTRE 0 I 80 --")
    print(arr)

    # 2.Modificar l'anterior matriu a una matriu 4x3
    # i l'última fila passa a ser l'última columna

    # Reshape que transforma l'anterior matriu a una 4x3
    arrAux = arr.reshape(4,3)

    # Agafem l'última fila de la matriu original
    # i fem reshape per convertir-la a columna
    arrAux2 = arr[-1,:].reshape(-1,1)

    # Fem append amb axis=1 per afegir la columna,
    # i substituir la tercera columna de la matriu 4x3
    arr = np.append(arrAux[:,:2],arrAux2, axis=1)

    print("-- LA MATRIU ANTERIOR ES TRANSFORMA A 4X3 AMB RESHAPE --")
    print("-- AFEGIM L'ÚLTIMA FILA COM A COLUMNA AMB APPEND --")
    print(arr)

    # 3.La nova matriu tindrà l'última columna amb el
    # mateixos nombres, iguals al primer nombre de
    # l'última columna en la matriu anterior
    arr[:,-1] = arr[0,-1]

    print("-- L'ÚLTIMA COLUMNA AMB TOTS ELS MATEIXOS NOMBRES IGUALS AL PRIMER --")
    print(arr)
    print("\n")