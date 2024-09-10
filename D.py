import matplotlib.pyplot as plt # type: ignore
from matplotlib.widgets import RadioButtons # type: ignore

def generate_combinations(u_count, l_count, current_path, all_paths):
    paths_to_expand = [(current_path, u_count, l_count)]
    
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
up_moves = (end[1] - start[1] + total_moves) // 2
left_moves = total_moves - up_moves

# Generate all possible paths
all_possible_paths = []
generate_combinations(up_moves, left_moves, '', all_possible_paths)

# Filter paths that go through y = 0
filtered_paths = goesThroughY(all_possible_paths, 0)

print("\nAll the possible paths:")
# Print the paths for reference
for path in filtered_paths:
    print(path)

print("\nAmount of paths that never touch or cross the x-axis:")
print(len(filtered_paths))
input('\nPress any key to exit')