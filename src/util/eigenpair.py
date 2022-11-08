import numpy as np

errThreshold = 1E-8

def err(val, orig):
    return abs(1 - (orig / val))

def maxEigenpairPowerIter(M):
    eigVec = np.random.rand(len(M))

    oldEigVal = 0
    eigVal = None
    while True:
        temp = np.dot(M, eigVec)
        eigVal = np.linalg.norm(temp)
        eigVec = temp / eigVal

        if err(eigVal, oldEigVal) < errThreshold: break
        oldEigVal = eigVal
    return (eigVal, eigVec)

def extractAllEigenPairsPowerIter(M):
    origMat = np.copy(M)
    currMat = np.copy(M)
    eigenpairs = []
    for i in range(len(currMat)):
        L, V = maxEigenpairPowerIter(currMat)
        eigenpairs += [L]
        
        # Find max index
        currMax = 0
        j = 1
        while j < len(currMat):
            if abs(V[j]) > abs(V[currMax]): currMax = j
            j += 1
        
        # Swap row
        for j in range(len(currMat)):
            currMat[0][j], currMat[currMax][j] = currMat[currMax][j], currMat[0][j]

        # Transform max eigenvector into its elementary form
        for j in range(1, len(currMat)):
            factor = V[j if j != currMax else 0] / V[currMax]
            for k in range(len(currMat)):
                currMat[j][k] -= factor * currMat[0][k]

        # Swap columns
        for j in range(len(currMat)):
            currMat[j][0], currMat[j][currMax] = currMat[j][currMax], currMat[j][0]

        # Extract eigenvalue from submatrix
        currMat = np.array(currMat[1:len(currMat),1:len(currMat)])

    return eigenpairs


# TESTING
if __name__ == '__main__':
    mat = np.array([[0.0, 5.0, -6.0], [-4.0, 12.0, -12.0], [-2.0, -2.0, 10.0]])
    eigenpairs = extractAllEigenPairsPowerIter(mat)
    print(eigenpairs)
