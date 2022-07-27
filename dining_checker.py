import pandas as pd
from send_email import send_email
from resturant_availability import DisneyResturant

meal_period = ['breakfast','brunch','lunch','dinner']

def main():

    resturants = (
    'Garden Grill Resturant',
    'Hollywood & Vine',
    'Tusker House Resturant',
    'Chef Mickey',
    'Story Book Dining at Artist Point with Snow White',
    'Topolinos Terrace - Flavors of the Riveria',
    'Wonderland Tea Party at 1900 Park Fare')

    park_days = [11,12,13,14,17]
    
    

    location = DisneyResturant('Hollywood & Vine')

    for period in meal_period: 
        location.get_resturant_availability(11,period)

    print(location.availability[2])
    
if __name__ == '__main__':
 
    main()
