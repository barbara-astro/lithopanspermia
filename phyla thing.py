# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 14:37:09 2018

@author: Basia
"""
import numpy as np 
import matplotlib.pyplot as plt

Phyla=np.linspace(1,13,13)
Class=np.linspace(1,4,4)
Order=np.linspace(1,4,4)

Ones=np.ones(16)
Twos=2*Ones
Threes=3*Ones
Fours=4*Ones
Fives=5*Ones
Sixes=6*Ones
Sevens=7*Ones
Eights=8*Ones
Nines=9*Ones
Tens=10*Ones
Elevens=11*Ones 
Twelves=12*Ones
Thirteens=13*Ones
Forteens=14*Ones
Fifteens=15*Ones
Sixteens=16*Ones
Seventeens=17*Ones
Eighteens=18*Ones
Nineteens=19*Ones
Twenties=20*Ones
TwentyOnes=21*Ones

Phyla=np.append(Ones,Twos)
Phyla=np.append(Phyla, Threes)
Phyla=np.append(Phyla, Fours)
Phyla=np.append(Phyla, Fives)
Phyla=np.append(Phyla, Sixes)
Phyla=np.append(Phyla, Sevens)
Phyla=np.append(Phyla, Eights)
Phyla=np.append(Phyla, Nines)
Phyla=np.append(Phyla, Tens)
Phyla=np.append(Phyla, Elevens)
Phyla=np.append(Phyla, Twelves)
Phyla=np.append(Phyla, Thirteens)
# =============================================================================
# Phyla=np.append(Phyla, Forteens)
# Phyla=np.append(Phyla, Fifteens)
# Phyla=np.append(Phyla, Sixteens)
# Phyla=np.append(Phyla, Seventeens)
# Phyla=np.append(Phyla, Eighteens)
# Phyla=np.append(Phyla, Nineteens)
# Phyla=np.append(Phyla, Twenties)
# Phyla=np.append(Phyla, TwentyOnes)
# =============================================================================

Ones2=np.ones(4)
Twos2=Ones2*2
Threes2=Ones2*3
Fours2=Ones2*4
Added2=np.append(Ones2,Twos2)
Added2=np.append(Added2,Threes2)
Added2=np.append(Added2,Fours2)
Class=np.append(Added2,Added2)
Class1=np.append(Class, Class)
Class=np.append(Class1, Class1)
Class=np.append(Class, Class1)
Class=np.append(Class,Added2)

Added3=np.append(Order,Order)
Added3b=np.append(Added3,Added3)
Added3b=np.append(Added3b,Added3)
Added3b=np.append(Added3b,Added3b)
Added3=np.append(Added3b, Added3b)
Orderstack=np.append(Order,Order)
Orderstack=np.append(Orderstack,Orderstack)
Added3=np.append(Added3,Orderstack)
Order=np.append(Added3,Added3b)
Order=np.append(Order,Added3b)

Matrix=np.vstack(([Phyla], [Class], [Order]))

mastermax=np.zeros(208)
#uniquePh=np.unique(Matrix[0,:])
#print(uniquePh)
for k in range(5):
    print("\n")
    maskindx=np.random.choice(np.arange(208),20)
    mask0=np.zeros(208)
    mask0[maskindx]=1
    mask1=np.zeros(208)
    for i in range(len(mask0)):
        if mask0[i]==1 and mastermax[i]==0:
            mask1[i]=1
            mastermax[i]=1
        
    for Ph in uniquePh:
        r1=Matrix[0,:]
        r2=Matrix[1,:]
        tmpcl=r2[r1==Ph]
        uniqueCl=np.unique(tmpcl)
        for Cl in uniqueCl:
            r3=Matrix[2,:]
            
            print( Ph,Cl, r3[(r2==Cl)&(r1==Ph)&(mask1==1)])  