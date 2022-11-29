def is_palindrome(nums_list):
    reverse_list = []
    for i_num in range(len(nums_list) - 1, -1, -1):
        reverse_list.append(nums_list[i_num])
        print(nums_list, "в цикле нею нам")
        print(reverse_list, "в цикле реверс лист")
    if nums_list == reverse_list:
        return True
    else:
        return False
nums = []
how_many = int(input("Сколько будет чисел? "))
for i_input in range(how_many):
    number_input = int(input(f"Число {i_input + 1}: "))
    nums.append(number_input)
new_nums = []
answer = []
for i_nums in range(0, len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

print("Последовательность:", nums)
print("Нужно приписать чисел:", len(answer))
print("Сами числа", answer)