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
    
    return temp_list 

# Starting and ending points
start = (0, 3)
end = (7, 2)

# Calculate the total moves and breakdown into U and L moves
total_moves = end[0] - start[0]
up_moves = (end[1] - start[1] + total_moves) // 2
left_moves = total_moves - up_moves

# Generate all possible paths
all_possible_paths = []
generate_combinations(up_moves, left_moves, '', all_possible_paths)

print("Amount of possible paths:")
print(len(all_possible_paths))
print("\nAll the possible combinations:")

# Print the paths for reference
for path in all_possible_paths:
    print(path)

input('\nPress any key to exit')