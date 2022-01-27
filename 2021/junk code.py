def flash_lights(arr, x, y, coords_cache={}):
    result = 0
        
    # check all coords
    for x in range(arr.shape[0]):
        
        for y in range(arr.shape[1]):
            
            if (x, y) not in coords_cache:
                if arr[x, y] > 9:
                    print(f'{x},{y} flashes')
                    coords_cache[(x, y)] = arr[x, y]
                    result += 1
                    
                    # left
                    if x - 1 >= 0:
                        arr[x - 1, y] += 1
                        if (x - 1, y) not in coords_cache:
                            if arr[x - 1, y] > 9:
                                print(f'{x-1},{y} flashes recursively')
                                coords_cache[(x - 1, y)] = arr[x - 1, y]
                                result += flash_lights(arr, x - 1, y, coords_cache)
                    # right
                    if x + 1 <= len(arr[y]) - 1:
                        arr[x + 1, y] += 1
                        if (x + 1, y) not in coords_cache:
                            if arr[x + 1, y] > 9:
                                print(f'{x+1},{y} flashes recursively')
                                coords_cache[(x + 1, y)] = arr[x + 1, y]
                                result += flash_lights(arr, x + 1, y, coords_cache)
                    # down
                    if y - 1 >= 0:
                        arr[x, y - 1] += 1
                        if (x, y - 1) not in coords_cache:
                            if arr[x, y - 1] > 9:
                                print(f'{x},{y-1} flashes recursively')
                                coords_cache[(x, y - 1)] = arr[x, y - 1]
                                result += flash_lights(arr, x, y - 1, coords_cache)
                    # up
                    if y + 1 <= len(arr) - 1:
                        arr[x, y + 1] += 1
                        if (x, y + 1) not in coords_cache:
                            if arr[x, y + 1] > 9:
                                print(f'{x},{y+1} flashes recursively')
                                coords_cache[(x, y + 1)] = arr[x, y + 1]
                                result += flash_lights(arr, x, y + 1, coords_cache)
                    # left, up
                    if x - 1 >= 0 and y + 1 <= len(arr) - 1:
                        arr[x - 1, y + 1] += 1
                        if (x - 1, y + 1) not in coords_cache:
                            if arr[x - 1, y + 1] > 9:
                                print(f'{x-1},{y+1} flashes recursively')
                                coords_cache[(x - 1, y + 1)] = arr[x - 1, y + 1]
                                result += flash_lights(arr, x - 1, y + 1, coords_cache)
                    # right, up
                    if x + 1 <= len(arr[y]) - 1 and y + 1 <= len(arr) - 1:
                        arr[x + 1, y + 1] += 1
                        if (x + 1, y + 1) not in coords_cache:
                            if arr[x + 1, y + 1] > 9:
                                print(f'{x+1},{y+1} flashes recursively')
                                coords_cache[(x + 1, y + 1)] = arr[x + 1, y + 1]
                                result += flash_lights(arr, x + 1, y + 1, coords_cache)
                    # left, down
                    if x - 1 >= 0 and y - 1 >= 0:
                        arr[x - 1, y - 1] += 1
                        if (x - 1, y - 1) not in coords_cache:
                            if arr[x - 1, y - 1] > 9:
                                print(f'{x-1},{y-1} flashes recursively')
                                coords_cache[(x - 1, y - 1)] = arr[x - 1, y - 1]
                                result += flash_lights(arr, x - 1, y - 1, coords_cache)
                    # right, down
                    if x + 1 <= len(arr[y]) - 1 and y - 1 >= 0:
                        arr[x + 1, y - 1] += 1
                        if (x + 1, y - 1) not in coords_cache:
                            if arr[x + 1, y - 1] > 9:
                                print(f'{x+1},{y-1} flashes recursively')
                                coords_cache[(x + 1, y - 1)] = arr[x + 1, y - 11]
                                result += flash_lights(arr, x + 1, y - 1, coords_cache)
                    
    return result

def decode(binary_str, first_pass=True, length_id=1, length=1, type_id=1):
    print(f'{binary_str}, {length_id}, {length}')
    args = []
    if first_pass:
        _, type_id, increment = read_header(binary_str)
        binary_str = binary_str[increment:]
        length_id, length, increment = read_operator(binary_str)
        binary_str = binary_str[increment:]
    if length_id == '0':
        sub_string = binary_str[:length]
        binary_str = binary_str[length:]
        while sub_string:
            if '1' not in binary_str:
                break
            _, new_type_id, increment = read_header(sub_string)
            sub_string = sub_string[increment:]
            if new_type_id == 4:
                literal, increment = read_literal(sub_string)
                sub_string = sub_string[increment:]
                args.append(literal)
            else:
                length_id, length, increment = read_operator(sub_string)
                sub_string = sub_string[increment:]
                if not sub_string:
                    break
                result, new_str = decode(sub_string, False, length_id, length, new_type_id)
                sub_string = new_str
                args.append(result)
    elif length_id == '1':
        counter = 0
        while counter < length:
            if '1' not in binary_str:
                break
            _, new_type_id, increment = read_header(binary_str)
            binary_str = binary_str[increment:]
            if new_type_id == 4:
                literal, increment = read_literal(binary_str)
                binary_str = binary_str[increment:]
                args.append(literal)
                counter += 1
            else:
                counter += 1
                length_id, length, increment = read_operator(binary_str)
                binary_str = binary_str[increment:]
                result, new_str = decode(binary_str, False, length_id, length, new_type_id)
                binary_str = new_str
                args.append(result)
    print(args)
    args = apply_function(args, type_id)
    return args, binary_str