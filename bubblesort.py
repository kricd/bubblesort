#!/usr/bin/python

#
def main():
    liste = [9, 8, 7, 1, 4, 3, 2, 6, 5]
    print (liste)
    print(len(liste))
    newlist = []
    for i in range(0, len(liste)-1):
        tmp_i = i+1
        print(i)
        if liste[i] > liste[tmp_i]:
            newlist[i] = liste[tmp_i]
        else:
            newlist[i] = liste[i]

    print ("ERGEBNIS:")        
    for element in newlist:
        print (element)
    




if __name__ == "__main__":
    main()
