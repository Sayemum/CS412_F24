"""
    name:  Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


"""
PESUDO-CODE:
1. split the grid into 4 sub-grids
2. recursively go through each sub-grid to check if there's a removed tile already
"""

# def place_l_tile(grid, top_left, grid_size, remove_coords, tile_num):
def place_l_tile(grid, top_left, grid_size, missing_tile, tile_num):
    # BASE CASE (2x2 grid)
    if grid_size == 2:
        for row in range(top_left[0], top_left[0] + grid_size):
            for col in range(top_left[1], top_left[1] + grid_size):
                # print(row, col)
                # fill the 3 tiles that aren't the missing value
                if (row, col) != missing_tile:
                    grid[row][col] = tile_num
        return tile_num + 1
    
    # RECURSIVE
    mid = grid_size // 2
    centers = [
        (top_left[0] + mid - 1, top_left[1] + mid - 1),
        (top_left[0] + mid - 1, top_left[1] + mid),
        (top_left[0] + mid, top_left[1] + mid - 1),
        (top_left[0] + mid, top_left[1] + mid)
    ]
    
    if missing_tile[0] < top_left[0] + mid and missing_tile[1] < top_left[1] + mid:
        missing_quad = 0
    elif missing_tile[0] < top_left[0] + mid and missing_tile[1] >= top_left[1] + mid:
        missing_quad = 1
    elif missing_tile[0] >= top_left[0] + mid and missing_tile[1] < top_left[1] + mid:
        missing_quad = 2
    else:
        missing_quad = 3
    
    for i in range(4):
        if i != missing_quad:
            grid[centers[i][0]][centers[i][1]] = tile_num
    
    tile_num += 1
    
    quadrants = [
        (top_left, (mid, mid)),
        ((top_left[0], top_left[1] + mid), (mid, mid)),
        ((top_left[0] + mid, top_left[1]), (mid, mid)),
        ((top_left[0] + mid, top_left[1] + mid), (mid, mid))
    ]
    
    for i, (quad_top_left, _) in enumerate(quadrants):
        if i == missing_quad:
            quad_missing_tile = missing_tile
        else:
            quad_missing_tile = centers[i]
            
        tile_num = place_l_tile(grid, quad_top_left, mid, quad_missing_tile, tile_num)
        
    return tile_num
    
    # pass

def main():
    # get input
    # n = 3
    # remove_coords = (0, 0)
    n = int(input())
    remove_coords = tuple(map(int, input().split()))
    
    # print(n)
    # print(remove_coords)
    
    # create grid
    grid_size = 2 ** n
    grid = [[0] * grid_size for _ in range(grid_size)]
    # print("GRID SIZE", grid_size)
    
    # remove the tile at location
    grid[remove_coords[0]][remove_coords[1]] = -1
    # grid[0][6] = 10
    # grid[6][0] = 69
    # grid[6][6] = 42
    
    # place_l_tile(grid, (0, 0), grid_size, remove_coords, 1)
    place_l_tile(grid, (0, 0), grid_size, remove_coords, 0)
    
    # break down into 4 sides
    # mid_row = len(grid) // 2
    # mid_col = len(grid[0]) // 2
    # top_left_grid = grid[:divide][:divide]
    # top_left_grid = [row[:mid_col] for row in grid[:mid_row]]
    # top_right_grid = [row[mid_col:] for row in grid[:mid_row]]
    # bottom_left_grid = [row[:mid_col] for row in grid[mid_row:]]
    # bottom_right_grid = [row[mid_col:] for row in grid[mid_row:]]
    
    # place_l_tile(grid, grid_size)
    
    # print the grid
    for row in grid:
        print(" ".join(f"{num:02d}" for num in row))


if __name__ == "__main__":
    main()
