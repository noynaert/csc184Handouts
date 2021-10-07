# temperature.py
# demonstrates elif

temperature = float(input('What is the current temperature in Fahrenheit? '))
print(f'The temperature is {temperature} degrees fahrenheit.')

if temperature > 90:
    raining = input('Is it raining?')
    if raining == 'yes':
        print('Go for a walk in the rain')
    else:
        print('Go swimming')
elif temperature > 60:
   print('Take a walk')
elif temperature > 32:
    print('Go hiking')
elif temperature > 0:
    inches = float(input('How many inches of snow is on the ground? '))
    enoughSnow = inches > 1.0
    if enoughSnow:
        print('Go sledding')
    else:
        print('Go ice skating')
else:
    print('Play cards by the fire')
    
print('Done')
