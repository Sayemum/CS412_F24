"""
    name:  Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

def place_l_tile(grid, top_left, grid_size, missing_tile, tile_num):
    # BASE CASE (2x2 grid)
    if grid_size == 2:
        for row in range(top_left[0], top_left[0] + grid_size):
            for col in range(top_left[1], top_left[1] + grid_size):
                # fill the 3 tiles that aren't the missing tile
                if (row, col) != missing_tile:
                    grid[row][col] = tile_num
        return tile_num + 1
    
    # RECURSIVE
    # get middle coords of all 4 subgrids
    mid = grid_size // 2
    center_coords = [
        (top_left[0] + mid - 1, top_left[1] + mid - 1),
        (top_left[0] + mid - 1, top_left[1] + mid),
        (top_left[0] + mid, top_left[1] + mid - 1),
        (top_left[0] + mid, top_left[1] + mid)
    ]
    
    # determine which subgrid has the original missing tile
    missing_subgrid = 0
    if missing_tile[0] < top_left[0] + mid and missing_tile[1] >= top_left[1] + mid:
        missing_subgrid = 1
    elif missing_tile[0] >= top_left[0] + mid and missing_tile[1] < top_left[1] + mid:
        missing_subgrid = 2
    elif missing_tile[0] >= top_left[0] + mid and missing_tile[1] >= top_left[1] + mid:
        missing_subgrid = 3
    
    # remove center tile from all other subgrids
    # that aren't missing a tile already
    for i in range(4):
        if i != missing_subgrid:
            grid[center_coords[i][0]][center_coords[i][1]] = tile_num
    
    tile_num += 1
    
    # define each quadrant's top-left corner coords
    quadrant_coords = [
        (top_left[0], top_left[1]),
        (top_left[0], top_left[1] + mid),
        (top_left[0] + mid, top_left[1]),
        (top_left[0] + mid, top_left[1] + mid)
    ]
    
    # recurse through each quadrant
    for i, quad_top_left in enumerate(quadrant_coords):
        if i == missing_subgrid:
            quad_missing_tile = missing_tile
        else:
            quad_missing_tile = center_coords[i]
        
        tile_num = place_l_tile(grid, quad_top_left, mid, quad_missing_tile, tile_num)
    
    return tile_num


def main():
    # get input
    # n = 3
    # remove_coords = (0, 0)
    n = int(input())
    remove_coords = tuple(map(int, input().split()))
    
    # create grid
    grid_size = 2 ** n
    grid = [[0] * grid_size for _ in range(grid_size)]
    
    # remove the tile at location
    grid[remove_coords[0]][remove_coords[1]] = -1
    
    # recursive function
    place_l_tile(grid, (0, 0), grid_size, remove_coords, 0)
    
    # print the grid
    for row in grid:
        print(" ".join(f"{num:02d}" for num in row))


if __name__ == "__main__":
    main()
