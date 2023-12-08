def check_all_substr(name_list,sub_str):
    for i in name_list:
        if sub_str not in i:
            return False
    return True

def get_longest_sub_str(name_list):
    first_str = name_list[0]
    max_str = ''
    for i in range(0,len(first_str)):
        current_str = ''
        for j in range(i+1,len(first_str)):
            sub_str = first_str[i:j+1]
            if check_all_substr(name_list,sub_str):
                current_str = sub_str
        if len(max_str) < len(current_str):
            max_str = current_str
    print(max_str)


name_list = ['kanffd','fdsfdkans','gdkansgafg','adfdafkan']
get_longest_sub_str(name_list)