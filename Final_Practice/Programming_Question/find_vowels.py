name = input("enter the string --> ")
vowels_list = ['a','e','i','o','u']
for i in vowels_list:
    if i in name:
        print("{} vowel is present and count is {}".format(i,name.count(i)))

