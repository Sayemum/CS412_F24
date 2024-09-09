def place_l_tile(grid, top_left, grid_size, missing_tile, tile_num):
    # BASE CASE (2x2 grid)
    if grid_size == 2:
        for row in range(top_left[0], top_left[0] + grid_size):
            for col in range(top_left[1], top_left[1] + grid_size):
                if (row, col) != missing_tile:
                    grid[row][col] = tile_num
        return tile_num + 1
    
    # RECURSIVE CASE
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
        quad_missing_tile = missing_tile if i == missing_quad else centers[i]
        tile_num = place_l_tile(grid, quad_top_left, mid, quad_missing_tile, tile_num)
        
    return tile_num

def main():
    # Get input
    n = int(input())
    remove_coords = tuple(map(int, input().split()))
    
    # Create grid
    grid_size = 2 ** n
    grid = [[0] * grid_size for _ in range(grid_size)]
    
    # Remove the tile at location
    grid[remove_coords[0]][remove_coords[1]] = -1
    
    # Place L-tiles
    place_l_tile(grid, (0, 0), grid_size, remove_coords, 1)
    
    # Print the grid
    for row in grid:
        print(" ".join(f"{num:02d}" for num in row))

if __name__ == "__main__":
    main()
