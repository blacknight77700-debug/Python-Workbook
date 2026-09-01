coins = ['Bronze', 'Silver', 'Gold','Platinum'] # No, tuples are immutable
coin = 'Bronze'
score = 10000

if score > 10000:
    if coin in ('Gold','Platinum'):
        print("You have reached level 3")
    else:
        print("You have reached level 2")
elif score > 5000 and coin in coins: # this is an elif statement
    print("You have reached level 1. Keep going")
else:
    print("Increase your score and collect coins to move up") 
# output will be You have reached 1. Keep going
