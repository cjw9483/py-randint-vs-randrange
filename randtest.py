
from random import randint
from random import randrange
import time
import numpy

def rint(num):
    timesint = []
    for i in range(num):
        start_time = time.time()
        for i in range(1000):
            print(f"Iteration {i}")
            #chose generation
            gen = (randint(1, 3))
            if gen == 1:
                print(gen)
                #chose season from generation 1
                g1 = (randint(1, 3))
                if g1 == 1:
                    print(g1)
                    #chose episode from season 1
                    g1s1 = (randint(1, 3))
                    if g1s1 == 1:
                        print(g1s1)
                    elif g1s1 == 2:
                        print(g1s1)
                    elif g1s1 == 3:
                        print(g1s1)
                elif g1 == 2:
                    print(g1)
                    #chose episode from season 2
                    g1s2 = (randint(1, 3))
                    if g1s2 == 1:
                        print(g1s2)
                    elif g1s2 == 2:
                        print(g1s2)
                    elif g1s2 == 3:
                        print(g1s2)
                elif g1 == 3:
                    print(g1)
                    #chose episode from season 3
                    g1s3 = (randint(1, 3))
                    if g1s3 == 1:
                        print(g1s3)
                    elif g1s3 == 2:
                        print(g1s3)
                    elif g1s3 == 3:
                        print(g1s3)
            elif gen == 2:
                print(gen)
                #chose season from generation 2
                g2 = (randint(1, 3))
                if g2 == 1:
                    print(g2)
                    #chose episode from season 1
                    g2s1 = (randint(1, 3))
                    if g2s1 == 1:
                        print(g2s1)
                    elif g2s1 == 2:
                        print(g2s1)
                    elif g2s1 == 3:
                        print(g2s1)
                elif g2 == 2:
                    print(g2)
                    #chose episode from season 2
                    g2s2 = (randint(1, 3))
                    if g2s2 == 1:
                        print(g2s2)
                    elif g2s2 == 1:
                        print(g2s2)
                    elif g2s2 == 3:
                        print(g2s2)
                elif g2 == 3:
                    print(g2)
                    #chose episode from season 2
                    g2s3 = (randint(1, 3))
                    if g2s3 == 1:
                        print(g2s3)
                    elif g2s3 == 2:
                        print(g2s3)
                    elif g2s3 == 3:
                        print(g2s3)
            elif gen == 3:
                print(gen)
                #chose season from generation 3
                g3 = (randint(1, 3))
                if g3 == 1:
                    print(g3)
                    #chose episode from season 1
                    g3s1 = (randint(1, 3))
                    if g3s1 == 1:
                        print(g3s1)
                    elif g3s1 == 2:
                        print(g3s1)
                    elif g3s1 == 3:
                        print(g3s1)
                elif g3 == 2:
                    print(g3)
                    #chose episode from season 2
                    g3s2 = (randint(1, 3))
                    if g3s2 == 1:
                        print(g3s2)
                    elif g3s2 == 2:
                        print(g3s2)
                    elif g3s2 == 3:
                        print(g3s2)
                elif g3 == 3:
                    print(g3)
                    #chose episode from season 3
                    g3s3 = (randint(1, 3))
                    if g3s3 == 1:
                        print(g3s3)
                    elif g3s3 == 2:
                        print(g3s3)
                    elif g3s3 == 3:
                        print(g3s3)
        end_time = time.time()
        exeint = end_time - start_time
        timesint.append(exeint)
    return(timesint)

def rrange(num):
    timesrange = []
    for i in range(num):
        start_time = time.time()
        for i in range(1000):
            print(f"Iteration {i}")
            #chose generation
            gen = (randrange(1, 4, 1))
            if gen == 1:
                print(gen)
                #chose season from generation 1
                g1 = (randrange(1, 4, 1))
                if g1 == 1:
                    print(g1)
                    #chose episode from season 1
                    g1s1 = (randrange(1, 4, 1))
                    if g1s1 == 1:
                        print(g1s1)
                    elif g1s1 == 2:
                        print(g1s1)
                    elif g1s1 == 3:
                        print(g1s1)
                elif g1 == 2:
                    print(g1)
                    #chose episode from season 2
                    g1s2 = (randrange(1, 4, 1))
                    if g1s2 == 1:
                        print(g1s2)
                    elif g1s2 == 2:
                        print(g1s2)
                    elif g1s2 == 3:
                        print(g1s2)
                elif g1 == 3:
                    print(g1)
                    #chose episode from season 3
                    g1s3 = (randrange(1, 4, 1))
                    if g1s3 == 1:
                        print(g1s3)
                    elif g1s3 == 2:
                        print(g1s3)
                    elif g1s3 == 3:
                        print(g1s3)
            elif gen == 2:
                print(gen)
                #chose season from generation 2
                g2 = (randrange(1, 4, 1))
                if g2 == 1:
                    print(g2)
                    #chose episode from season 1
                    g2s1 = (randrange(1, 4, 1))
                    if g2s1 == 1:
                        print(g2s1)
                    elif g2s1 == 2:
                        print(g2s1)
                    elif g2s1 == 3:
                        print(g2s1)
                elif g2 == 2:
                    print(g2)
                    #chose episode from season 2
                    g2s2 = (randrange(1, 4, 1))
                    if g2s2 == 1:
                        print(g2s2)
                    elif g2s2 == 1:
                        print(g2s2)
                    elif g2s2 == 3:
                        print(g2s2)
                elif g2 == 3:
                    print(g2)
                    #chose episode from season 2
                    g2s3 = (randrange(1, 4, 1))
                    if g2s3 == 1:
                        print(g2s3)
                    elif g2s3 == 2:
                        print(g2s3)
                    elif g2s3 == 3:
                        print(g2s3)
            elif gen == 3:
                print(gen)
                #chose season from generation 3
                g3 = (randrange(1, 4, 1))
                if g3 == 1:
                    print(g3)
                    #chose episode from season 1
                    g3s1 = (randrange(1, 4, 1))
                    if g3s1 == 1:
                        print(g3s1)
                    elif g3s1 == 2:
                        print(g3s1)
                    elif g3s1 == 3:
                        print(g3s1)
                elif g3 == 2:
                    print(g3)
                    #chose episode from season 2
                    g3s2 = (randrange(1, 4, 1))
                    if g3s2 == 1:
                        print(g3s2)
                    elif g3s2 == 2:
                        print (g3s2)
                    elif g3s2 == 3:
                        print(g3s2)
                elif g3 == 3:
                    print(g3)
                    #chose episode from season 3
                    g3s3 = (randrange(1, 4, 1))
                    if g3s3 == 1:
                        print(g3s3)
                    elif g3s3 == 2:
                        print(g3s3)
                    elif g3s3 == 3:
                        print(g3s3)
        end_time = time.time()
        exerange = end_time - start_time
        timesrange.append(exerange)
    return(timesrange)

def meancalc(q):
    mean = numpy.mean(q)
    return(mean)

def compare(r, r2):
    diffrence = r2 - r
    return(diffrence)

raint = meancalc(q=rint(num=50))
rarange = meancalc(q=rrange(num=50))
diffrence2 = compare(r=rarange, r2=raint)
print(f"The average of the randrange runs is {rarange} seconds.\nThe average of randint is {raint} seconds.\nThe diffrence between the two is {diffrence2} seconds.")
