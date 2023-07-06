from FUNCIONES import *
#{==================================================}
while True:
    menu_principal()
    opci = vali_opcion()
    while True:
        if opci == 1:
            vali_entrada()
#{--------------------------------------------------}
        elif opci == 2:
            ver_posiciones()
#{--------------------------------------------------}
        elif opci == 3:
            encontrar_asistente()
#{--------------------------------------------------}
        elif opci == 4:
            ganancias()
#{--------------------------------------------------}
        else:
            print ("\nGracias por usar el programa!")
            print ("\n= Made by: Benjamin Concha - 06-07-2023 =")
            break