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

# choose shape function
def shape_quest(question):

  while True:

    shape = input(question).lower()
    if shape == "parallelogram":
      return shape
    if shape == "circle":
      return shape
    if shape == "rectangle":
      return shape
    if shape == "square":
      return shape
    else:
      print("please enter correct value")

# number and perameter checker
def perameter_maker(question):

  while True:
    try:
      gate = int(input(question))
      if gate in range(2,201):
        print("alright")
        return gate
      else:
        print("ERROR")
    except ValueError:
      print("error")

# calculations for perimeter and area
def calc_PandA():
  if shape_picker == "parallelogram":
    para_area = base * height 
    para_perimeter = 2 * (aside + base)
    print("The area total for parallelogram is {}cm".format(para_area))
    print("The perimeter total for parallelogram is {}cm".format(para_perimeter))
    return
  if shape_picker == "circle":
    circl_area = 3.14 * (radius * radius)
    circl_perimeter = 2 * 3.14 * radius
    print("The area total for circle is {}cm".format(circl_area))
    print("The perimeter total for circle is {}cm".format(circl_perimeter))
    return
  if shape_picker == "rectangle":
    rect_area = width * length
    rect_perimeter = 2 * (length + width)
    print("The area total for rectangle is {}cm".format(rect_area))
    print("The perimeter total for rectangle is {}cm".format(rect_perimeter))
    return
  if shape_picker == "square":
    squar_area = side * side
    squar_perimeter = 4 * side
    print("The area total for square is {}cm".format(squar_area))
    print("The perimeter total for square is {}cm".format(squar_perimeter))
    return

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

print("The four shapes that are available are parallelogram, rectangle, circle, and square ")
# shape picker for the shapes given
shape_picker = shape_quest("now which one of these four shapes would you like to input dimensions for? : ")

# just for looks
sleep(1)
print("now it is time to enter the dimensions for the shape")

#loop for dimension values
while True:
  #inputs for the parallelogram dimensions
  if shape_picker == "parallelogram":
    print("with these values input, the min will be 2 & the max will be 200")
    print()
    base = perameter_maker("please enter the base of the parallelogram :")
    print()
    height = perameter_maker("please enter the height of the parallelogram :")
    print()
    aside = perameter_maker("please enter the side of the parallelogram :")
    print()
    break
  # inputs for the parallelogram dimensions
  if shape_picker == "circle":
    print("with this value input, the min will be 2 & the max will be 200")
    print()
    radius = perameter_maker("please enter the radius of the circle :")
    print()
    break
  # inputs for the rectangle dimensions
  if shape_picker == "rectangle":
    print("with these values input, the min will be 2 & the max will be 200")
    print()
    length = perameter_maker("please enter the length of the rectangle :")
    print()
    width = perameter_maker("please enter the width of the rectangle :")
    print()
    break
  # inputs for the rectangle dimensions
  if shape_picker == "square":
    print("with this value input, the min will be 2 & the max will be 200")
    print()
    side = perameter_maker("please enter the side of the square :")
    print()
    break

#calculations results
print(" ---- RESULTS ----")
calc_PandA()

