
import time
#now we begin the code


user_text = input("Please paste your text here: ")
words = user_text.split()
# freeze the script till they hit enter v.2 is adding \n
#input("\nPress Enter when you are ready to start reading...") issue with for 2
#v1.1 for versions default feels fast
print("\nSelect your reading speed")
print("1 - Normal (0.2 seconds)")
print("2 - Slower (0.4 seconds)")
print("3 - Turtle (0.6 seconds)")
print("4 - Fast (0.1 seconds)")
#get users choice
speed_choice = input("Type 1, 2, 3, or 4 and press enter: ")
if speed_choice == "1":
    delay = 0.2
elif speed_choice == "2":
    delay = 0.4
elif speed_choice == "3":
    delay = 0.6
elif speed_choice == "4":
    delay = 0.1
else:
    #failbreak, for different imputs
    print("Invalid choice! Defaulting to Normal speed.")
    delay = 0.2
# And then your loop goes here!
#had a crash about words = code using ljust(30) to clean it
#waiting room
input("\nText loaded! Press enter when you are ready to start reading... ")

for word in words:
    print(word.ljust(30), end="\r", flush=True)
    time.sleep(delay)
