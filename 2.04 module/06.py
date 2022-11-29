list_nums = [1,2,3,0,4,77,2,3,0,2,0,3,0,5,0,7,0,1,0,0,1,0]
print("Изначальный список:", list_nums)

new_nums = [num for num in list_nums if num != 0]
print("Список в той же последовательности, но без нулей:", new_nums)

new_nums[len(new_nums):] = [0] * list_nums.count(0)
print("Список с 0 в конце:", new_nums)