def get_permutation(string_value):
    permutation = []
    if len(string_value) == 1:
        return [string_value]
    for i in range(0,len(string_value)):
        current_char = string_value[i]
        remain_char = string_value[:i] + string_value[i+1:]
        remain_permute = get_permutation(remain_char)
        for j in remain_permute:
            permutation.append(current_char+j)
    return permutation

def get_list_of_permutation(string_list):
    string_value = ''
    for i in range(0,len(string_list)):
        string_value = string_value + str(i)
    permutation = get_permutation(string_value)
    for i in permutation:
        li = []
        for j in i:
            li.append(string_list[int(j)])
        print(li)

string_value_list = ["kandarp","patel","sureshbhai"]
get_list_of_permutation(string_value_list)