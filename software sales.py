# Adam Bricha (U9233-5585) and Shahad Al-Harrasi(U4160-6760)
# Driver - Shahad (50%)
# Navigator - Adam (50%)

# This program accepts a value from the user which is the amount of packages purchased. They can be decimal points.
# The program then takes this values and calculates the the discount the user will receive.
# The program will show the user the discount and the total price after applying the discount.


package= int(input("Enter the number of packages purchased: "))
price = 99
if package < 10:
    discount = 0 * price * package
    print("Discount Amount @ 0%: $ ", format(discount, '.2f'))
    total = (package * price) - discount
    print("Total Amount: $ ", format(total, '.2f'))
else:
    if package >= 10 and package <= 19:
       discount = 0.1 * price * package
       print("Discount Amount @ 10%: $ ",format(discount,'.2f'))
       total= (package * price) - discount
       print("Total Amount: $ ",format(total,'.2f'))
    else:
        if package >= 20 and package <= 49:
           discount = 0.2 * price * package
           print("Discount Amount @ 20%: $ ",format(discount,'.2f'))
           total = (package * price ) - discount
           print("Total Amount: $ ",format(total,'.2f'))
        else:
            if package >= 50 and package <= 99:
               discount = 0.3 * price * package
               print("Discount Amount @ 30%: $ ", format(discount, '.2f'))
               total = (package * price) - discount
               print("Total Amount: $ ", format(total, '.2f'))
            else:
                if package >= 100 :
                   discount = 0.4 * price * package
                   print("Discount Amount @ 40%: $ ", format(discount, '.2f'))
                   total = (package * price) - discount
                   print("Total Amount: $ ", format(total, '.2f'))

