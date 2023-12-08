def get_permute(name):
    permutations = []
    if len(name) == 1:
        return [name]
    for i in range(0,len(name)):
        current_char = name[i]
        remain_character = name[:i] + name[i+1:]
        remaining_permute = get_permute(remain_character)
        for j in remaining_permute:
            permutations.append(current_char+j)
    return permutations

name = 'xyz'
print(get_permute(name))