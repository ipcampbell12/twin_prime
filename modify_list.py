""" my_array = [2, 4, 6, 8, 10, 12]

for i, num in enumerate(my_array):
    my_array[i] = num + 1

print(my_array)
 """

import time

slaves = ["Bob", "Sam", "Tomkin"]

print("Here are the slaves: ")
time.sleep(1)

for slave in slaves:
    print(slave)
    time.sleep(1)

while True:
    user_input = input("Who do you want as your slave?")

    while True:
        for slave in slaves:
            if user_input == slave:
                time.sleep(1)
                print(f"You have selected {slave} ")
                break  # breaks out of the for loop
            if user_input not in slaves:
                time.sleep(1)
                print("Please select a valid slave")
                continue
            break
