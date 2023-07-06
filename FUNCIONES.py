import numpy as np
import os
import time
import msvcrt
#{==================================================================================}
arreglo_escenario = np.zeros((10,10),int)
#{----------------------------------------------------------------------------------}
list_ruts          = []
list_filas         = []
list_columnas      = []
list_cant_entradas = []
list_tipo_entradas = []
#{----------------------------------------------------------------------------------}
Platinum = 120000 #(Asientos del 1 al 20)
Gold = 80000 #(Asientos del 21 al 50)
Silver = 50000 #(Asientos del 51 al 100)
#{----------------------------------------------------------------------------------}
conta_Platinum = 0
conta_Gold = 0
conta_Silver = 0
#{----------------------------------------------------------------------------------}
acum_Platinum = 0
acum_Gold = 0
acum_Silver = 0
#{==================================================================================}
def menu_principal():
    os.system ('cls')
    print ("""======================= Menu ==========================
Bienvenido || Entradas para: Michael Jam disponibles!
=======================================================
\t1.- Comprar entradas
\t2.- Mostrar ubicaciones disponibles
\t3.- Ver listado de asistentes
\t4.- Mostrar ganancias totales
=======================================================
\n5.- Salir
=======================================================
    """)
#{==================================================================================}
def vali_opcion():
    while True:
        try:
            opci = int(input("\nSeleccione una opcion: "))
            if opci in (1,2,3,4,5):
                return opci
            else:
                print("\nSeleccione una opcion disponible!")
        except:
            print ("\nUse numeros para seleccionar!")
#{==================================================================================}
def tipo_entrada():
    while True:
        try:
            tipo = int(input("\nIngrese donde posicionarse: "))
            if tipo in (1,2):
                print(f"\nUsted ha seleccionado la posicion Platinum equivalente a ${Platinum}")
                #conta_Platinum +=1
                #acum_Platinum += 120000
#{----------------------------------------------------------------------------------}
            elif tipo in (3,4,5):
                print(f"\nUsted ha seleccionado la posicion Gold equivalente a ${Gold}")
                #conta_Gold +=1
                #acum_Gold += 80000
#{----------------------------------------------------------------------------------}
            elif tipo in (6,7,8,9,10):
                print(f"\nUsted ha seleccionado la posicion Silver equivalente a ${Silver}")
                #conta_Silver +=1
                #acum_Silver += 50000
#{----------------------------------------------------------------------------------}
            else:
                print("\nPosicion no existente!")
        except:
            print("\nFormato de tipo entrada invalido, ingrese numeros!")
#{==================================================================================}
def cantidad_entrada():
    while True:
        try:
            cant_entrada = int(input("\nIngrese la cantidad de entradas a comprar (de 1 a 3): "))
            if cant_entrada >= 1 and cant_entrada <=3:
                return cant_entrada
            else:
                 print("\nNumero de entradas no disponible!")
        except:
             print("\nFormato de cantidad invalido, ingrese numeros")
#{==================================================================================}
def vali_ruts():
    while True:
        try:
            rut = int(input("\nIngrese su rut (sin digito verificador - ni signos): "))
            if rut >= 10000000 and rut <= 99999999:
                return rut
            else:
                print("\nRut invalido!")
        except:
             print("\nFormato de rut invalido, ingrese numeros!")
#{==================================================================================}
def ver_posiciones():
    print("\nSuponiendo que puede ver las filas y columnas porque Dios mio, no recuerdo la formula, me siento idiota")
#{==================================================================================}
def vali_entrada():
    if 0 not in arreglo_escenario:
        print("Todos los lugares se encuentran vendidos!")
        #ver_posiciones()
    rut = vali_ruts()
    cant_entrada = cantidad_entrada()
    tipo = tipo_entrada
    list_ruts.append(rut)
    list_cant_entradas.append(cant_entrada)
    list_tipo_entradas.append(tipo)
    list_ruts.append(rut)
    #list_filas.append(fila)
    #list_columnas.append(columna)
    print ("La compra se ha realizado con exito!")
    print("\nPresione una tecla para continuar!")
    msvcrt.getch()
    return
#{==================================================================================}
def encontrar_asistente():
    print (list_ruts)
    print("\nPresione una tecla para continuar!")
    msvcrt.getch()
#{==================================================================================}
def ganancias():
    acumulador_tipos = conta_Silver + conta_Gold + conta_Platinum
    acumulador_totales = conta_Silver * Silver + conta_Gold * Gold + conta_Platinum * Platinum
    print(f"""
\t __________________________________________________________________________________
\t|                   |                  |                                           |  
\t|    Tipo entrada   |     Cantidad     |          Total                            |
\t|___________________|__________________|___________________________________________|
\t|                                                                  |
\t|Platinum {Platinum}          {conta_Platinum}            {conta_Platinum * Platinum}
\t|___________________|__________________|___________________________________________|
\t|                                                                                  |
\t|Gold {Gold}          {conta_Gold}            {conta_Gold * Gold}
\t|___________________|__________________|___________________________________________|
\t|                                                                                  |
\t|Silver {Silver}          {conta_Silver}          {conta_Silver * Silver}
\t|___________________|__________________|___________________________________________|
\t|                                                                                  |
\t|   TOTAL:                {acumulador_tipos}          {acumulador_totales}   |
\t|___________________|__________________|___________________________________________|
    """)
    print("\nPresione una tecla para continuar!")
    msvcrt.getch()
#{==================================================================================}
def cierre_programa():
    print ("\nGracias por usar el programa!")
    print ("\n= Made by: Benjamin Concha - 06-07-2023 =")
#{==================================================================================}
def ver_posiciones_WIP():
    for x in range (10):
        print(f"fila {x+1}| ", end=" ")
        print(arreglo_escenario)
        for y in range (10):
            print(arreglo_escenario[y])
            print() 
    print("\nPresione una tecla para continuar!")
    msvcrt.getch()
#{==================================================================================}