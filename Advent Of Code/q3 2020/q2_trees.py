def find_trees(grid, moves):
    trees = []
    for move in moves:
        trees.append(0)
        for i in range(0, len(grid), move[0]):
            row = i
            col = int((i/move[0])*move[1]) % len(grid[0])
            if grid[row][col] == "#":
                trees[-1] += 1
    return trees

def find_product(trees):
    if len(trees) == 0:
        return True
    if not find_product(trees[1:]):
        return find_product(trees[1:])
    return trees[0]*find_product(trees[1:])

with open("d3_input", "r") as f:
    grid = f.read().splitlines()

moves = [
    [1,1],
    [1,3],
    [1,5],
    [1,7],
    [2,1]
]
trees = find_trees(grid, moves)
print(find_product(trees))
