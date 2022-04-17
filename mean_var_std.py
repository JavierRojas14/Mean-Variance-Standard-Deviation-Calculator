import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    
    else:
        matriz = []
        for i in range(0, 9, 3):
            arreglo = list[i: i + 3]
            matriz.append(arreglo)
        
        matriz = np.array(matriz)


    calculations = None
    return calculations

calculate([1, 2,3,4,5,6,7,8,9])