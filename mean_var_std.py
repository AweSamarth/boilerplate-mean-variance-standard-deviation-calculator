import numpy as np

def calculate(list):
    if (len(list)<9):
        raise ValueError("List must contain nine numbers.")
    matrix = np.array(list)
    matrix.shape = (-1, 3)
    # print(matrix)

    calculations={  }
    
    # np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

    calculations['mean']=[np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix)]
    calculations['variance']=[np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix)]
    calculations['standard deviation']=[np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix)]
    calculations['max']=[np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix)]
    calculations['min']=[np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix)]
    calculations['sum']=[np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix)]

    # print(calculations)
    
    return calculations
    
    
    # return calculations
    

# print(calculate([2,6,2,8,4,0,1,]))