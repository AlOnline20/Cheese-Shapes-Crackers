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

# number checker function
def num_check(question):
  
  while True:
    try:
      
      response = int(input(question))
      return response
      
    except ValueError:
      print("please enter an integer")

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
# pun to make the user laugh
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
  # code that makes sure each choice is recorded for later, small comments to make the user chuckle
  if shaper == "parallelogram":
    print("parallelogram huh, ok then.")
    print()
    shapes = "parallelogram"
    break
  if shaper == "circle":
    print("Circle, nice choice.")
    print()
    shapes = "circle"
    break
  if shaper == "rectangle":
    print("Rectangle, bold choice.")
    print()
    shapes = "rectangle"
    break
  if shaper == "square":
    print("Square, wow first pick huh")
    print()
    shapes = "square"
    break
  else:
    #error prevention
    print("please enter one of the four shapes given")


# just for looks
sleep(1)
print("now it is time to enter the dimensions for the shape")


# set loopin as well as the MIN & MAX values
looping = True
MAX_VALUE = 200
MIN_VALUE = 2

#loop for dimension values
while looping == True:
  try:
    #inputs for the parallelogram dimensions
    if shapes == "parallelogram":
      print("with these values input, the min will be 2 & the max will be 200")
      print()
      base = num_check("please enter the base of the parallelogram :")
      print()
      height = num_check("please enter the height of the parallelogram :")
      print()
      # makes sure the min and max of the parallelogram inputs are set and not overlooked
      if base < MIN_VALUE or base > MAX_VALUE or height < MIN_VALUE or height > MAX_VALUE:
        print("please enter a value input between the minimum and maximum values")
        print()
      else:
        break
    # inputs for the parallelogram dimensions
    if shapes == "circle":
      print("with this value input, the min will be 2 & the max will be 200")
      print()
      radius = num_check("please enter the radius of the circle :")
      print()
      # makes sure the min and max of the circle input are set and not overlooked
      if radius < MIN_VALUE or radius > MAX_VALUE:
        print("please enter a value input between the minimum and maximum values")
        print()
      else:
        break
    # inputs for the rectangle dimensions
    if shapes == "rectangle":
      print("with these values input, the min will be 2 & the max will be 200")
      print()
      length = num_check("please enter the length of the rectangle :")
      print()
      width = num_check("please enter the width of the rectangle :")
      print()
      # makes sure the min and max of the rectangle inputs are set and not overlooked
      if length < MIN_VALUE or length > MAX_VALUE or width < MIN_VALUE or width > MAX_VALUE:
        print("please enter a value input between the minimum and maximum values")
        print()
      else:
        break
    # inputs for the rectangle dimensions
    if shapes == "square":
      print("with this value input, the min will be 2 & the max will be 200")
      print()
      side = num_check("please enter the side of the square :")
      print()
      # makes sure the min and max of the square input are set and not overlooked
      if side < MIN_VALUE or side > MAX_VALUE:
        print("please enter a value input between the minimum and maximum values")
        print()
      else:
        break

  except ValueError:
    print()
    print("please enter the correct value")

# calculations for the parallelogram area
if shapes == "parallelogram":
  print()
  para_answer = base * height 
  print("in total the area of a parallelogram is {}cm".format(para_answer))
# calculations for the circle area
if shapes == "circle":
  print()
  circl_answer = 3.14 * (radius * radius)
  print("in total the area of a circle is {}cm".format(circl_answer))
# calculations for the rectangle area
if shapes == "rectangle":
  print()
  rect_answer = width * length
  print("in total the area of a rectangle is {}cm".format(rect_answer))
# calculations for the square area
if shapes == "square":
  print()
  squar_answer = side * side
  print("in total the area of a square is {}cm".format(squar_answer))

