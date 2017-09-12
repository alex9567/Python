number = 23
guess = int(input('Enter an integer :'))
if guess == number:
    print('you guess it')
    print('but not any prizes')
elif guess < number:
    print('No,it is a litter higher than that')
else:
    print('Mo.it is a litter lower than that')
print('Done')    
