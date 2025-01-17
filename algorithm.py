# lst = [4,2,8,6,1]
# minValue = lst[0]
# for i in lst:
#     if i < minValue:
#         minValue = i
# print(minValue)

# lst = [4, 2, 8, 6, 1]
# count = 0
# for i in lst:
#     if i % 2 == 0:
#         count += 1

# print(count)

# lst = [4, 2, 8, 6, 2]
# shufle = [0] * len(lst)
# for i in range(len(lst)):
#     shufle[(i + 1) % len(lst)] = lst[i]

# print(shufle)

# n = 64
# is_power_of_two = True
# while n> 1:
#     if n % 2 != 0:
#         is_power_of_two = False
#         break
#     n = n // 2

# print(is_power_of_two)

#algorithm to find the index of a target value in a sorted list
# lst = ['a', 'b', 'c', 'd', 'e']
# target = 'c'
# low, high = 0, len(lst) - 1
# found = False
# while low <= high:
#     mid = (low + high) // 2
#     if lst[mid] == target:
#         found = print("Found at index", mid)
#         break
#     elif lst[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1
# print(found)

# lst = [4, 2, 8, 6, 1]
# for i in range(len(lst)):
#     min_index = i
#     for j in range(i + 1, len(lst)):
#         if lst[j] < lst[min_index]:
#             min_index = j
#     lst[i], lst[min_index] = lst[min_index], lst[i]
# print(lst)

# lst = [4,2,8,6,1,4]
# unique_count = 0
# for i in range(len(lst)):
#     is_unique = True
#     for j in range(len(lst)):
#         if i != j and lst[i] == lst[j]:
#             is_unique = False
#             break
#     if is_unique:
#         unique_count += 1
# print(unique_count)

# a = input("Enter a number: ")
# count = 0
# for i in range(a +1):
#     count += i
# a = input("Enter a string: ")
# count = 0
# b = ['a', 'e', 'i', 'o', 'u']
# for i in a.lower():
#     for i in a:
#         if i in b:
#             count += 1
# print(count)

# a = int(input("Enter a 1 number: "))
# b = int(input("Enter a 2 number: "))
# sum = 0
# if a>b:
#     a, b = b, a
# for i in range(a, b + 1):  
#     sum += i
# print(sum)

# n = int(input("Enter a number: "))
# for i in range(1,11):
#     print(n * i)

# b = input("Enter a string: ")
# check = True
# for i in range(len(b)//2):
#     if b[i] != b[-(i+1)]:
#         check = False
#         break
# if check:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# def bubble(lst):
#     swap = True
#     while swap:
#         swap = False
#         for i in range(len(lst) - 1):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#                 swap = True
# nums = [4, 2, 8, 6, 1]
# bubble(nums)
# print(nums)

# def insertion(lst):
#     for i in range(1, len(lst)):
#         key = lst[i]
#         j = i - 1
#         while j >= 0 and key < lst[j]:
#             lst[j + 1] = lst[j]
#             j -= 1
#         lst[j + 1] = key
# nums = [4, 2, 8, 6, 1]
# insertion(nums)
# print(nums)

# def solution(lst):
#     for i in range(len(lst)):
#         index = i
#         j = i - 1
#         for j in range(i + 1, len(lst)):
#             if lst[j] < lst[index]:
#                 index = j
#         lst[i], lst[index] = lst[index], lst[i]

# nums = [4, 2, 8, 6, 1]
# solution(nums)
# print(nums)

# target = 10
# lst = [4, 2, 8, 6, 1]
# low, high = 0, len(lst) - 1
# found = False
# while low <= high:
#     mid = (low + high) // 2
#     if lst[mid] == target:
#         found = True
#         break
#     elif lst[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1
# print(found)

# def heapify(sort_nums, heap_size, root):
#     l = root
#     left = (2 * root) + 1
#     right = (2 * root) + 2
#     if left < heap_size and sort_nums[left] > sort_nums[l]:
#         l = left
#     if right < heap_size and sort_nums[right] > sort_nums[l]:
#         l = right
#     if l != root:
#         sort_nums[root], sort_nums[l] = sort_nums[l], sort_nums[root]
#         heapify(sort_nums, heap_size, l)

# def heap_sort(sort_nums):
#     size = len(sort_nums)
#     for i in range(size, -1, -1):
#         heapify(sort_nums, size, i)
#     for i in range(size - 1, 0, -1):
#         sort_nums[i], sort_nums[0] = sort_nums[0], sort_nums[i]
#         heapify(sort_nums, i, 0)

# nums = [4, 2, 8, 6, 1]
# heap_sort(nums)
# print(nums)

# a = input("Enter a 10 number: ")
# lst = []
# # lst =[5, 26,98 , 77, 3,2,7, 1, 0, 105]
# def bubble(lst):
#     swap = True
#     while swap:
#         swap = False
#         for i in range(len(lst) - 1):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#                 swap = True
# bubble(lst)
# print(lst)

