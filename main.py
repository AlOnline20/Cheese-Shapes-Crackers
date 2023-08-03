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
  print("The Questions proceeded will ask for numbers that will make")
  print("       the area and perimeter of a shape chosen.           ")
  sleep(6)
  print("    it will ask you to choose a shape from those given,    ")
  print("   and it will ask if you would like to do another shape.  ")
  sleep(5)

print("     Now    ")
sleep(2)
print("Lettuce begin")
sleep(2)
print()

