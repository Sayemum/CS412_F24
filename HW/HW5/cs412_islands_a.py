"""
    name: Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


def iterative(region, visited, x, y):
    count = 0
    stack = [(x, y)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        curr_x, curr_y = stack.pop()
        
        if visited[curr_x][curr_y]:
            continue
        
        visited[curr_x][curr_y] = True
        count += 1
        
        for dir_x, dir_y in directions:
            new_x = curr_x + dir_x
            new_y = curr_y + dir_y
            
            if (0 <= new_x < len(region)) and (0 <= new_y < len(region[0])) \
                and not visited[new_x][new_y] and region[new_x][new_y] == 1:
                    stack.append((new_x, new_y))
    
    return count


def main():
    # get input
    
    n = int(input())
    
    region = []
    for _ in range(n):
        line = input().split()
        
        row = [int(num) for num in line]
        region.append(row)
    
    # Init visited array
    visited = [[False] * n for _ in range(n)]
    largest_island = 0
    
    
    # Iterate each cell
    for i in range(n):
        for j in range(n):
            if region[i][j] == 1 and not visited[i][j]:
                island_size = iterative(region, visited, i, j)
                largest_island = max(largest_island, island_size)
    
    print(largest_island)


if __name__ == "__main__":
    main()
