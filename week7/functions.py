#AI DISCLOSURE: Use of CHatgpt, to help understand some of
#Function concepts. Help to understand in Exercise 5 what the bug issue was
#In the file and steps on fixing bugs
#
#
# --3 Assesment Questions--
#1. The first bug I noticed was the SyntaxError, on line 10 through traceback.
#I feel like this shows my debugging instinct is through like seeing
#a direct error show up through my code. As when I saw the python message I was
#able to figure out quick where the error was and understand a bit why it happened.
#The other errors where bit difficult as I didn't get anything from python it just did it wrong
#So i probably need to learn more about the functions and operations so I am able to
#catch those errors that are those wrong math or range ones.
#
#
#2.apply_discount(price, tier) - Takes the original price and the discount from the tier
#As inputs. Apples the right discount to the tier and returns the final price.
#Yes, a colleague can use it without reading the body as the function
#inputs + name shows already it's purpose.
#
#
#3. AI DISCLOSURE: Use of CHatgpt, to help understand some of
#Function concepts. Help to understand in Exercise 5 what the bug issue was
#In the file and steps on fixing bugs.AI use helped build my understanding
#as it was able to break it down really simple for me to understand
#Concepts and also the bugs in Exercise 5.
#
#
# --Exercise 1--
def calculate_tax(price, rate):
    return price*rate
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: {tax1:.2f}")
print(f"Tax on $250 at 8%: {tax2:.2f}")
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}")
# --Exercise 2--
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
price = 200
tiers = ["gold", "silver", "bronze", "none"]
for tier in tiers:
    print(f"{tier}:   ${apply_discount(price, tier):.2f}")
# --Exercise 3--
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted+tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")
#Function version
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted+tax
print(f"Final price ${final_price(200, "gold", 0.07):.2f}")
# --Exercise 4--
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Order: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")
# --Exercise 5--
#Solo debug, "Total = sale" - Line 6, It is equalling total to sale meaning
#it isn't adding sale to total. Line 10 there is a colon missing,I think it can't work
# without it cause all the functions I see use a ":", probs a syntax error. and for the other 2
#I think there is a error on line 6 "total = sale"this woudn't work as it suppose to be
#like the sales added to the total so I don't know the bug name for this. Also don't know the third bug
#where it is present.
#  
#Class Debrief - Yes the AI's explanation did match the actual bugs that where
#Seen in the script. It also pointed out another bug I didn't really know how to explain 
#It was the Indexerror one and the "+=" one. I guess I found that I have a little
#difficukties finding in program error and not system ones where python shows you what is wrong. 
#
#
# --Fixed Version of the code--
sales = [120, 80, 250, 175, 90]
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")
i = 0
while i < len(sales):
    print(sales[i])
    i += 1
# --Exercise 6--
x = 100   # global variable
def double_it():
    x = 999   # local variable — different from global x!
    return x * 2
print(x)           # what prints here? - I think 100
print(double_it()) # what prints here? - 1998
print(x)           # has x changed? I think 999
#Explanation why it looks like this, print(x) - does this
#cause it is usuing global variable, makes it 100. print(double_it())
#FUnction usesthe local variable 999 and times it by 2. Last print(x)
#it is 100 cause it still using the global variable as local variable does
#not change inside the function.
#
#Scope is where variables can be used in code.Local variable, only used
#inside its function, global variable is the opposite. Meaning
#can be used outside of function.
