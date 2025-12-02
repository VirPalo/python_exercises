# Calculadora de distancia entre dos puntos en el plano con coordenadas x e y.

import math

# Función para calcular la distancia
def calcular_distancia(x1, y1, x2, y2):
    '''
    Calcula la distancia entre dos puntos en el plano.
    
    Args:
    x1 (float): Coordenada x del primer punto
    y1 (float): Coordenada y del primer punto
    x2 (float): Coordenada x del segundo punto
    y2 (float): Coordenada y del segundo punto
    
    Return:
    distancia (float): Distancia entre los dos puntos
    
    '''

    # Calculo de la distancia
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    return distancia
    
# Función para validar datos ingresados
def validar_coordenada(mensaje):
    '''
    Valida la coordenada numérica ingresada por el usuario
    
    Arg:
    mensaje (str): Mensaje que se muestra al usuario
    
    Return:
    value (float): Coordenada validada
    '''
    
    while True:
        try:
            value = float(input(mensaje))
            return value
        except ValueError:
            print('Error: Por favor, ingrese valores numericos válidos')
            
# Función para obtener las coordenadas por teclado
def obtener_coordenadas(numero_punto):
    '''
    Solicita las coordenadas x e y de un punto.
    
    Arg:
    numero_punto (int): Número del punto a ingresar (1 o 2)
    
    Returns:
    x, y (tuple): Coordenadas del punto
    '''
    
    x = validar_coordenada(f'Ingrese la coordenada x del punto {numero_punto}.')
    y = validar_coordenada(f'Ingrese la coordenada y del punto {numero_punto}.')
    
    return x, y

# Función para mostrar resultados
def mostrar_resultados(x1, x2, y1, y2, distancia):
    '''
    Se muestran los resultados obtenidos
    
    Args:
    x1 (float): Coordenada x del primer punto
    y1 (float): Coordenada y del primer punto
    x2 (float): Coordenada x del segundo punto
    y2 (float): Coordenada y del segundo punto
    distancia (float): Distancia entre los dos puntos
    '''
    
    print('\n--- Resultado ---')
    print(f'Punto 1: {x1}, {y1}')
    print(f'Punto 2: {x2}, {y2}')
    print(f'Distancia: {distancia:.2f} unidades.')


def main():
    pass


#Llamada a la función
#dist_between_points(x1, y1, x2, y2)