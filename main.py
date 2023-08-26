shapers = []
area = []
perimeter = []

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
      print("parallelogram huh, ok then.")
      return shape
    if shape == "circle":
      print("Circle, nice choice.")
      return shape
    if shape == "rectangle":
      print("Rectangle, bold choice.")
      return shape
    if shape == "square":
      print("Square, wow first pick huh")
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
        print("please keep the number in the 2-200 range")
    except ValueError:
      print("please enter a number")

# calculations for perimeter and area for the chosen shape
def dimensions():
  while True:
    try:
      #calculations for parallelogram
      if shape == "parallelogram":
        base = perameter_maker("please enter the base:")
        height = perameter_maker("please enter the height:")
        aside = perameter_maker("please enter the side:")
        para_area = base * height 
        para_perimeter = 2 * (aside + base)
        area.append(para_area)
        perimeter.append(para_perimeter)
        #printing the are and perimeter of the parallelogram
        print()
        print("The area total for parallelogram is {}cm".format(para_area))
        print()
        print("The perimeter total for parallelogram is {}cm".format(para_perimeter))
        return base,height,aside
      #calculations for square
      if shape == "square":
        side = perameter_maker("please enter the side:")
        squar_area = side * side
        squar_perimeter = 4 * side
        area.append(squar_area)
        perimeter.append(squar_perimeter)
        #printing the are and perimeter of the square
        print()
        print("The area total for square is {}cm".format(squar_area))
        print()
        print("The perimeter total for square is {}cm".format(squar_perimeter))
        return side
      #calculations for circle
      if shape == "circle":
        radius = perameter_maker("please enter the radius:")
        circl_area = 3.14 * (radius * radius)
        circl_perimeter = 2 * 3.14 * radius
        area.append(circl_area)
        perimeter.append(circl_perimeter)
        #printing the are and perimeter of the circle
        print()
        print("The area total for circle is {}cm".format(circl_area))
        print()
        print("The perimeter total for circle is {}cm".format(circl_perimeter))
        return radius
      #calculations for rectangle
      if shape == "rectangle":
        length = perameter_maker("please enter the length:")
        width = perameter_maker("please enter the width:")
        rect_area = width * length
        rect_perimeter = 2 * (length + width)
        area.append(rect_area)
        perimeter.append(rect_perimeter)
        #printing the are and perimeter of the rectangle
        print()
        print("The area total for rectangle is {}cm".format(rect_area))
        print()
        print("The perimeter total for rectangleis{}cm".format(rect_perimeter))
        return length,width
      else:
        print("error")
    except ValueError:
      print("ERROR")
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
print("The four shapes that are available are parallelogram, rectangle, circle, and square")
#loop to make sure you can go multiple times
while True:
  shape = shape_quest("now which one of these four shapes would you like to input dimensions for? :")
  print()
  shapers.append(shape)
  dimensions()
  go_again = yes_no("would you like to go again?")
  if go_again == "yes":
    print("ok")
  else:
    break

print("Alrighty then")
#print for the area, perimeter and the shape
print("the shape(s) that were chosen were {}".format(shapers))
print("the area(s) that were calculated were {}".format(area))
print("the perimeter(s) that were calculated were {}".format(perimeter))

