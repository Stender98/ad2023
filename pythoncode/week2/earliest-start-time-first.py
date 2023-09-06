#Implementation of the earliest finish time first algorithm for the interval partitioning problem.
#Implementation based on pseudo code from lecture 2 slides.
from queue import PriorityQueue

#INPUT AND DATA STRUCTURE
n, k = map(int, input().split()) #n activities, k rooms

activities = []
for _ in range(n):
    (start_time, end_time) = map(int, input().split())
    activities.append((start_time, end_time))
activities.sort(key=lambda x: x[0])

classrooms = PriorityQueue(k) 
for _ in range(k-1): 
    classrooms.put(0) 
classrooms.put(activities[0][1])

#GREEDY ALGORITHM
scheduled = 1
#print("status PQ: ")
#print(classrooms.queue)
for i in range(1, n):
    #print("activity: ")
    #print((activities[i][0], activities[i][1])) 
    if activities[i][0] >= classrooms.queue[0]: 
        classrooms.get() 
        classrooms.put(activities[i][1]) 
        scheduled += 1 
        #print("chosen")
    #print("status PQ: ")
    #print(classrooms.queue) 

#OUTPUT
#print("Number of activities: ")
print(scheduled)
