# using the below list, print out the following sentences
# 1. print " the sky"
# 2. create a sentence "The stars are shining" by picking and combining items from grid and manually adding "are"


grid = [
    ["The", "Sky", "is"],
    ["full", "of", "stars"],
    ["shining", "bright", "tonight"]
]

print(grid[0][0] + " " + grid[0][1])
print(grid[0][0] + " " + grid[1][2] + " " + "are " + grid[2][0])
print(grid[1][::-1])

