import numpy as np

def clientAssignment(matrix):
    n_rows,n_columns = np.shape(matrix)
    arrayOfElements = []
    for i in range(min(n_rows,n_columns)):
        #max_current = np.amax(matrix)
        max_pos = [0,0]
        max_current = matrix[0][0]
        for j in range(n_rows):
            for k in range(n_columns):
                if(matrix[j][k] > max_current):
                    max_pos = [j,k]
                    max_current = matrix[j][k]
        #print(max_current)
        #print(max_pos)
        #print(matrix)
        
        # SElect the position
        arrayOfElements.append(max_pos)
        
        # Convert all elements in line/column to -1
        matrix[max_pos[0]][:] = -1
        matrix[:,max_pos[1]] = -1
    return np.array(arrayOfElements)



matrix = np.random.randint(1,high=40,size=(2,1))

a = clientAssignment(matrix)
