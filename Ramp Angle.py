# Adam Bricha (U9233-5585) and Shahad Al-Harrasi(U4160-6760)
# Driver - Adam (50%)
# Navigator - Shahad(50%)

# This program accepts mass and force values from the user. These values can be decimal points.
# The program then takes these points and calculates the angle formed and formats it to 1 decimal place.



import math

g = 9.8

mass = float(input('Enter the mass of the cart (in kg): '))
force = float(input('Enter the force to push the cart (in N): '))

angle_of_ramp = (force)/(mass * g)

angle_of_ramp = math.asin(angle_of_ramp)
angle_of_ramp = (angle_of_ramp * 57.298)
angle = format(angle_of_ramp,'.1f')

print('The angle of the ramp is:', angle, 'degrees')