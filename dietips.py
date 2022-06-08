from usuario import cargarDatos
import os

def menu():
    os.system('cls')
    print('Bienvenido a Dietips')
    user = cargarDatos()
    os.system('cls')
    print(f'\nSegun el Indice de Masa Muscular su estado actual de {user.imc}')
    opcion = int(input('\n¿Desea obtener una sugerencia Nutricional?\n1_Si\n2_No\nSelecione una opcion: '))

    if(opcion == 1):
        os.system('cls')
        calorias = user.calcularConsumoCalorico(user.tasaMB, user.pesoInicial,user.pesoObjetivo,user.tiempo)
        user.caloriasXComida(user.pesoObjetivo,user.tiempo,round(calorias))
        opcionNueva = int(input('\n¿Desea obtener una sugerencia de Entrenamiento?\n1_Si\n2_No\nSelecione una opcion: '))
        if(opcionNueva == 1):
            user.recomendacionEjercicios(user.pesoObjetivo,user.tiempo,round(calorias),user.pesoInicial)
        else:
            print('Fin del programa')
            exit
    else:
        print('Fin del programa')
        exit
        

menu()