import time
import matplotlib.pyplot as plt

def rotateStrings (S, T) :

    for s in range(T) :

        rotations = ''
        copy = S[s] 

        for j in range(len(copy) - 1) :
            temp = copy[0]
            copy = copy[1:]  
            copy += temp
            rotations += (copy + ' ')

        print(rotations + str(S[s]))
