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
R = {} #rejecters
for _ in range(int(n/2)): #n/2 proposers
    names = input().split()
    P[names[0]] = deque(names[1:]) 
    P[names[0]].reverse() 
for _ in range(int(n/2)): #n/2 rejecters
    names = input().split()
    R[names[0]] = {} 
    for i in range(1, len(names)): 
        R[names[0]][names[i]] = i 

#test data structure on sample input
#print(P)
#{'Chandler': deque(['Phoebe', 'Rachel', 'Monica']), 'Joey': deque(['Monica', 'Phoebe', 'Rachel']), 'Ross': deque(['Phoebe', 'Rachel'])}
#We can find each proposers next choice in O(1) time with pop().
#print(R)
#{'Monica': {'Chandler': 1, 'Joey': 2}, 'Phoebe': {'Joey': 1, 'Ross': 2, 'Chandler': 3}, 'Rachel': {'Ross': 1, 'Joey': 2, 'Chandler': 3}}
#We can easily compare rejecters preferences for each proposer in O(1) time.

#Gale-shapley algorithm


#OUTPUT





        