#Implementation of the earliest finish time first algorithm for the interval partitioning problem.
#Implementation based on pseudo code from lecture 2 slides.
from queue import PriorityQueue

#INPUT AND DATA STRUCTURE
n, k = map(int, input().split()) #n activities, k rooms

activities = []
for _ in range(n):
    (start_time, end_time) = map(int, input().split())
    activities.append((start_time, end_time))
activities.sort(key=lambda x: x[1])
print("activities: ")
print(activities)

classrooms = PriorityQueue(k) 
for i in range(k): 
    classrooms.put(activities[i][1])

#GREEDY ALGORITHM
scheduled = k
print("status PQ: ")
print(classrooms.queue)
for j in range(k, n):
    print("activity: ")
    print((activities[j][0], activities[j][1])) 
    if activities[j][0] >= classrooms.queue[0]: 
        classrooms.get() 
        classrooms.put(activities[j][1]) 
        scheduled += 1 
        print("chosen")
    print("status PQ: ")
    print(classrooms.queue) 

#OUTPUT
print("Number of activities: ")
print(scheduled)
