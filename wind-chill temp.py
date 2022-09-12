# Adam Bricha (U9233-5585) and Shahad Al-Harrasi(U4160-6760)
# Driver - Adam (50%)
# Navigator - Shahad(50%)

# This program accepts values from the user which are wind speed and temperature. They can be decimal points.
# The program then takes these values and calculates the wind chill temperature only if the conditions are met.
# The program will keep running until the conditions are met.


temp= float(input('Enter the temperature in Fahrenheit: '))
while temp < -59 or temp > 41:
    print("Temperature must be between -58F and 41F" )
    temp = float(input("Please re-enter the temperature in Fahrenheit: "))

wind = float(input('Enter the wind speed miles per hour: '))
while wind < 2:
    print("Speed must be greater than or equal to 2" )
    wind = float(input("Please re-enter the wind speed miles per hour: "))

windchill = 35.74 + (0.6215*temp) - (35.75 * (wind**0.16)) + (0.4275 * temp* (wind**0.16))
print('The wind chill index is',format(windchill,'.3f'))