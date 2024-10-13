import numpy as np

def exercici1():

    # Crear una matriu amb valors ascendents en la
    # diagonal de 0 a 49
    arr = np.arange(50) # Creem un array amb els valors de 0 a 49
    arr2 = np.diag(arr) # Fem un nou array on la diagonal té els valors de 0 a 49, fem servir el mètode np.diag()

    np.save('exercici1.npy', arr2) # Fem servir save() per guardar l'array en format binari

    arr3 = np.load('exercici1.npy')

    print("-> EXERCICI 1")
    print("-- MATRIU AMB VALORS DE 0 A 49 EN DIAGONAL --")
    print(arr3)
    print("-- NOMBRE DE DIMENSIONS DE LA MATRIU --")
    print(arr3.ndim)
    print("-- TAMANY DE LA MATRIU --")
    print(arr3.shape)
    print("-- NOMBRE TOTAL D'ELEMENTS --")
    print(arr3.size)
    print("-- TIPUS D'ELEMENTS INTERNS --")
    print(arr3.dtype)
    print("\n")