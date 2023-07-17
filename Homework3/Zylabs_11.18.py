# ZyLabs 11.18
# Benjamin Ojode
# 1663352

new_list = input().split()

nums = [int(num) for num in new_list]

pos_nums = [num for num in nums if num >= 0]

sorted_nums = sorted(pos_nums)

output = ' '.join(str(num) for num in sorted_nums) + ' '

print(output, end='')