"""Create a function named calculate_discount(price, discount_percent) that 
calculates the final price after applying a discount. 
The function should take the original price (price)
and the discount percentage (discount_percent) as parameters. 
If the discount is 20% or higher, apply the discount; otherwise, 
return the original price.
Using the calculate_discount function, prompt the user to enter the original price
of an item and the discount percentage. Print the final price after applying the
discount, or if no discount was applied, print the original price.
"""


def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent/100))
        return final_price
    else:
        return price

enter_price = eval(input("Enter the original price of the product: "))
enter_discount = eval(input("Enter the discount you want: "))
final_price = calculate_discount(enter_price, enter_discount)
print("The final price of the product you are purchasing is: GHc",final_price)     

list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]

sum = 0

sum1 = 0

for elem in list1:

    if (elem % 2 == 0):
        sum = sum + elem
        continue
if (elem % 3 == 0):
    sum1 = sum1 + elem
print(sum , end=" ")