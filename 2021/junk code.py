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