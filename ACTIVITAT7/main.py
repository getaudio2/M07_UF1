from create_table import create_table
from create import create_user
from read import read_all
from update import update_user
from delete import delete_user

def crud_menu():
    create_table()
    while True:
        print("\n--- Menu CRUD ---")
        print("1. Crear usuari")
        print("2. Visualitzar usuaris")
        print("3. Actualitzar usuari")
        print("4. Eliminar usuari")
        print("5. Sortir")

        opcio = input("Tria una opcio: ")

        if opcio == '1':
            create_user()
        elif opcio == '2':
            read_all()
        elif opcio == '3':
            update_user()
        elif opcio == '4':
            delete_user(input("Id-> "))
        elif opcio == '5':
            print("Sortint")
            break
crud_menu()