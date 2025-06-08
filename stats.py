def get_num_words(text):
    return len(text.split())

def char_count(text):
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict

def sort_char_count(char_count_dict):
    new_list = []
    for key in char_count_dict:
       new_list.append({'char': key, 'num': char_count_dict[key]})
    new_list.sort(key=lambda x: x['num'], reverse=True)
    return new_list