# There are 8 prison cells in a row, and each cell is either occupied or vacant.

# Each day, whether the cell is occupied or vacant changes according to the following rules:

#     If a cell has two adjacent neighbors that are both occupied or both vacant, 
#     then the cell becomes occupied.
#     Otherwise, it becomes vacant.

# (Note that because the prison is a row, the first and the last cells in the row 
# can't have two adjacent neighbors.)

# We describe the current state of the prison in the following way: cells[i] == 1 
# if the i-th cell is occupied, else cells[i] == 0.

# Given the initial state of the prison, return the state of the prison after N days 
# (and N such changes described above.)

# Example 1:

# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation: 
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

# Example 2:

# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0] 

# Note:

#     cells.length == 8
#     cells[i] is in {0, 1}
#     1 <= N <= 10^9

# =================================================================================

# NOT Accepeted in Leetcode 
# Failed with TIME LIMIT EXCEEDED - for Large inputs N = 1000000000

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        output = []
        output.append(0)
        j = 0
        while j < N:
            for i in range(1, len(cells)-1):
                if cells[i-1]==0 and cells[i+1]==0:
                    output.append(1)
                elif cells[i-1]==1 and cells[i+1]==1:
                    output.append(1)
                else:
                    output.append(0)
            
            output.append(0)
            cells = output
            temp = output
            output = []
            output.append(0)
            j+=1
        return temp
            

obj = Solution()
cells = [1,0,0,1,0,0,1,0]
N = 1000000000
print(obj.prisonAfterNDays(cells, N))

# ===============================================================================
# Accepted in Leetcode
# Approach :-
# We have only 2 bits (0,1)
# and if we have to make 3 digit number - then 2^3 combinations possible only
# So similarly , we have 8 digit number,
# out of which 1st and last will always be zero
# So we need to look between 1 to 6 i.e. 6 digit number
# So, 2^6 combinations possible i.e. 64  because
# Lets suppose input is [1,0,0,1,0,0,1,0]
# Leave 1st and last , so our string is
# [0,0,1,0,0,1] ==> at every place either 1 came or 0 came (so 2 possibilities)
# So, 2*2*2*2*2*2 = 64
# So even after N can be any Large Number, after some loop, we will get repetitions
# of sequence, So we need to take advantage of that
# and need to use hash-map

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        _map = {}
        self.cells = cells
        i = 0
        while i < N:
            s = str(self.cells)
            if s in _map:
                loop_length = i - _map[s]
                remaining_days = (N-i) % loop_length
                return self.prisonAfterNDays(self.cells, remaining_days)
            else:
                _map[s] = i
                prev = self.cells[0]
                for j in range(1,7):
                    curr, next = self.cells[j], self.cells[j+1]
                    self.cells[j] = 1 - (prev ^ next)
                    prev = curr
            self.cells[0] = 0
            self.cells[7] = 0
            i+=1
        return self.cells
                
obj = Solution()
cells = [1,0,0,1,0,0,1,0]
N = 1000000000
print(obj.prisonAfterNDays(cells, N))

# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

# ======================================================================================

# Accepetd in Leetcode
# In above explanation - we saw maximum 64 combinaton possible
# but in actual even 64 combination was not there
# because few combinations will be invalid (because of conditon), 
# so there will be only 14 combination
# example, lets take 3 digit number
# Below are various combinations
# 000 => invalid (because if adjacent cells are empty, middle should be occupied)
# 111
# 010
# 001
# etc
# So in this way only 14 combination possible
# if we create hash map - after 14 entries, entries will get repeated,
# So from there we got to know only 14 entries posisble
# and our answer will out of those 14 entries

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        _dict = {}
        i = 0
        while i <= 14:
            s = str(cells)
            _dict[i] = s
            prev = cells[0]
            for j in range(1, len(cells)-1):
                curr, _next = cells[j], cells[j+1]
                if prev==0 and _next==0:
                    cells[j] = 1
                elif prev==1 and _next==1:
                    cells[j] = 1
                else:
                    cells[j] = 0
                prev = curr
            cells[0] = 0
            cells[7] = 0
            i+=1
        
        if N%14==0:
            abc = ''.join(_dict[14])
            
        else:
            abc = ''.join(_dict[N%14])
            
        
        # As output is a list if numbers, not a string
        output = []
        for i in abc:
            if i in '01':
                output.append(int(i))
        return output

# ==============================================================================