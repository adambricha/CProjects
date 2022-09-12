# Adam Bricha (U9233-5585) and Shahad Al-Harrasi(U4160-6760)
# Driver - Shahad (50%)
# Navigator - Adam(50%)

# This program accepts 3 values from the user which are the length of edges of a triangle. They can be decimal points.
# The program then takes these points and calculates the perimeter of the triangle if the certain conditions are met.

edge1= float(input('Enter length of edge1: '))
edge2= float(input('Enter length of edge2: '))
edge3= float(input('Enter length of edge3: '))
sum= edge1 + edge2 + edge3

if (edge1 + edge2) > edge3 and (edge2 + edge3) > edge1 and (edge1 +edge3) > edge2:
    print ('The perimeter is', sum)
else:
    print("Perimeter cannot be calculated: the input is invalid.")
