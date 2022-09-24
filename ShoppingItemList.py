# Psduecode:
# Custom module  
    # Define one function in a seperate file named subtotal.py
    # Multiply price * quantity
    # Print item and subtotal
# Import subtotal module as pew 
# Ask user to:
    # Input # of items
    # Description of item
    # Price of item
    # Quantity of item
    # Discplay subtotal and go back in the loop
# Store subtotals and add them all together at the end & display

# Creating a module named subtotal (pew)
import subtotal as pew

def main():

    # Generate question for num variable
    num = int(input(f'How many different items are being purchased? '))

    # Set these variables to 0 for later use 
    total = 0
    pusheen = 0

    # Get ready for for statement in the amount listed above 
    for r in range(num):
        desc = input(f'Enter description of item {r+1} ')
        price = float(input(f'Enter price of item {r+1} '))
        quantity = int(input(f'Enter the quantity for item {r+1} '))
        # Call function and label total 
        total = pew.subtotal(desc,price,quantity)
        # All totals will equal the adorable kitty (the final total added all together)
        pusheen += total

    print(f'\nYour total is ${pusheen:,.2f}')

main()
