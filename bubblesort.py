#!/usr/bin/python3
 
from __future__ import print_function
 
import random
 
def main():
        liste = []
        for x in range(0, 20):
                liste.append(random.randint(1, 100))
        sortedliste = bubblesort(liste)
        print(sortedliste)
 
 
def bubblesort(liste):
        for a in range(0, len(liste), 1):
                for i in range(0, len(liste)-a-1, 1):
                        value = liste[i]
                        nextvalue = liste[i+1] 
                        if liste[i]>liste[i+1]:
                                value = liste[i]
                                nextvalue = liste[i+1]
                                liste[i+1] = value
                                liste[i] = nextvalue
                               
        return (liste)
if __name__ == "__main__":
        main()
