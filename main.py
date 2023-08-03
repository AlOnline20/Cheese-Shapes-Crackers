# sleep

from time import sleep

# yes or no function
def yes_no(question):

  while True:
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"

    elif response == "no" or response == "n":
      return "no"

    else:
      print("please enter yes or no")

# main routine down below

want_instructions = yes_no("Do you want to read the instructions? :")
sleep(1)

if want_instructions == "yes":
  print("")
  print("")
  print("")
  print("")
  sleep(3)

print("Now to begin")
sleep(2)
print()