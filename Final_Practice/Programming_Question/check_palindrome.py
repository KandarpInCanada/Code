name = input("enter the word --> ")
reverse_str = ''
for i in name:
    reverse_str = i + reverse_str
if name == reverse_str:
    print("{} is palindrome".format(name))
else:
    print("try next time")