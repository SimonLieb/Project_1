import matplotlib.pyplot as plt # type: ignore
from matplotlib.widgets import RadioButtons # type: ignore

# This method takes in a list and then a certain amount of L's and U's that it will make paths out of.
# For the first iteration of the method, two termporary paths will be added to the list, so:
#
# Before first iteration (With an empty list and l_count = 2, u_count = 2):
# paths_to_expand = [('',2,2)]
# After the first iteration:   
# Paths_to_expand = [('U',1,2),('L',2,1)]
# 
# The method will then pop the first path in the list and add two new combations UU and UL 
# (if there are enough remaining U's and L's). These will then be added to the end of the list 
# so the next paths that are created are LU and LL.
#
# Finally when both the remaining u's and l's are 0, this means that we have generated all possible
# permutations of that number of Ls and Us. All those permutations are added to the all_paths list,
# whose reference we passed in the method parameters.

def generate_combinations(u_count, l_count):
    all_paths = []
    paths_to_expand = [('', u_count, l_count)]
    
    while paths_to_expand:
        current_path, remaining_u, remaining_l = paths_to_expand.pop(0)
        
        if remaining_u == 0 and remaining_l == 0:
            all_paths.append(current_path)
        else:
            if remaining_u > 0:
                new_path = current_path + 'U'
                paths_to_expand.append((new_path, remaining_u - 1, remaining_l))
            
            if remaining_l > 0:
                new_path = current_path + 'L'
                paths_to_expand.append((new_path, remaining_u, remaining_l - 1))
    return all_paths

# Before the loop starts, an empty list `temp_list` is initialized to store paths that pass through the desired level.
# For each path in `all_paths`, the function checks if following that path will pass through the given `level`.
# For example, let's assume `start = (0, 0)` and `level = 2`.

# Before the first iteration (With an example path "ULUL" and start position (0,0)):
# current_y = start[1] = 0
# For each instruction in the path "ULUL":
# 
# 1. The first instruction is 'U', so current_y += 1:
#    current_y = 1
# 2. The next instruction is 'L', so current_y -= 1:
#    current_y = 0
# 3. The next instruction is 'U', so current_y += 1:
#    current_y = 1
# 4. The next instruction is 'L', so current_y -= 1:
#    current_y = 0
#
# Since `current_y` never reaches `level = 2`, this path is not added to `temp_list`.
# For this version of the method, the difference is then found between all_paths and the ones
# found since we want to find out which path do not cross the x axis.

def goesThroughY(all_paths, level):
    temp_list = []
    for path in all_paths:
        current_y = start[1] 
        for instruction in path:
            if instruction == "U":
                current_y += 1
            elif instruction == "L":
                current_y -= 1
            
            if current_y == level:
                temp_list.append(path)
                break

    return list(set(all_paths) - set(temp_list))

# Starting and ending points
start = (7, 6)
end = (20, 5)

# Calculate the total moves and breakdown into U and L moves
total_moves = end[0] - start[0]
u_moves = (end[1] - start[1] + total_moves) // 2
l_moves = total_moves - u_moves

# Generate all possible paths
all_possible_paths = generate_combinations(u_moves, l_moves)

# Filter paths that go through y = 0
filtered_paths = goesThroughY(all_possible_paths, 0)

print("\nAll the possible paths:")
# Print the paths for reference
for path in filtered_paths:
    print(path)

print("\nAmount of paths that never touch or cross the x-axis:")
print(len(filtered_paths))
input('\nPress any key to exit')