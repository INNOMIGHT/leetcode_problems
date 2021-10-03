def escape_from_jail(jump_height, slip, no_of_walls, wall_arr):
    i = 0
    jump_count = 0
    while i < len(wall_arr):
        if jump_height >= wall_arr[i]:
            i += 1
            jump_count += 1
        elif jump_height < wall_arr[i]:
            total_jump = 0
            while total_jump < wall_arr[i]:
                total_jump += jump_height - slip
                jump_count += 1
            i += 1
    return jump_count


print(escape_from_jail(10, 1, 2, [21]))
