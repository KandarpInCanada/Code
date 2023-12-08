def get_permutation(string_value):
    permutation = []
    if len(string_value) == 1:
        return [string_value]
    for i in range(0,len(string_value)):
        current_char = string_value[i]
        remain_character = string_value[:i] + string_value[i+1:]
        remaining_permute = get_permutation(remain_character)
        for j in remaining_permute:
            permutation.append(current_char + j)
    return permutation

string_value = input("enter the string --> ")
print(get_permutation(string_value))

