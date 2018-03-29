#!/usr/bin/python3
 
from __future__ import print_function
 
import random
 
def main():
        unsorted_list = []
        for x in range(0, 20):
                unsorted_list.append(random.randint(1, 100))
        sorted_list = bubblesort(unsorted_list)
        print(sorted_list)
 
 
def bubblesort(unsorted_list):
        for a in range(0, len(unsorted_list), 1):
                for i in range(0, len(unsorted_list)-a-1, 1):
                        value = unsorted_list[i]
                        nextvalue = unsorted_list[i+1] 
                        if unsorted_list[i]>unsorted_list[i+1]:
                                value = unsorted_list[i]
                                nextvalue = unsorted_list[i+1]
                                unsorted_list[i+1] = value
                                unsorted_list[i] = nextvalue
                               
        return (unsorted_list)

if __name__ == "__main__":
        main()
