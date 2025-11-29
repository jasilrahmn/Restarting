# Making funcction to get ticket price with value of it as age
def get_ticket_price(age):
    # Ticket price for age under 12
    if age <= 12:
        ticket_price = 10
    # Ticket price for age above 65
    elif age >= 65:
        ticket_price = 15
    # Ticket price for age b/w 13 and 64
    else:
        ticket_price = 20
     # Returing Ticket price for using outside function
    return ticket_price

# Getting age of the user  
user_age = int(input("Enter your age:"))

# Printing ticket price by accessing through the function inside print
print(get_ticket_price(user_age), "$")