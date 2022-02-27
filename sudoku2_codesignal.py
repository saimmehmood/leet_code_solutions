def solution(grid):
    
    grid_num_col = []
    grid_num_row = []
    sub_grid_row = []

    # checking for rows and columns
    for i in range(len(grid)):
        grid_num_row.append([x for x in grid[i] if x.isdigit()])
        grid_num_col.append([col[i] for col in grid if col[i].isdigit()])

    for i in range(len(grid_num_row)):
        if sorted(grid_num_row[i]) != sorted(list(set(grid_num_row[i]))):
            return False

    for i in range(len(grid_num_col)):
        if sorted(grid_num_col[i]) != sorted(list(set(grid_num_col[i]))):
            return False

    # generating sub grids
    arr = []
    arr2 = []
    arr3 = []
    j = 0
    sub_grids = []
    for i in range(len(grid)):

        arr.append(grid[i][0:3])
        arr2.append(grid[i][3:6])
        arr3.append(grid[i][6:9])
        j += 1

        if j == 3:
            j = 0
            x = []
            [x.extend(ele) for ele in arr]
            sub_grids.append(x)
            x = []
            [x.extend(ele) for ele in arr2]
            sub_grids.append(x)
            x = []
            [x.extend(ele) for ele in arr3]
            sub_grids.append(x)
            arr = []
            arr2 = []
            arr3 = []

    # checking for sub grids
    for i in range(len(sub_grids)):
        sub_grid_row.append([x for x in sub_grids[i] if x.isdigit()])

    for i in range(len(sub_grid_row)):
        if sorted(sub_grid_row[i]) != sorted((list(set(sub_grid_row[i])))):
            return False

    return True
