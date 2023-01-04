# reversed lists
list_rev = [100, 200, 300, 400, 500]
# print(list(reversed(list_rev)))

# Concatenate two lists index-wise
list_1 = ["M", "na", "i", "Ke", "woo"]
list_2 = ["y", "me", "s", "lly"]
new_list = []
for i, j in zip(list_1, list_2):
    new_list.append(i + j)
# print(new_list)

# Turn every item of a list into its square
num_list = [1, 2, 3, 4, 5, 6, 7]
sqr_list = [i ** 2 for i in num_list]
# print(sqr_list)

# Concatenate two lists in the following order
l1 = ["Hello ", "take "]
l2 = ["Dear", "Sir"]
l3 = []
for i in range(len(l1)):
    for j in range(len(l2)):
        l3.append(l1[i] + l2[j])
# print(l3)

# Iterate both lists simultaneously
num_1 = [10, 20, 30, 40]
num_2 = [100, 200, 300, 400]

# for i, j in zip(num_1, reversed(num_2)):
#     print(i,j)

# Remove empty strings from the list of strings
str_list = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for i in str_list:
    if i == "":
        str_list.remove(i)
# print(str_list)

# Add new item to list after a specified item
sp_list = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
sp_list[2][2].append(7000)
# print(sp_list)

# Extend nested list by adding the sublist
ex_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
ex_list[2][1][2].extend(sub_list)
# print(ex_list)

# Replace list’s item with new value if found
n1 = [5, 10, 15, 20, 25, 50, 20]
n1[n1.index(20)] = 200
# print(n1)

# Remove all occurrences of a specific item from a list
list_a = [5, 10, 15, 20, 25, 50, 20]
for i in list_a:
    if i == 20:
        list_a.remove(20)


# print(list_a)


# swap first and last element of the list.

def swap_func(n_list):
    val = n_list[0]
    n_list[0] = n_list[len(n_list) - 1]
    n_list[len(n_list) - 1] = val

    return n_list


# print(swap_func([12, 35, 9, 56, 24]))

'''Given a list in Python and provided the positions of the elements, 
write a program to swap the two elements in the list.'''


def new_swap_func(in_list, pos_1, pos_2):
    val_1 = in_list[pos_1 - 1]
    in_list[pos_1 - 1] = in_list[pos_2 - 1]
    in_list[pos_2 - 1] = val_1
    return in_list


# print(new_swap_func([1, 2, 3, 4, 5], 1, 3))


# Check if element exists in list in Python
def check_list(in_list1, val):
    if val in in_list1:
        return True
    else:
        return False


# print(check_list([3, 4, 6, 7, 1, 3, 4, 9, 7, 5], 3))


# Given a list in Python and a number x, count the number of occurrences of x in the given list.
def count_occurrences(list_a1, x):
    count = 0
    for n in list_a1:
        if n == x:
            count = count + 1
        else:
            pass
    return count


# print(count_occurrences([15, 6, 7, 10, 12, 20, 10, 28, 10], 10))


# Find sum and average of List in Python
def avg_sum(list_b):
    x = 0
    for n in range(len(list_b)):
        x = x + list_b[n]
    avg = x / len(list_b)
    return x, avg


# print(avg_sum([4, 5, 1, 2, 9, 7, 10, 8]))


# Sum of number digits in List
def sum_digit(list_c):
    digit_list = []
    for n in list_c:
        x = 0
        for m in str(n):
            x = x + int(m)
        digit_list.append(x)

    return digit_list


# print(sum_digit([12, 67, 98, 34]))


# Multiply all numbers in the list
def mul_digit(list_d):
    x = 1
    for n in list_d:
        x = x * n
    return x


# print(mul_digit([1, 2, 3]))


# Python program to find the smallest number in a list
def smallest_digit(list_e):
    list_e1 = sorted(list_e)
    return list_e1[0]


# print(smallest_digit([10, 20, 4]))


# Python program to find the largest number in a list
def largest_digit(list_f):
    list_f1 = sorted(list_f)
    list_f1.reverse()
    return list_f1[0]


# print(largest_digit([10, 20, 4]))

# Python program to find second-largest number in a list
def sec_largest_digit(list_e):
    list_e1 = sorted(list_e)
    list_e1.reverse()
    return list_e1[1]


# print(sec_largest_digit([70, 11, 20, 4, 100]))

# Python program to print even numbers in a list

def even_digit(list_g):
    list_g1 = []
    for n in list_g:
        if n % 2 == 0:
            list_g1.append(n)
        else:
            pass
    return list_g1


# print(even_digit([2, 7, 5, 64, 14]))

# Python program to print odd numbers in a List
def odd_digit(list_h):
    list_h1 = []
    for n in list_h:
        if n % 2 != 0:
            list_h1.append(n)
        else:
            pass
    return list_h1


# print(odd_digit([12, 14, 95, 3, 73]))

# Python program to print all even numbers in a range

def even_num_range(st_1, st_2):
    for n in range(st_1, st_2 + 1):
        if n % 2 == 0:
            print(n, end=" ")
        else:
            pass


# even_num_range(5, 26)

# Python program to print all odd numbers in a range

def odd_num_range(st_1, st_2):
    for n in range(st_1, st_2 + 1):
        if n % 2 != 0:
            print(n, end=" ")
        else:
            pass


# odd_num_range(5, 26)

# Python program to count Even and Odd numbers in a List

def count_evn_odd(list_i):
    x = 0
    y = 0
    for n in list_i:
        if n % 2 == 0:
            x = x + 1
        else:
            y = y + 1
    return f"Even = {x} , Odd = {y}"


# print(count_evn_odd([2, 7, 5, 64, 14]))

# Python program to print positive numbers in a list

def positive_num(list_j):
    list_j1 = []
    for n in list_j:
        if n > 0:
            list_j1.append(n)
        else:
            pass
    return list_j1


# print(positive_num([12, -7, 5, 64, -14]))

# Python program to print negative numbers in a list

def negative_num(list_k):
    list_k1 = []
    for n in list_k:
        if n < 0:
            list_k1.append(n)
        else:
            pass
    return list_k1


# print(negative_num([12, -7, 5, 64, -14]))


# Python program to count positive and negative numbers in a list

def count_negative_positive(list_l):
    x = 0
    y = 0
    for n in list_l:
        if n > 0:
            x += 1
        else:
            y += 1
    return f"Positive = {x} , Negative = {y}"


# print(count_negative_positive([2, -7, 5, -64, -14]))

# Remove multiple elements from a list in Python

def rmv_mul_elements(list_m, rmv_list):
    for m in rmv_list:
        list_m.remove(m)

    return f"Remove = {rmv_list} , New_list = {list_m}"


# print(rmv_mul_elements([12, 15, 3, 10], [12, 3]))

# Remove empty tuples from a list
def rmv_empty_tuple(list_n):
    for tuples in list_n:
        if len(tuples) == 0:
            list_n.remove(tuples)
        else:
            pass
    return list_n


# print(rmv_empty_tuple([(), ("ram", "15", "8"), (), ("laxman", "sita"), ("krishna", "akbar", "45"), ()]))

# Program to print duplicates from a list of integers

def rmv_duplicates(list_o):
    d = list(dict.fromkeys(list_o))
    return d


# print(rmv_duplicates([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]))

# Python – Remove empty List from List

def rmv_empty_list(list_p):
    for n in list_p:
        if [] in list_p:
            list_p.remove([])
        else:
            pass
    return list_p


# print(rmv_empty_list([5, 6, [], 3, [], [], 9]))


# Convert List to List of dictionaries

def list_of_dict(list_q, key_lst):
    len_1 = int(len(list_q) / len(key_lst))
    lst = []
    for k in range(len_1):
        lst.append(dict.fromkeys(key_lst))

    # out_put = [list_q[i:i + len(key_lst)] for i in range(0, len(list_q), len(key_lst))]
    out_put = []
    for m in range(0, len(list_q), len(key_lst)):
        out_put.append(list_q[m:m + len(key_lst)])

    new_1 = []
    for n in range(len(lst)):
        new_1.append(dict(zip(list(lst[n].keys()), out_put[n])))
    return new_1


# print(list_of_dict(['Gfg', 3, 'is', 8, "fgf", 5, "hjk", 6], ['name', 'id']))


# Pair elements with Rear element in Matrix Row

def pair_elem(lst_r):
    new_lst = []
    for ele in lst_r:
        lst = []
        for ele_1 in range(len(ele) - 1):
            lst.append([ele[ele_1], ele[-1]])
        new_lst.append(lst)
    return new_lst


# print(pair_elem([[4, 5, 6], [2, 4, 5], [6, 7, 5]]))

# How to count unique values inside a list
def count_unique(lst_s):
    lst_s = dict.fromkeys(lst_s).keys()
    return len(lst_s)


# print(count_unique([1, 2, 2, 5, 8, 4, 4, 8]))

# List product excluding duplicates

def list_product(lst_t):
    lst_t = list(dict.fromkeys(lst_t).keys())
    x = 1
    for ele in lst_t:
        x = ele * x
    return x


# print(list_product([1, 3, 5, 6, 3, 5, 6, 1]))

# Extract elements with Frequency greater than K

def ele_sp_freq(lst_u, k):
    freq_ele = []
    for ele in lst_u:
        freq = lst_u.count(ele)
        if freq > k and ele not in freq_ele:
            freq_ele.append(ele)
    return freq_ele


# print(ele_sp_freq([4, 6, 4, 3, 3, 4, 3, 7, 8, 8], 2))

# Python program to check if the list contains three consecutive common numbers in Python
def common_num_list(lst_v):
    rsv = []
    for ele in lst_v:
        freq = lst_v.count(ele)
        if freq == 3:
            rsv.append(ele)
    return list(dict.fromkeys(rsv).keys())


# print(common_num_list([1, 1, 1, 64, 23, 64, 22, 22, 22]))
