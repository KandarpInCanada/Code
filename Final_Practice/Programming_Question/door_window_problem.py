door = []
window = []
door_opening_time = 60
window_opening_time =50

for i in range(0,6):
    door.append(False)
    window.append(False)
total_time = 0
while True:
    answer = input("Do you want to continue Y/N --> ")
    if answer.lower() == 'n':
        print("Bye Bye ...... Total Time {}".format(total_time))
        break
    print("Okay let move forward ")
    print("Door Status {}".format(door))
    print("Window status {}".format(window))
    print("What further action do you want ")
    action = input("Enter in this formate [Entity Action SerialNumber] --> ")
    list1 = action.split(" ")
    if str(list1[0]).lower() == 'door':
        print(str(list[1]).lower())
        if str(list1[1]).lower() == 'open':
            door[int(list1[2])] = True
            print("door number {} opened".format(list1[2]))
            total_time = total_time + 60
        else:
            door[int(list1[2])] = False
            print("door number {} closed".format(list1[2]))
            total_time = total_time + 60
    if str(list1[0]).lower() == 'window':
        if str(list1[1]).lower() == 'open':
            window[int(list1[2])] = True
            print("window number {} opened".format(list1[2]))
            total_time = total_time + 50
        else:
            window[int(list1[2])] = False
            print("window number {} closed".format(list1[2]))
            total_time = total_time + 50

