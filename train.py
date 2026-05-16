# M-TASK (PYTHON)
# """
# Shunday function yozing, u string qabul qilsin va string palindrom yani togri oqilganda ham,
# orqasidan oqilganda ham bir hil oqiladigan soz ekanligini aniqlab boolean qiymat qaytarsin.
# MASALAN: palindrom_check("dad") return True;  palindrom_check("son") return False;
# """


# def palindrom_check(word):
#     reverse_word = word[::-1]
#     if word == reverse_word:
#         return True
#     return False


# print(palindrom_check("dam"))


# K-TASK
# '''Shunday function yozing, u string qabul qilsin va string ichidagi eng uzun sozni qaytarsin.
# MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan"'''


# def find_longest(word):
#     word_array = word.split()
#     longest = ''
#     for i in word_array:
#         if len(i) > len(longest):
#             longest = i
#     return longest


# print(find_longest("MyUzbekistan I come from Uzbekistan"))


# I-TASK
'''Shunday function tuzing, unga string argument pass bolsin. 
Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
MASALAN: get_digits("m14i1t") return qiladi "141"'''


# def get_digits(text):
#     new_string = ''
#     for i in text:
#         if i >= "0" and i <= "9":
#             new_string += i
#     return new_string


# print(get_digits("m14i1t"))

# G-TASK
'''
Shunday function tuzingki unga integerlardan iborat array pass bolsin va 
function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
'''


# def get_highest_index(array):
#     high_number = 0
#     high_ind = 0
#     for ind, val in enumerate(array):
#         if val > high_number:
#             high_number = val
#             high_ind = ind
#     return high_ind


# result = get_highest_index([58, 5, 21, 12, 21, 38, 8])
# print(result)
