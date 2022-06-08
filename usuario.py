import os

class Usuario:
    def __init__(self,sexo,edad,estatura,pesoInicial,pesoObjetivo,tiempo):
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.pesoInicial =pesoInicial
        self.pesoObjetivo =pesoObjetivo
        self.tiempo = tiempo
        self.comidasDiarias = 0
        self.tasaMB = self.TMB(sexo,pesoInicial,estatura,edad)
        self.imc = self.IMC(pesoInicial,estatura)

    #Tasa Metabolica Basal TMB

    def TMB(self,sexo,pesoInicial,altura,edad):
        hombre = 66 + (13.7 * pesoInicial) + (5 * altura) - (6.75 * edad)
        mujer = 655 + (9.6 * pesoInicial) + (1.8 * altura) - (4.7 * edad)

        if(sexo == 'Masculino' or sexo == 'masculino'):
            return round(hombre)
        else:
            return round(mujer)
    
    #Indice de Masa Corporal IMC

    def IMC (self,peso,estatura):
        estatura = estatura / 100
        estatura = estatura * estatura
        imc = peso/estatura

        if(imc < 18.5):
            return 'Peso es inferior al normal'
        if(imc >= 18.5 and imc <= 24.9):
            return 'Peso es Normal'
        if(imc >= 25 and imc <=29.9):
            return 'Peso es superior al normal'
        if(imc >= 30):
            return 'Peso es Obesidad'
    

    #Calculo para obtener la cantidad de Kcal x dia que necesita la persona

    def calcularConsumoCalorico(self,TMB,pesoActual,pesoObjetivo,tiempo):
        nivelActividadFisica = int(input('¿Que tan frecuenta realiza actividad fisica?\n1_Ninguna vez\n2_Una o dos veces por semana\n3_Tres a cinco veces por semana\n4_Seis a Siete veces a la semana\n5_Toda la semana, dos veces a la semana\nSelecione una Opcion:  '))
        os.system('cls')

        tmbFinal = TMB * tiempo
        pesoFinal = 7000 * abs((pesoActual - pesoObjetivo))

        #Poco o Ningun Ejercicio
        if(nivelActividadFisica == 1):
            calorias = tmbFinal * 1.2
            calorias = (calorias - pesoFinal)
            return calorias
        #Ejercicio Ligero
        if(nivelActividadFisica == 2):
            calorias = tmbFinal* 1.375
            calorias = (calorias - pesoFinal)
            return calorias
        #Ejercicio Moderado
        if(nivelActividadFisica == 3):
            calorias = tmbFinal * 1.55
            calorias = (calorias - pesoFinal)
            return calorias
        #Deportista
        if(nivelActividadFisica == 4 ):
            calorias = tmbFinal * 1.72
            calorias = (calorias - pesoFinal)
            return calorias
        #Atleta
        if(nivelActividadFisica == 5):
            calorias = tmbFinal * 1.9
            calorias = (calorias - pesoFinal)
            return calorias

    #Calcular calorias a Consumir x Comida

    def caloriasXComida(self,pesoObjetivo,tiempo,calorias):
        calXDia = calorias / tiempo
        listaCalorias = [calXDia * 0.20,calXDia * 0.10,calXDia * 0.30]
        os.system('cls')

                
        print(f'Usted debe de consumir {calXDia} Kcal por dia durante los proximos {tiempo} para alcanzar el peso deseado de {pesoObjetivo} Kg')
        print('Comidas Diarias')
        print(f'Desayuno: {listaCalorias[0]} kcal')
        print(f'Media Mañana: {listaCalorias[1]} kcal')
        print(f'Almuerzo: {listaCalorias[2]} kcal')
        print(f'Merienda: {listaCalorias[1]} kcal')
        print(f'Cena: {listaCalorias[2]} kcal')

    def recomendacionEjercicios(self,pesoObjetivo,tiempo,calorias,pesoActual):
        ejercicios = [['Pesas: Poco Peso',1.52],['Yoga',2.11],['Maquina de escalar',3.16],['Pesas: Moderado',3.16],['Bicicleta estatica',3,70],['Maquina de Remo',3.70],['VolleyBall',1.52],['Golf',1.8],['Caminar 5km',2.38],['Nadar',3.1]]
        os.system('cls')
        promedioCalorias = 0

        #Promedio de Calorias para calorias finales tabla nutricional
        for i in range(len(ejercicios)):
            arrayAux = ejercicios[i]
            promedioCalorias += arrayAux[1] * pesoActual
            if(i == len(ejercicios)):
                promedioCalorias += arrayAux[1] * pesoActual
                promedioCalorias = promedioCalorias / len(ejercicios) 

        self.caloriasXComida(pesoObjetivo,tiempo,(promedioCalorias+calorias))
        print('\nAl otorgar una recomendacion de actividades a realizar se cambiara los consumos caloricos por comida\n')

        #Recomendacion de Ejercicios
        for i in range(len(ejercicios)):
            arrayAux = ejercicios[i]
            caloriasRecomendadas = pesoActual * arrayAux[1]
            print(f'{arrayAux[0]}: {caloriasRecomendadas} Kcal ')


#Carga de datos antropometricos

def cargarDatos():
    print('Los numeros escrito con , deberan de ingresarse con un . (Ej: 57,6 => 57.6)\nIngrese los siguientes datos para iniciar\n')
    sexo = input('Ingrese su sexo(Masculino | Femenino): ')
    edad = int(input('Ingrese su Edad: '))
    pesoInicial = int(input('Ingrese su peso actual en Kg: '))
    estatura = int(input('Ingrese su estatura en cm: '))
    pesoObjetivo = float(input('Ingrese su Peso Objetivo: '))
    tiempo = int(input('Ingrese la cantidad de dias para llegar a su Peso Deseado: '))
    user = Usuario(sexo,edad,estatura,pesoInicial,pesoObjetivo, tiempo)
    return user