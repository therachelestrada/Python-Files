# Psuedocode: 
# Start with import of random #'s 
# Before main function, convert Celsius to Fahrenheit, using formula, and return 
# In main function, create 50 random integers from the randge of -40 to 40
# Print lowest and highest CELSIUS temperature in the list
# Put a zeroFlag to check
# Generate a loop so that:
    # True? --> Set flag to true, print, and exit 
    # False? --> Print message that 0c did NOT happen
# Create a sublist of 10 individual Celsius temperatures in the range of =40 and 40 
# Rank this sublist in fro low to high 
# Execute the converter function so that it converts Celsius and Fahrenheit  
# Before excuting the average, create a storage box for the average of Celsius and Fahrenheit  
# Print Sorted sample of 10 temps... and break line for header 
# Label header Celcius and Fahrenhiet & print 
# Create a loop and find average 
# Compute the average by calling lens, then rounding both Celsius and Fahrenheit  
# End of with the average of the average of both Celsius and Fahrenheit  

import random

# Define a Function that converts the temp. from celsius to fahrenheit
def convertCtoF(celsius):
    
    # Math cruchng 
    fahrenheit = [(9/5*t)+32 for t in celsius]
    
    return fahrenheit

# Starting point of main func
def main():
    
    # Initiate  50 random #'s (-40 to 40)
    celsius = [random.randint(-40, 40) for cat in range(50)]
    
    # Print lowest & highest Celsius temps. 
    print(f'\nLowest temp is {min(celsius)}C and highest is {max(celsius)}C')
    
    # Flag to see if 0 Celsius is on or off the list
    # *** I don't think we have learned zeroFlag yet, (I learned thru Code Academy), I couldn't think of any other way from the textbook
    zeroFlag = False
    
    # Loop for each temperature in celsius list
    for cat in range(50):
        
        if celsius[cat] == 0:
            
            zeroFlag = True 
            
            # Print that the index of the first incident was found, label kitty 
            print('Found 0C at index', cat)
            
            break
      
    if zeroFlag == False:
        
        # Print that 0C is not in the temps. 
        print('No 0C occurred in list of temperatures')
        
    # Create 10 random #'s w/ ranges 
    celUniq = random.sample(range(-40, 40), 10)
    
    # Ascending order
    celUniq.sort()
    
    # Perform the first function, before def(main)
    fahrenheit = convertCtoF(celUniq)
    
    # Store average temperature in Celsius & Fahrenheit ()
    avgCelsius = 0 
    avgFahrenheit = 0 

    # Nothing fancy, just printed text 
    print('Sorted sample of ten equivalent temperatures: ')
    
    # Print the "table header"
    print('\n%-20s %-20s' %('CELSIUS', 'FAHRENHEIT'))

    # Loop for the temp. of each value 
    for cat in range(len(celUniq)):
        
        # Print the temperature list
        print('%-20.2f %-20.2f' %(celUniq[cat], fahrenheit[cat]))
        
        # Keep adding the celsius and fahrenheit temperature and store it 
        avgCelsius += celUniq[cat]
        avgFahrenheit += fahrenheit[cat]
    
    # Calculate average of the celsius temperature    
    avgCelsius = avgCelsius / len(celUniq)

    # Round celsius to 2 sig figs
    favgCelsius = round(avgCelsius,2)
    
    # Calculate average of the fahrenheit temperature    
    avgFahrenheit = avgFahrenheit / len(celUniq)

    # Round fahrenheit to 2 sig figs
    favgFahrenheit = round(avgFahrenheit,2)
    
    # Print average of the Celsius Temperature
    print(f'\nThe average Celsius Temperature is: {favgCelsius}')
    
    # Print average of the Fahrenheit Temperature
    print(f'The average Fahrenheit Temperature is: {favgFahrenheit}')

    # Not needed but create an extra line to keep everything orderly
    print('\n')
   
main() 
