# sleep
from time import sleep
from types import EllipsisType

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

# Instructions that tell the user what to expect
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
#pun to make the user laugh
print("Lettuce begin")
sleep(2)
print()

#to keep loop
loopin = True

# while loop to choose shape
while loopin == True:
  # the four shapes that are available
  print("The four shapes that are available are parallelogram, rectangle, circle, and square")
  print()
  sleep(2)
  shaper = input("now which one of these four shapes would you like to input dimensions for? :").lower()
  # code that makes sure each choice is recorded for later
  if shaper == "parallelogram":
    print("parallelogram huh, ok then.")
    shapes = "parallelogram"
    break
  if shaper == "circle":
    print("Circle, nice choice.")
    shapes = "circle"
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
    #error prevention
    print("please enter one of the four shapes given")

    
sleep(1)
print("now it is time to enter the dimensions for the shape")

looping = True
MAX_VALUE = 200
MIN_VALUE = 2

#loop for dimension values
while looping == True:
  try:
    #inputs for the dimensions
    if shapes == "parallelogram":
      print("with these values input, the min will be 2 & the max will be 200")
      print()
      base = int(input("please enter the base of the parallelogram :"))
      print()
      height = int(input("please enter the height of the parallelogram :"))
      print()
    if shapes == "circle":
      print("with this value input, the min will be 2 & the max will be 200")
      print()
      radius = int(input("please enter the radius of the circle :"))
      print()
    if shapes == "rectangle":
      print("with these values input, the min will be 2 & the max will be 200")
      print()
      length = int(input("please enter the length of the rectangle :"))
      print()
      width = int(input("please enter the width of the rectangle :"))
      print()
    if shapes == "square":
      print("with this value input, the min will be 2 & the max will be 200")
      print()
      side = int(input("please enter the side of the square :"))
      print()
    else:
      print()
      break
  except ValueError:
    print()
    print("please enter the correct value")