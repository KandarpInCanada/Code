def check_substr_in_all(list1,substr):
    for i in list1:
        if substr not in i:
            return False
    return True

def get_longest_substr(list1):
    sample_str = string_list[0]
    maximum_substr = ''
    for i in range(0,len(sample_str)):
        current_sub_str = ''
        for j in range(i+1,len(sample_str)):
            sub_str = sample_str[i:j+1]
            if check_substr_in_all(list1,sub_str):
                current_sub_str = sub_str
        if len(maximum_substr) < len(current_sub_str):
            maximum_substr = current_sub_str
    return maximum_substr

string_list = ["kandarrrrrp","kandarrrrrrtrt","asakandarrgfg","fhdfjkandarr"]
print("maximum substr in the list id {}".format(get_longest_substr(string_list)))
