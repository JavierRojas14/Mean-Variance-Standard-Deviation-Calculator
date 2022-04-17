import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    
    else:
        matriz = np.zeros((1, 3))
        for i in range(0, 9, 3):
            arreglo = np.array(list[i: i + 3])
            matriz = np.vstack([matriz, arreglo])
        
        matriz = matriz[1:]


    calculations = None
    return calculations

calculate([1, 2,3,4,5,6,7,8,9])