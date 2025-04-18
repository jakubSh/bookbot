def word_count(i):
    return len(i.split())

def char_count(i):
    char_dict = dict()
    text_list  = list(i)

    for char in text_list:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sorting(e):
    return e['count']

def dict_to_list(char_dict):
    chars_list = []

    for char, count in char_dict.items():
         chars_list.append({"char": char, "count": count})
    
    chars_list.sort(reverse=True, key=sorting)
    return chars_list