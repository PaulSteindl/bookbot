def get_word_count(text):
    return len(text.split())

def get_character_count_dic(text):
    char_count_dic = {}
    for char in text:
        lower_char = char.lower()        
        if lower_char in char_count_dic:
            char_count_dic[lower_char] += 1
            continue
        char_count_dic[lower_char] = 1
    return char_count_dic
    
def sort_character_count_dic(dictornary):
    sortable_list = []
    for key in dictornary:
        char_dic = {}
        char_dic["char"] = key
        char_dic["num"] = dictornary[key]
        sortable_list.append(char_dic)

    sortable_list.sort(key=lambda d: d["num"], reverse=True)
    return sortable_list