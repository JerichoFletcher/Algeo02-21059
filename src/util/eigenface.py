import numpy as np
from processimage import *

N = 256

def eigenface(dataset):
    print(dataset)
    # dataset adalah array of matriks gambar
    # mencari mean dari semua matriks dataset
    sumMatrix = [[0 for j in range(N)] for i in range(N)]
    for i in range (0,len(dataset)):
        sumMatrix = sumMatrix + dataset[i]
        #print("sum matrix")
        #print(sumMatrix)
    meanDataset = sumMatrix / len(dataset)
    #print("mean data set")
    #print(meanDataset)
    
    # cari selisih dari tiap matriks dataset dengan meanDataset
    selisih = []
    for i in range (0,len(dataset)):
        selisih.append(dataset[i] - meanDataset)
    #print("selisih")
    #print(selisih)
    
    # hitung nilai matriks kovarian: rata rata dari perkalian antara matriks selisih dengan transposnya
    arrCovarian = []
    for i in range (0,len(selisih)):
        covarianMult = [[0 for j in range(N)] for i in range(N)]
        covarianMult = np.matmul(selisih[i],selisih[i].transpose()) # salah di sini
        arrCovarian.append(covarianMult)
    #print("arr covarian selisih dikali transposnya")
    #print(arrCovarian)
    sumCovarian = [[0 for j in range(N)] for i in range(N)]
    for i in range (0,len(arrCovarian)):
        sumCovarian = sumCovarian + arrCovarian[i]
    #print("sum covarian")
    #print(sumCovarian)
    
    covarian = [[0 for j in range(N)] for i in range(N)]
    covarian = sumCovarian * (1 / len(arrCovarian)) # masih error di sini
    #print("covarian")
    #print(covarian)
    
    # cari eigen value dan eigen vector dari covarian
    eigenValue,eigenVector=np.linalg.eig(covarian)
    #print("eigen vector")
    #print(eigenVector)
    # cari eigen face dengan mengalikan eigen vector dengan selisih masing masing foto, lalu jumlahkan
    EigenFace = [[0 for j in range(N)] for i in range(N)]
    for i in range (0,len(selisih)):
        #print("selisih")
        #print(selisih[i])
        eigFaceMult = np.matmul(eigenVector,selisih[i])
        #print("eigFaceMult")
        #print(eigFaceMult)
        EigenFace += (eigFaceMult)
        #print("eigen faceeee")
        #print(EigenFace)
    #print("eigen face hasil")
    #print(EigenFace)
        