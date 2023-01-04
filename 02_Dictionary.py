# 01_Python program to find the sum of all items in a dictionary

def sum_dict(dict_1):
    val_lst = list(dict_1.values())
    return sum(val_lst)


# print((sum_dict({'a': 100, 'b': 200, 'c': 300})))

# 02_Program to create grade calculator in Python

jack = {"name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
        }
james = {"name": "James Potter",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "lab": [67.90, 78.72]
         }
dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 23, 39],
         "test": [78, 77],
         "lab": [80, 80]
         }
jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
        }
tom = {"name": "Tom Hanks",
       "assignment": [29, 89, 60, 56],
       "test": [65, 56],
       "lab": [50, 40.6]
       }
student_info = [jack, james, dylan, jess, tom]


def avg_marks(student):
    assignment = sum(student["assignment"]) / len(student["assignment"]) * 0.1
    test = sum(student["test"]) / len(student["test"]) * 0.7
    lab = sum(student["lab"]) / len(student["lab"]) * 0.2
    return sum([assignment, test, lab])


student_score = []
for name in student_info:
    student_score.append(avg_marks(name))


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"


# for ele in range(len(student_score)):
#     print(student_info[ele]["name"])
#     print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
#     print(f"Average mark of {student_info[ele]['''name''']} is: {student_score[ele]}")
#     print(f"Letter grade of {student_info[ele]['''name''']} is: {grade(student_score[ele])} \n")

# 03_Python – Insertion at the beginning in OrderedDict

def insertion(dict_2, item):
    key_lst = list(dict_2.keys())
    val_lst = list(dict_2.values())
    dict_lst = list(zip(key_lst, val_lst))
    dict_lst.insert(0, item)
    return dict_lst


# print(insertion({'a': 1, 'b': 2}, ('c', 3)))

# 04_Dictionary and counter in Python to find winner of election
'''
    Given an array of names of candidates in an election. 
    A candidate name in the array represents a vote cast to the candidate. 
    Print the name of candidates received Max vote. 
    If there is tie, print a lexicographically smaller name.
'''


def count_func(str_lst):
    from collections import Counter
    freq_list = []
    for names in str_lst:
        freq_list.append(str_lst.count(names))
    max_vote = max(freq_list)
    str_lst = dict(Counter(str_lst))
    name_list = []
    for key, val in str_lst.items():
        if val == max_vote:
            name_list.append(key)
    return min(name_list, key=len)


# print(count_func(['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie', 'jamie', 'jamie',
#                   'john', 'johnny', 'jamie', 'johnny',
#                   'john']))


# 05_Key with maximum unique values

def max_unique_val(dict_3):
    max_val = 0
    max_key = None
    for key, val in dict_3.items():
        if len(set(val)) > max_val:
            max_val = len(set(val))
            max_key = key
    return max_key


# print(max_unique_val({"Gfg": [5, 7, 5, 4, 5], "is": [6, 7, 4, 3, 3], "Best": [9, 9, 6, 5, 5]}))

# 06_Find all duplicate characters in string

def dup_str(str_var):
    input_lst = [str_var[i] for i in range(len(str_var))]
    dup_lst = []
    new_lst = []
    for i in input_lst:
        if i not in new_lst:
            new_lst.append(i)
        else:
            dup_lst.append(i)
    return list(dict.fromkeys(dup_lst).keys())


# print(dup_str("geeksforgeeeks"))

# 07_Group Similar items to Dictionary Values List

def group_similar(test_list):
    from collections import Counter

    test_dict = dict(Counter(test_list))

    for val in test_dict:
        test_dict[val] = [val for i in range(test_dict[val])]
    return test_dict


# print(group_similar([4, 6, 6, 4, 2, 2, 4, 8, 5, 8]))

# 08_K’th Non-repeating Character in Python

def non_repeating_char(str_var1, k):
    freq_lst = []
    for i in range(len(str_var1)):
        if str_var1.count(str_var1[i]) == 1:
            freq_lst.append(str_var1[i])

    if len(freq_lst) < k:
        return f"Less than {k} non-repeating characters in input"
    else:
        return freq_lst[k - 1]


# print(non_repeating_char("geeksforgeeks", 3))

# 09_Replace words from Dictionary

def repl_word(test_str, lookp_dict):
    test_lst = test_str.split()
    new_repl_lst = []
    for ele in test_lst:
        if ele in lookp_dict:
            new_repl_lst.append(lookp_dict[ele])
        else:
            new_repl_lst.append(ele)
    new_repl_lst = " ".join(new_repl_lst)
    return new_repl_lst


# print(repl_word('geekforgeeks best for geeks', {"best": "good and better", "geeks": "all CS aspirants"}))

# 10_Remove Dictionary Keywords

def rmv_from_str(test_str, test_dict):
    test_str = 'gfg is best for geeks'
    test_dict = {'geeks': 1, 'best': 6}
    test_lst = test_str.split()

    for ele in test_lst:
        if ele in test_dict:
            test_lst.remove(ele)
        else:
            pass
    return test_lst


# print('gfg is best for geeks', {'geeks': 1, 'best': 6})

# 11_Remove all duplicates words from a given sentence

def rmv_all_dup(str1):
    str_lst = str1.split()
    str_dict = dict.fromkeys(str_lst)
    return " ".join(list(str_dict.keys()))


# print(rmv_all_dup("Python is great and Java is also great"))

# 12_Remove duplicate values across Dictionary Values

def rmv_dup_across(test_dict):
    key_lst = list(test_dict.keys())
    val_lst = list(test_dict.values())
    new_list = []
    for elem in val_lst:
        for j in elem:
            new_list.append(j)
    list_2 = []
    for elem in val_lst:
        list_1 = []
        for j in elem:
            if new_list.count(j) == 1:
                list_1.append(j)
        list_2.append(list_1)
    return dict(list(zip(key_lst, list_2)))


# print(rmv_dup_across({'Manjeet': [1, 4, 5, 6], 'Akash': [1, 8, 9], 'Nikhil': [10, 22, 4],
#                       'Akshat': [5, 11, 22]}))

# 13_Python Dictionary to find mirror characters in a string

def mirror_char(input_word, n):
    str_alphabet = "abcdefghijklmnopqrstuvwxyz"
    rev_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    new_word = input_word[:(n - 1)]
    for i in range(n - 1, len(input_word)):
        new_word += rev_alphabet[str_alphabet.index(input_word[i])]
    return new_word


# print(mirror_char("paradox", 3))

# Counting the frequencies in a list using dictionary in Python

def count_freq(inp_list):
    count_list = list(dict.fromkeys(inp_list).keys())
    freq_list = []
    for i in count_list:
        freq_list.append(inp_list.count(i))

    return dict(list(zip(count_list, freq_list)))


print(count_freq([1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]))
