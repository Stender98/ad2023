#Implementation of the earliest finish time first algorithm for the interval scheduling problem.
#Implementation based on pseudo code from lecture 2 slides.
#Suggestions from Copilot AI were used to improve the code and comments.

#INPUT AND DATA STRUCTURE
n = int(input())
jobs = []
for _ in range(n):
    (start_time, end_time) = map(int, input().split())
    jobs.append((start_time, end_time))
jobs.sort(key=lambda x: x[1])

#GREEDY ALGORITHM
chosen = []
chosen.append(jobs[0])
for i in range(1, n):
    if jobs[i][0] >= chosen[-1][1]:
        chosen.append(jobs[i])

#OUTPUT
print(len(chosen))