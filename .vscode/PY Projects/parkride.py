print ()
first_rider_age = int (input('What is the age of the first rider? '))
first_rider_height = int (input('What is the height of the first rider (in inches)? '))
second_rider = (input('Is there a second rider (Yes/No)? '))
if second_rider.lower() == 'no':
#Single Rider
    if first_rider_height < 36:
        joy_ride = False
    elif first_rider_age >= 18 and first_rider_height >= 62:
        joy_ride = True
#STRETCH
    elif first_rider_age >= 12:
        golden_passport = (input('Please do you have a golden passport (Yes/No)? '))
        if golden_passport.lower() == 'yes' and first_rider_height >= 62:
            joy_ride = True
        else:
            joy_ride = False
    else:
        joy_ride = False
elif second_rider.lower () == 'yes':
#Two riders
    second_rider_age = int (input('What is the age of the second rider? '))
    second_rider_height = int (input('What is the height of the second rider (in inches)? '))
    if first_rider_height < 36 or second_rider_height < 36:
        joy_ride = False
    elif first_rider_age >= 18 or second_rider_age >= 18:
        joy_ride = True
#STRETCH
    elif first_rider_age >= 12 and second_rider_age >= 12 and first_rider_height >= 52 and second_rider_height >= 52:
        joy_ride = True
    else:
        joy_ride = False
print()
if joy_ride:
    print ('Congratulation! You meet the requirements. Enjoy the ride.')
else:
    print  ('Sorry, you did not meet our minimum requirements.')