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
  print("    It will ask you to choose a shape from those given,    ")
  print("   and it will ask if you would like to do another shape.  ")
  sleep(5)
  print("  You will answer with yes or no questions or if prompted, ")
  print("             will answer with shapes or numbers.            ")
  sleep(4)

print("     Now    ")
sleep(2)
print("Lettuce begin")
sleep(2)
print()

loopin = True

while loopin == True:
  print("The four shapes that are available are circle, rectangle, triangle, and square")
  print()
  sleep(2)
  shaper = input("now which one of these four shapes would you like to input dimensions for? :").lower()
  if shaper == "circle":
    print("Circle huh, ok then.")
    shapes = "circle"
    break
  if shaper == "triangle":
    print("Triangle, nice choice.")
    shapes = "triangle"
    break
  if shaper == "rectangle":
    print("Rectangle, bold choice.")
    shapes = "rectangle"
    break
  if shaper == "square":
    print("Square, alright then")
    shapes = "square"
    break
  else:
    print("please enter one of the four shapes given")

print()
print(shapes)