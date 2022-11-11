import numpy as np
import random

debug = False
errThreshold = 1E-32

# FUNGSI
# err -- Mengembalikan nilai error dari val terhadap orig
def err(val, orig):
    if abs(float(orig)) < errThreshold: return np.inf
    r = float(orig / val)
    return abs(1.0 - r)

# decomposeQR -- Mengembalikan Q, R di mana Q dan R adalah matriks dekomposisi QR dari M
def decomposeQR(M):
    # TODO: Implementasi algoritma dekomposisi QR
    return np.linalg.qr(M)

# extractEigenpairsQR -- Mengembalikan L, V di mana:
#   L adalah array berisi taksiran semua eigenvalue dari M
#   V adalah array berisi taksiran semua eigenvector dari M
#   Dengan eigenvalue L[i] berkorespondensi dengan eigenvector V[i]
#   Taksiran dilakukan menggunakan metode dekomposisi QR
def extractEigenpairsQR(M, iter=None):
    A = np.copy(M)
    n = A.shape[0]
    Qi = np.eye(n)

    oldVal = 0
    newVal = None
    i = 0
    while iter is None or i < iter:
        i += 1

        S = A[n-1][n-1] * np.eye(n)
        Q, R = np.linalg.qr(np.subtract(A, S))
        A = np.add(R @ Q, S)
        Qi = Qi @ Q

        newVal = A[0][0]
        if iter is None and err(newVal, oldVal) < errThreshold: break
        oldVal = newVal
    if debug: print(f"{i} iterations with QR")
    return np.diag(A), Qi

# maxEigenpairPI -- Mengembalikan nilai eigenvalue terbesar dari suatu matriks M, ditaksir menggunakan metode power-iteration
def maxEigenpairPI(M):
    eigVec = np.random.rand(len(M))

    oldEigVal = 0
    eigVal = None
    if debug: i = 0
    while True:
        temp = np.dot(M, eigVec)
        eigVal = np.linalg.norm(temp)
        eigVec = temp / eigVal

        if err(eigVal, oldEigVal) < errThreshold: break
        oldEigVal = eigVal
        if debug: i += 1
    if debug: print(f"{i} iterations with power iteration")
    return (eigVal, eigVec)

# extractEigenpairsPI -- Mengembalikan array berisi taksiran semua eigenvalue dari M
# WARNING: Sangat lambat untuk matriks besar! Fungsi ini hanya untuk testing/benchmarking
# Gunakan extractEigenpairsQR untuk practical application
def extractEigenpairsPI(M):
    origMat = np.copy(M)
    currMat = np.copy(M)
    eigenpairs = []
    for i in range(len(currMat)):
        L, V = maxEigenpairPI(currMat)
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
    debug = True

    """mat = np.array(
        [[52., 30., 49., 28.],
        [30., 50., 8., 44.],
        [49., 8., 46., 16.],
        [28., 44., 16., 22.]]
    )"""
    mat = np.array([[random.random() for j in range(256)] for i in range(256)])

    # Test with power iteration
    """# Commented out: too slow for large matrices
    eigenpairs = extractEigenpairsPI(mat)
    print(eigenpairs)
    print()"""

    # Test with QR decomposition iterate until convergent
    print("QR decomposition (iterate until converge):")
    L, V = extractEigenpairsQR(mat)
    print("Eigenvalues: "); print(L)
    print("Eigenvectors: "); print(V)
    print()

    # Test with QR decomposition iterate N times
    N = 20
    print(f"QR decomposition (iterate {N} times):")
    L, V = extractEigenpairsQR(mat, iter=N)
    print("Eigenvalues: "); print(L)
    print("Eigenvectors: "); print(V)
    print()
    
    # Compare with values from numpy
    L, V = np.linalg.eig(mat)
    print("Actual value from numpy")
    print("Eigenvalues: "); print(L)
    print("Eigenvectors: "); print(V)
