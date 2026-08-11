"""
each command has a ..
- last_run_epoch
- curr_count

misc.
- no command will have same last_run epoch (by definition a single command can only be run at a time)

0 1 2 3 4 5
X . . X . .
. Y . . Y . 

0 1 2 3 4 5
X . . X . . 
. Y . .  . 

0 1 2 3 4 5 <- no
Y . . . . . 
. X . . X . 


- after every command run, records the last run epoch (last_run_epoc)
- if (now - last_run_epoch > n), a command can be run
- when multiple candidates..
    - largest curr_count
    - ! least last_run_epoch 

at epoch k
- X: 3
- Y: 3

curr_epoch = 0
while there commands left:
    curr_epoch += 1
    for each cooldown, if readcy than readd to pq

    cmd = command the largest curr count and THAT can be run!

    ... 

    cmd.curr_count -= 1
    if curr_count > 0:
        cmd.last_run_epoch = curr_epoch
        enqueue to colddown
    
    
curr_epoch = 5
X: 0, 1
Y: 1, 2

hq = [(curr_count, last_run_epoch, "X")]

X, Y, idle, X, Y

0 1 2 3 4 5
X . . X . .
. Y . . Y . 

"""
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = dict()
        for task in tasks:
            if task not in taskCounts:
                taskCounts[task] = 1
            else:
                taskCounts[task] += 1
        
        pq = [] # [(curr_count, task)]
        for task, count in taskCounts.items():
            heapq.heappush(pq, (-1 * count, task))

        cooldown = deque() # [(last run epoch, curr_count, task)]

        curr_epoch = 0
        while pq or cooldown:
            curr_epoch += 1

            while cooldown:
                last_run_epoch, curr_count, task = cooldown[0]
                if curr_epoch - last_run_epoch > n:
                    heapq.heappush(pq, (-1 * curr_count, task))
                    cooldown.popleft()
                else:
                    break
            
            if pq:
                curr_count, task = heapq.heappop(pq)
                curr_count *= -1
                if curr_count > 1:
                    cooldown.append((curr_epoch, curr_count - 1, task))

        return curr_epoch
