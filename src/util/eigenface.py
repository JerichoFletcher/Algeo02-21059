import numpy as np
from eigenpair import *

#N = 3
#dataset
datasetVector = []
meanDataset = []
eigenFaceVector = []

def matrixToVector(m):
    # Mengubah matriks m (N x N) menjadi vektor (N^2 x 1)
    #v = np.array([0] for i in range (len(m)**2))
    v = np.zeros(((len(m))**2, 1))
    #v = np.array([[0] for i in range (0,len(m)**2)])
    for j in range (len(m)):
        for i in range (len(m)):
            v[i+j*(len(m))][0] = m[i][j]
    return v

def vectorToMatrix(v):
    # vector (N^2 x 1) to matrix (N x N)
    m = np.array([[0. for j in range (int(len(v) ** 0.5))] for i in range (int(len(v) ** 0.5))])
    for i in range (len(v)):
        m[i%(int(len(v)**0.5))][i//(int(len(v)**0.5))] = v[i][0]
    '''
    for i in range (0,len(v)):
        m[i//(int(len(v)**0.5))][i%(int(len(v)**0.5))] = v[i]
    '''
    return m

def packToMatrix(arrayM):
    # "append" a buah matrix menjadi satu matriks berukuran N^2 x a
    #A = np.array([[0 for j in range (len(arrayM))] for i in range(len(arrayM[0]))])
    A = np.zeros((len(arrayM[0]), len(arrayM)))
    #A = np.array([[0 for j in range(len(arrayM))] for i in range (len(arrayM[0]))])
    for i in range (len(arrayM[0])):
        for j in range (len(arrayM)):
            A[i][j] = arrayM[j][i][0]
    return A

def eigenface(dataset):
    print(dataset)
    # dataset adalah array of matriks gambar dengan ukuran N x N
    # ubdah semua matriks pada data set menjadi ukuran N^2 x 1
    datasetVector = np.array([[[0] for i in range(len(dataset[0])**2)] for x in range (len(dataset))])
    for i in range (len(dataset)):
        datasetVector[i] = (matrixToVector(dataset[i]))
    #print("datasetVector")
    #print(datasetVector)
    
    # mencari mean dari semua matriks dataset
    sumMatrix = np.array([[0] for i in range (len(dataset[0])**2)])
    for i in range (0,len(datasetVector)):
        sumMatrix = sumMatrix + datasetVector[i]
        #print("sum matrix")
        #print(sumMatrix)
    meanDataset = np.floor(sumMatrix / len(datasetVector))
    #print("mean data set")
    #print(meanDataset)
    
    # cari selisih dari tiap matriks dataset dengan meanDataset
    selisih = np.array([[[0] for i in range(len(dataset[0])**2)] for x in range (len(dataset))])
    for i in range (0,len(dataset)):
        selisih[i] = abs(np.subtract(datasetVector[i], meanDataset))
    #print("selisih")
    #print(selisih)
    
    # hitung nilai matriks kovarian: rata rata dari perkalian antara matriks selisih dengan transposnya
    A = packToMatrix(selisih)
    AT = np.transpose(A)
    #print("A = pack to matrix selisih")
    #print(A)
    #print("A transpose")
    #print(AT)
    covarian = np.matmul(AT,A)
    #covarian = np.matmul(A,AT)
    print("covarian")
    print(covarian)
    
    # cari eigen value dan eigen vector dari covarian
    #eigenVector = np.array([0.0,0.0] for x in len(dataset))
    #eigenValue,eigenVector=np.linalg.eig(covarian)
    eigenValue,eigenVector=extractEigenpairsQR(covarian)
    #print("eigenValue")
    #print(eigenValue)
    print("eigen vector")
    print(eigenVector)
    
    # cari magnitude eigen vector
    magnitudeEigenVector = np.array([0. for i in range (len(eigenVector))])
    for i in range (len(magnitudeEigenVector)):
        sumMagnitude = 0
        for j in range (len(eigenVector[0])):
            sumMagnitude += (eigenVector[i][j] ** 2)
        magnitudeEigenVector[i] = (sumMagnitude ** 0.5)
    print("magnitudeEigenVector")
    print(magnitudeEigenVector)
    
    # cari eigenface dengan mengalikan A dengan setiap eigen vector
    eigenFaceVector = np.array([[0. for i in range(len(dataset[0])**2)] for x in range (len(dataset))])
    for i in range (len(dataset)):
        eigenFaceVector[i] = np.matmul(A,eigenVector[i])
    print("eigenfaceVector")
    print(eigenFaceVector)
    '''return eigenFaceVector'''
    
    # ubdah bentuk eigenface yang dalam bentuk vector (N^2 x 1) menjadi (N x N)
    #retEigenface = np.array([[[0. for j in range (len(dataset[0]))] for i in range(len(dataset[0]))] for x in range (len(dataset))])
    #for i in range (len(dataset)):
    #    retEigenface[i] = (vectorToMatrix(arrEigenface[i]))
    #print("retEigenface")
    #print(retEigenface)
    #return retEigenface

def ruangWajah():
    # menghitung ruang wajah
    arrRuangWajah = np.array([[0] for i in range (len(datasetVector))])
    for i in range (len(arrRuangWajah)):
        arrRuangWajah[i] = np.matmul(np.transpose(eigenFaceVector[i]), np.subtract(datasetVector[i], meanDataset))
    return arrRuangWajah

        