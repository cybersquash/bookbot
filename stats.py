def get_num_words(string):
    words = string.split()
    word_count = len(words)
    return word_count

def get_num_char_count(string):
    dictionary = {}
    for i in string:
        char = i.lower()
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

def sort_on(items):
    return items["num"]

def sort_char_list(dic):
    dic_list = []
    for key in dic:
        d = {}
        d["char"] = key
        d["num"] = dic[key]
        dic_list.append(d)
    dic_list.sort(reverse=True, key=sort_on)
    return dic_list

