import random
import copy
from collections import Counter
def Llenar_matriz_enunciado(matriz):
    matriz.append([1,3,2,4,1])
    matriz.append([4,4,5,6,5])
    matriz.append([5,2,1,6,2])
    matriz.append([2,2,5,3,4])
    matriz.append([1,1,4,2,2])


def LLenar_matriz(matriz, dimension):
    for i in range(dimension):
        fila = []
        for j in range(dimension):
            fila.append(random.randint(1,6))
        matriz.append(fila)

def Mostrar_matriz(matriz, dimension):
    for i in range(dimension): 
        print(matriz[i])

M = []
n = 20
infectados_o = [(0,0)]
adyacentes_o =[]
presentes_o = []
def Calcular_adyacentes(infectados, adyacentes):
    global n
    for i, j in infectados:
        for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if (ii, jj) not in infectados and 0 <= ii < n and 0 <= jj < n and (ii, jj) not in adyacentes:
                adyacentes.append((ii, jj))


def Calcular_presentes(adyacentes, presentes):
    contador = 0
    for i, j in adyacentes:
        if M[i][j] not in presentes:
           presentes.append(M[i][j])

def Simular_Contagio(paciente_zero, copia_adyacentes, copia_infectados, contador):
    # Crear nuevas copias con deepcopy para evitar modificar los originales
    copia_a = copy.deepcopy(copia_adyacentes)
    copia_i = copy.deepcopy(copia_infectados)
    
    print(f'Adyacentes actuales: {copia_a}')
    print(f'Infectados actuales: {copia_i}')
    
    encuentra_victima = False  # Inicialmente, no se ha encontrado ninguna nueva víctima
    
    # Infectar las celdas adyacentes si tienen el mismo valor que el paciente cero
    for i, j in copia_a:
        if M[i][j] == paciente_zero:
            contador += 1
            copia_i.append((i, j))
            encuentra_victima = True
    
    # Recalcular los nuevos adyacentes basados en los infectados actuales
    nueva_lista_adyacentes = []
    Calcular_adyacentes(copia_i, nueva_lista_adyacentes)

    # Si no se encontraron nuevas víctimas, se detiene la recursión
    if encuentra_victima:
        return Simular_Contagio(paciente_zero, nueva_lista_adyacentes, copia_i, contador)
    else:
        return contador  # Devolver el número total de celdas infectadas

def Actualizar_infectados(last_patient, infectados):
    for i, j in infectados:
        M[i][j] = last_patient           
#  while (numero_infectados < total_casillas):
#     contador_simulacion = 0
#     mayor = 0
#     elemento_con_mayor_contagios = 0
#     adyacentes_o = []
#     presentes_o = []
#     Calcular_adyacentes(infectados_o, adyacentes_o)
#     Calcular_presentes(adyacentes_o, presentes_o)
#     for patient_zero in presentes_o:
#         contador_simulacion = Simular_Contagio(patient_zero, adyacentes_o, infectados_o, contador_simulacion)
#         if contador_simulacion > mayor:
#             mayor = contador_simulacion
#             elemento_con_mayor_contagios = patient_zero
#     Realizar_contagio(elemento_con_mayor_contagios, adyacentes_o, infectados_o)
#     Actualizar_infectados(elemento_con_mayor_contagios, infectados_o)
#     numero_infectados = len(infectados_o)
#     Mostrar_matriz(M, n)
#     print('')
#     print('')
#     print('')
def Realizar_contagio(paciente_zero, adyacentes, infectados):
    encuentra_victima = False
    for i, j in adyacentes:
        if M[i][j] == paciente_zero:
            infectados.append((i,j))
            encuentra_victima = True
    adyacentes = []
    Calcular_adyacentes(infectados, adyacentes)
    if encuentra_victima == True:
        return Realizar_contagio(paciente_zero, adyacentes, infectados)
    
LLenar_matriz(M, n)
# Llenar_matriz_enunciado(M)
Mostrar_matriz(M, n)
# print('')
# contador_contagio= [0]
# numero_infectados = len(infectados_o)
# total_casillas = n*n
# mayor = 0
# contador_simulacion = 0
# elemento_con_mayor_contagios = 0
# adyacentes_o = []
# presentes_o = []
# Calcular_adyacentes(infectados_o, adyacentes_o)
# Calcular_presentes(adyacentes_o, presentes_o)
# for patient_zero in presentes_o:
#     contador_simulacion = 0
#     contador_simulacion = Simular_Contagio(patient_zero, adyacentes_o, infectados_o, contador_simulacion)
#     print(f'para el elemento {patient_zero} hay {contador_simulacion} elementos')
    # print (presentes_o)
numero_infectados = 0
contador_pasos = 0
total_casillas = n*n
while (numero_infectados < total_casillas):
    contador_simulacion = 0
    mayor = 0
    elemento_con_mayor_contagios = 0
    adyacentes_o = []
    presentes_o = []
    Calcular_adyacentes(infectados_o, adyacentes_o)
    Calcular_presentes(adyacentes_o, presentes_o)
    for patient_zero in presentes_o:
        contador_simulacion = 0
        contador_simulacion = Simular_Contagio(patient_zero, adyacentes_o, infectados_o, contador_simulacion)
        if contador_simulacion > mayor:
            mayor = contador_simulacion
            elemento_con_mayor_contagios = patient_zero
    Realizar_contagio(elemento_con_mayor_contagios, adyacentes_o, infectados_o)
    Actualizar_infectados(elemento_con_mayor_contagios, infectados_o)
    numero_infectados = len(infectados_o)
    Mostrar_matriz(M, n)
    print('')
    print('')
    print('')
    contador_pasos += 1

print(f'El proceso ha tomado {contador_pasos} pasos')

