me_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# indexes:   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# reversed:-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print(f"{me_list[1] = }")           # = 2
print(f"{me_list[-1] = }")          # = 11
print(f"{me_list[0:6] = }")         # = [1, 2, 3, 4, 5, 6]
print(f"{me_list[-11:-5] = }")      # = [1, 2, 3, 4, 5, 6]

print(f"{me_list[3:7] = }")         # = [4, 5, 6, 7]
print(f"{me_list[-8:-4] = }")       # = [4, 5, 6, 7]

print(f"{me_list[1:11:2] = }")      # = [2, 4, 6, 8, 10]
print(f"{me_list[-10:-1:2] = }")    # = [2, 4, 6, 8, 10]

print(f"{me_list[-2:-11:-2] = }")   # = [10, 8, 6, 4, 2]
print(f"{me_list[9:1:-2] = }")      # = [10, 8, 6, 4, 2]

print(f"{me_list[11:6:-1] = }")     #  = [11, 10, 9, 8]
print(f"{me_list[-1:-5:-1] = }")    # = [11, 10, 9, 8]
print(f"{me_list[-1:6:-1] = }")     # = [11, 10, 9, 8]

print(f"{me_list[::-1] = }")        # = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

""" other """
list1 = [1, 2, 3, 4]
for list1[-2] in list1:
    print(list1[-2], end=" ")


#  string
# sample_url = 'https://softuni.bg'
# print(f"{sample_url = }")           # = 'https://softuni.bg'
#
# # reverced url
# print(f"{sample_url[::-1] =}")      # ='gb.inutfos//:sptth'
#
# # get the top level domain
# print(f"{sample_url[-3:] =}")       # ='.bg'
#
# # print url without https
# print(f"{sample_url[8:] =}")        # ='softuni.bg'
#
# # take the mane whithout http and top level domain
# print(f"{sample_url[8:-3] =}")      # ='softuni'
#
#  """funn string"""
# funn = "God saw I was dog"
#
# print(f"reverce {funn[::-1]}")
#
#
#
# # Извличане на domain
# # Проверка за протокола (http или https)
# sample_url = 'https://softuni.bg'
# protocol = 'https://' if sample_url.startswith('https') else 'http://'
# protocol_length = len(protocol)
#
# # Извличане на името на домейна
# domain_start = sample_url.find(protocol) + protocol_length if protocol in sample_url else 0
# domain_end = sample_url.find('.', domain_start)
#
# # Проверка за трибуквения домейн
# if sample_url[domain_end - 3] == '.':
#     domain_end -= 3  # премахвам и точката
# elif sample_url[domain_end - 4] == '.':
#     domain_end -= 4  # премахвам и точката
#
# domain = sample_url[domain_start:domain_end]
#
# print(f"{domain =}")
#
#
