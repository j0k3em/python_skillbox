nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [nice_list[i][k][j] for i in range(0, 2) 
    for k in range(0, 3) 
        for j in range(0, 3)]
print(new_list)