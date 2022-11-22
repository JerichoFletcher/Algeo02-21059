import numpy as np
from util.eigenpair import *
from math import sqrt

#dataset
datasetVector = []
meanDataset = []
eigenFaceVector = []
arrRuangWajah = []

def matrixToVector(m):
    # Mengubah matriks m (N x N) menjadi vektor (N^2 x 1)
    v = np.zeros(((len(m))**2, 1))
    for j in range (len(m)):
        for i in range (len(m)):
            v[i+j*(len(m))][0] = m[i][j]
    return v

def vectorToMatrix(v):
    # vector (N^2 x 1) to matrix (N x N)
    m = np.array([[0. for j in range (int(len(v) ** 0.5))] for i in range (int(len(v) ** 0.5))])
    for i in range (len(v)):
        m[i%(int(len(v)**0.5))][i//(int(len(v)**0.5))] = v[i][0]
    return m

def packToMatrix(arrayM):
    # "append" a buah matrix menjadi satu matriks berukuran N^2 x a
    A = np.zeros((len(arrayM[0]), len(arrayM)))
    for i in range (len(arrayM[0])):
        for j in range (len(arrayM)):
            A[i][j] = arrayM[j][i][0]
    return A

def eigenface(dataset):
    global datasetVector, meanDataset, eigenFaceVector, arrRuangWajah
    
    # dataset adalah array of matriks gambar dengan ukuran N x N
    # ubah semua matriks pada data set menjadi vektor ukuran N^2 x 1
    datasetVector = np.array([[[0] for i in range(len(dataset[0])**2)] for x in range (len(dataset))])
    for i in range (len(dataset)):
        datasetVector[i] = (matrixToVector(dataset[i]))
    
    # mencari mean dari semua matriks dataset
    sumMatrix = np.array([[0] for i in range (len(dataset[0])**2)])
    for i in range (0,len(datasetVector)):
        sumMatrix = sumMatrix + datasetVector[i]
    meanDataset = (sumMatrix / len(datasetVector))
    
    # cari selisih dari tiap matriks dataset dengan meanDataset
    selisih = np.array([[[0.] for i in range(len(dataset[0])**2)] for x in range (len(dataset))])
    for i in range (0,len(dataset)):
        selisih[i] = (np.subtract(datasetVector[i], meanDataset))
    
    # hitung nilai matriks kovarian: rata rata dari perkalian antara matriks selisih dengan transposnya
    A = packToMatrix(selisih)
    AT = np.transpose(A)
    covarian = np.matmul(AT,A)
    
    # cari eigen value dan eigen vector dari covarian
    eigenValue,eigenVector=extractEigenpairsQR(covarian)
    
    # cari eigenface dengan mengalikan A dengan setiap eigen vector
    eigenFaceVector = np.array([[0. for i in range(len(dataset[0])**2)] for x in range (len(dataset))])
    for i in range (len(dataset)):
        eigenFaceVector[i] = np.matmul(A,eigenVector[i])
    
    # menghitung ruang wajah
    arrRuangWajah = np.array([[0. for j in range (len(dataset))] for i in range (len(dataset))])
    for i in range (len(dataset)):
        for j in range (len(dataset)):
            arrRuangWajah[i][j] = np.matmul(np.transpose(eigenFaceVector[j]),selisih[i])

def testImage(newFace):
    # parameter matriks image / wajah baru
    newFaceVector = matrixToVector(newFace)
    newSelisih = newFaceVector - meanDataset
    
    # mencari weight / ruang wajah baru
    newRuangWajah = np.array([0. for i in range (len(eigenFaceVector))])
    for i in range (len(eigenFaceVector)):
        newRuangWajah[i] = np.matmul(np.transpose(eigenFaceVector[i]),newSelisih)
    
    # hitung (matriks) euclidean distance
    matEuclideanDistance = np.array([[0. for j in range (len(datasetVector))] for i in range (len(datasetVector))])
    for i in range (len(datasetVector)):
        matEuclideanDistance[i] = np.subtract(newRuangWajah, np.transpose(arrRuangWajah[i]))
    
    # hitung euclidean distance (magnitude)
    EuclideanDistance = np.array([0. for i in range (len(datasetVector))])
    for i in range (len(datasetVector)):
        for j in range (len(datasetVector)):
            EuclideanDistance[i] += (matEuclideanDistance[i][j]**2)
        EuclideanDistance[i] = sqrt(EuclideanDistance[i])
    
    # threshold
    threshold = (np.max(arrRuangWajah) - np.min(arrRuangWajah)) / 2
    print(f'Selection threshold: {threshold}')
    
    # cari euclidean distance terkecil
    min = np.inf
    idxmin = -1
    for i in range (len(datasetVector)):
        if min > EuclideanDistance[i]:
            min = EuclideanDistance[i]
            if EuclideanDistance[i] < threshold:
                idxmin = i
    print(f'Minimum distance is {min}')
    return idxmin
