from collections import deque

#This is a solution to StablePerfectMatching
# using deque as a stack and inverse preference lists.
#This should help us achieve a O(n^2) time complexity for 
# the Gale-Shapley alogrithm which will help us solve the matching problem.
#Data structures chosen based on Thore Husfeldt's suggestion in lecture 1
#Code and comments written with suggestions from Copilot AI

#INPUT
n, m = map(int, input().split())
P = {} #proposers
R = {} #rejectors
for _ in range(int(n/2)): #n/2 proposers
    names = input().split()
    P[names[0]] = deque(names[1:]) 
    P[names[0]].reverse() 
for _ in range(int(n/2)): #n/2 rejectors
    names = input().split()
    R[names[0]] = {} 
    for i in range(1, len(names)): 
        R[names[0]][names[i]] = i 

#test data structure
#print(P)
#print(R)

#Gale-shapley algorithm execution


#OUTPUT





        