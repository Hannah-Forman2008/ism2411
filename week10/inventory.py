# --3 assesment questions--
#1. The most surprising thing for me for lists is probably how easy it is to deal with them. 
#Your able to store different data types in them then needing to create
#new lists whenever you want to. Plus its easy to add
# and remove items from it wouthout needing to change the list.

#2. FOr class specifically math class python lists could save me much time
# in helping calculate averages, sums and differences of lot of numbers.
#Stats it would be really helpful to put the numbers in a list and
#find the 5 point summar or the statisical significance. 

print('# --Exercise 1--')
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))
print("# --Exercise 2--")
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])

print("# --Exercise 3--")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("# --Exercise4--")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("# --Exercise 5--")
coords = (40.7128, -74.0060)
try:
    coords[0]=99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")
print(coords)

print("# --Exercise 6--")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total/count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print(" --exercise 7--")
prices =[9.99, 14.99, 4.99, 24.99, 1.99]
discount =[]
for price in prices:
    discount.append(round(price* .9, 2))
print("Original prices:", prices)
print("Discount:", discount)

print(" --exercise 8--")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for amount in sales:
    if amount>300:
        high_sales.append(amount)
print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}") 