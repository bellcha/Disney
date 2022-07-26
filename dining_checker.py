import pandas as pd
from dataclasses import dataclass, asdict
from send_email import send_email
from resturant_availability import DisneyResturant

#Codes that Disney uses for resturants.  Not an complete list, just the ones I'm tracking.


#Codes for times of day when searching online.
meal_period = {
    'breakfast':80000712,
    'brunch':80000713,
    'lunch':80000717,
    'dinner':80000714
}

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


    #df = pd.DataFrame(asdict(data))
    
    #print(df.head(1))
    
    #send_email('disney_dining.xlsx')

if __name__ == '__main__':
 
    main()
