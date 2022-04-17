import numpy as np
from pandas import array

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    
    else:
        # Función hacer matriz
        matriz = np.zeros((1, 3))
        for i in range(0, 9, 3):
            arreglo = np.array(list[i: i + 3])
            matriz = np.vstack([matriz, arreglo])
        
        matriz = matriz[1:]
        resultados = calcular_estadisticas(matriz)

        return resultados

def calcular_estadisticas(matriz):
    resultado = {'mean': [], 'variance': [], 'standard deviation': [],
                 'max': [], 'min': [], 'sum': []}

    for i in range(3):
        if i != 2:
            mean = np.mean(matriz, axis = i)
            var = np.var(matriz, axis = i)
            std = np.std(matriz, axis = i)
            max = np.max(matriz, axis = i)
            min = np.min(matriz, axis = i)
            sum = np.sum(matriz, axis = i)
        
        else:
            mean = np.mean(matriz)
            var = np.var(matriz)
            std = np.std(matriz)
            max = np.max(matriz)
            min = np.min(matriz)
            sum = np.sum(matriz)
        
        resultado['mean'].append(mean.tolist())
        resultado['variance'].append(var.tolist())
        resultado['standard deviation'].append(std.tolist())
        resultado['max'].append(max.tolist())
        resultado['min'].append(min.tolist())
        resultado['sum'].append(sum.tolist())

    return resultado
