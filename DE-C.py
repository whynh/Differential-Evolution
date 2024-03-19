# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:17:57 2021

@author: Hendry
"""

#y = 15x - x^2
import random
#%%
N=3
induk = [0 for i in range(N)]
print(induk)
#%%
def hitungFitness(x):
    y = (15*x) - (x*x)
    return y
#%%
CR = 0.7
F = 0.5
BA = 15 
BB = 0

#Inisialisasi Populasi
for i in range(N):
    induk[i] = random.random()*(BA-BB) + BB
print(induk)    

epochs = 50
MaxFitness = [0 for i in range(epochs)]

for i in range(N):
    if (hitungFitness(induk[i])>=MaxFitness[0]):
        MaxFitness[0] = hitungFitness(induk[i])
print(induk)
print(MaxFitness)

D = 1
ctr = 1
while ctr<epochs:
    #Tidak lakukan Seleksi
    for i in range(N):
        jrand = int(random.random()*D)
        for j in range(D):
            if (random.random()<=CR or jrand==j):
                #Mutasi / Crossover
                #Lakukan crossover dan mutasi
                xr = induk[random.randint(0, N-1)]
                anak = xr + F*(induk[i])
            else:
                anak = induk[i]
        #Elitism
        if (hitungFitness(anak)>hitungFitness(induk[i])):
            induk[i] = anak
    #end for i 
    for i in range(N):
        if (hitungFitness(induk[i])>MaxFitness[ctr]):
            MaxFitness[ctr] = hitungFitness(induk[i])              
    ctr+=1
#%%
#Output
#print(MaxFitness)
#Tampilkan Hasilnya
import matplotlib.pyplot as plt
x = range(epochs)

plt.plot(x, MaxFitness)
plt.show()
print(induk)
print("Nilai Maximum: ", MaxFitness[10])