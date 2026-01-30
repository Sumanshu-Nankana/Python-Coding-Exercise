# https://www.techgig.com/challenge/prime-code-champ-june-17
"""
Game Center (100 Marks)
You and your friend go to a game arcade where you choose to play the game Lucky Pick.
In the game, there is a square grid and on each block, some money is placed on it.
When a player chooses a block, the machine randomly chooses a block from the neighboring
ones and the chosen block (consider 8 neighborhood). The player is awarded the money that
is placed on the block that the machine selects. Your friend needs help choosing the block.

Your job is to return the block position(s) that will maximize the minimum amount your
friend will win for sure. If there are more than one such block positions then the output
must return for all these positions.

Input Format
You will be given the Grid Description as -
The first line consists of the size of the square grid (N)
The next N lines each containing N numbers separated by '#', each number representing
the amount of money put on that block


Constraints
1 < N < 500

Output Format
You need to print the array of string containing the position(s)
of a block choosing which will give the maximum amount of money which your friend will definitely win.

Sample TestCase 1
Input
3
12#45#33
94#54#23
98#59#27
Output
3#1
Explanation
In the above example, if he selects the block (3,1), then under the best case,
he could win is 98 and under the worst case the maximum he could win is 54.
In such scenario, the worst case of block (3,1) gives your friend more money than
the worst case of other blocks.

Sample TestCase 2
Input
4
12#45#33#27
94#54#23#53
98#59#27#62
11#51#67#13
Output
1#3
1#4
2#3
2#4
Explanation

Note: If the output array contains multiple strings(block's positions),
all the positions must be in the row-wise traversal order. In Example 2,
the output is {1#3,1#4,2#3,2#4}. If your function is returning an array that has
same elements (block's position) but in the different order, then the output array will be incorrect.
"""


def main():
    n = int(input())
    grid = []
    for i in range(n):
        row = list(map(int, input().strip().split('#')))
        grid.append(row)

    winners = []
    best_guarantee = -float('inf')

    # Iterate through every cell
    for r in range(n):
        for c in range(n):
            pool = [grid[r][c]]

            # Top Row
            if r - 1 >= 0:
                pool.append(grid[r - 1][c])

            # Top-Left
            if r - 1 >= 0 and c - 1 >= 0:
                pool.append(grid[r - 1][c - 1])

            # Top-Right
            if r - 1 >= 0 and c + 1 < n:
                pool.append(grid[r - 1][c + 1])

            # Left
            if c - 1 >= 0:
                pool.append(grid[r][c - 1])

            # Right
            if c + 1 < n:
                pool.append(grid[r][c + 1])

            # Bottom Row
            if r + 1 < n:
                pool.append(grid[r + 1][c])

            # Bottom-Left
            if r + 1 < n and c - 1 >= 0:
                pool.append(grid[r + 1][c - 1])

            # Bottom-Right
            if r + 1 < n and c + 1 < n:
                pool.append(grid[r + 1][c + 1])

            # Find the minimym value in this specific zone
            current_min = min(pool)

            if current_min > best_guarantee:
                best_guarantee = current_min
                winners = [f"{r + 1}#{c + 1}"]
            elif current_min == best_guarantee:
                winners.append(f"{r + 1}#{c + 1}")

    for pos in winners:
        print(pos)


main()

## Little more compacted approach and without using pool to store values

def main():
    n = int(input())
    grid = []
    for i in range(n):
        row = list(map(int, input().strip().split('#')))
        grid.append(row)

    winners = []
    best_guarantee = -float('inf')

    # Neighbor offsets (8 Directions)
    neighbor_offset = [(-1, 0), (-1, -1), (-1, 1),  # Top Row, Top-Left, Top-Right
                       (0, -1), (0, 1), # Left and Right
                       (1, 0), (1, -1), (1, 1) # Bottom Row, Bottom-Left, Bottom-Right
                      ]
    # Iterate through every cell
    for r in range(n):
        for c in range(n):
            current_min = [grid[r][c]]

            for dr, dc in neighbor_offset:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    val = grid[nr][nc]
                    if val < current_min:
                        current_min = val

                    # if the zone's minimum is worse than the best we have found
                    # elsewhere, then stop checking that cell Neighbors
                    if current_min < best_guarantee:
                        break

            if current_min > best_guarantee:
                best_guarantee = current_min
                winners = [f"{r + 1}#{c + 1}"]
            elif current_min == best_guarantee:
                winners.append(f"{r + 1}#{c + 1}")

    for pos in winners:
        print(pos)


main()