import numpy as np
from processimage import *

def eigenface(dataset):
    # dataset adalah array of matriks gambar
    # mencari mean dari semua matriks dataset
    sumMatrix = []
    for i in range (0,len(dataset)-1):
        sumMatrix += dataset[i]
    meanDataset = sumMatrix / len(dataset)
    
    # cari selisih dari tiap matriks dataset dengan meanDataset
    selisih = []
    for i in range (0,len(dataset)-1):
        selisih.append(dataset[i] - meanDataset)
    
    # hitung nilai matriks kovarian: rata rata dari perkalian antara matriks selisih dengan transposnya
    arrCovarian = []
    for i in range (0,len(selisih)-1):
        arrCovarian.append(np.matmul(selisih[i],np.selisih[i].transpose()))
    sumCovarian = []
    for i in range (0,len(arrCovarian)-1):
        sumCovarian += arrCovarian[i]
    covarian = sumCovarian / len(arrCovarian)
    
    # cari eigen value dan eigen vector dari covarian
    eigenValue,eigenVector=np.linalg.eig(covarian)
    
    # cari eigen face dengan mengalikan eigen vector dengan selisih masing masing foto, lalu jumlahkan
    EigenFace = []
    for i in range (0,len(dataset)-1):
        EigenFace += (np.matmul(eigenVector,selisih[i]))
        