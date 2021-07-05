def find_trees(grid):
    new_grid = " "
    trees = 0
    for i in range(len(grid)):
        col = (i*3) % len(grid[0])
        if grid[i][col] == "#":
            trees += 1
            new_grid += grid[i][:col] + "X" + grid[i][col+1:] + "\n"
        else:
            new_grid += grid[i][:col] + "O" + grid[i][col+1:] + "\n"
    return trees, new_grid.strip()

with open("d3_input", "r") as f:
    grid = f.read().splitlines()
    trees, grid = find_trees(grid)
    print(trees)
    print(grid)

