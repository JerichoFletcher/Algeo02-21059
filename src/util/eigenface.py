import numpy as np
from util.processimage import *

#N = 3

def matrixToVector(m):
    # Mengubah matriks m (N x N) menjadi vektor (N^2 x 1)
    #v = np.array([0] for i in range (len(m)**2))
    v = np.zeros(((len(m))**2, 1))
    #v = np.array([[0] for i in range (0,len(m)**2)])
    count = 0
    for i in range (0,len(m)):
        for j in range (0,len(m)):
            v[(i+j+2*count)][0] = m[i][j]
        count += 1
    return v

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
    datasetVector = np.array([[[0] for i in range(N**2)] for x in range (len(dataset))])
    for i in range (len(dataset)):
        datasetVector[i] = (matrixToVector(dataset[i]))
    print("datasetVector")
    print(datasetVector)
    
    # mencari mean dari semua matriks dataset
    sumMatrix = np.array([[0] for i in range (N**2)])
    #sumMatrix = np.zeros((N**2, 1))
    #sumMatrix = np.array([[0 for j in range(N**2)] for i in range(N**2)])
    for i in range (0,len(datasetVector)):
        sumMatrix = sumMatrix + datasetVector[i]
        #print("sum matrix")
        #print(sumMatrix)
    meanDataset = (sumMatrix / len(datasetVector))
    print("mean data set")
    print(meanDataset)
    
    # cari selisih dari tiap matriks dataset dengan meanDataset
    selisih = np.array([[[0.] for i in range(N**2)] for x in range (len(dataset))])
    #selisih = np.arange(len(datasetVector))
    #selisih = np.array([])
    for i in range (0,len(dataset)):
        #print("datasetVector[i]")
        #print(datasetVector[i])
        #print(meanDataset)
        #print("meanDataset")
        selisih[i] = abs(np.subtract(datasetVector[i], meanDataset))
        #print("selisih[i]")
        #print(selisih[i])
        #print("---------------------")
        #selisih = np.append([selisih, abs(datasetVector[i] - meanDataset)], axis=0)
        #selisih.append(abs(datasetVector[i] - meanDataset))
    print("selisih")
    print(selisih)
    
    # hitung nilai matriks kovarian: rata rata dari perkalian antara matriks selisih dengan transposnya
    A = packToMatrix(selisih)
    AT = np.transpose(A)
    print("A = pack to matrix selisih")
    print(A)
    print("A transpose")
    print(AT)
    covarian = np.matmul(AT,A)
    print("covarian")
    print(covarian)
    
    #arrCovarian = []
    '''
    for i in range (0,len(selisih)):
        covarianMult = [[0 for j in range(N)] for i in range(N)]
        covarianMult = np.matmul(selisih[i],selisih[i].transpose()) # salah di sini
        arrCovarian.append(covarianMult)
    '''
    #print("arr covarian selisih dikali transposnya")
    #print(arrCovarian)
    '''
    sumCovarian = [[0 for j in range(N)] for i in range(N)]
    for i in range (0,len(arrCovarian)):
        sumCovarian = sumCovarian + arrCovarian[i]
    '''
    #print("sum covarian")
    #print(sumCovarian)
    '''
    covarian = [[0 for j in range(N)] for i in range(N)]
    covarian = sumCovarian * (1 / len(arrCovarian)) # masih error di sini
    print("covarian")
    print(covarian)
    '''
    
    # cari eigen value dan eigen vector dari covarian
    eigenValue,eigenVector=np.linalg.eig(covarian)
    print("eigen vector")
    print(eigenVector)
    '''
    # cari eigen face dengan mengalikan eigen vector dengan selisih masing masing foto, lalu jumlahkan
    #EigenFace = np.zeros((N, N))
    EigenFace = np.array([[0. for j in range(len(eigenVector))] for i in range(len(eigenVector))])
    for i in range (0,len(selisih)):
        print("----------")
        print("selisih")
        print(selisih[i])
        eigFaceMult = np.matmul([eigenVector],selisih[i])
        print("eigFaceMult")
        print(eigFaceMult)
        EigenFace += (eigFaceMult)
        print("eigen faceeee")
        print(EigenFace)
    print("eigen face hasil")
    print(EigenFace)
    '''
        