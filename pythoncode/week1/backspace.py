from collections import deque
word = input().strip()
new_word = deque()   
for i in range(len(word)):
    if word[i] == "<":
        new_word.pop()
    else:
        new_word.append(word[i])
print("".join(new_word))