import pandas as pd
from dataclasses import dataclass, asdict
from send_email import send_email
from resturant_availability import get_resturant_availability


@dataclass
class DisneyDiningAvailability:
    location:str
    date:str
    time:str


#Codes that Disney uses for resturants.  Not an complete list, just the ones I'm tracking.
resturant_dict = {
    '90002237':'Garden Grill Resturant',
    '90001744': 'Hollywood & Vine',
    '90002686':'Tusker House Resturant',
    '90001369':'Chef Mickey',
    '90001248':'Story Book Dining at Artist Point with Snow White',
    '19233597':'Topolinos Terrace - Flavors of the Riveria',
    '19046067':'Wonderland Tea Party at 1900 Park Fare'
}

#Codes for times of day when searching online.
meal_period = {
    'breakfast':80000712,
    'brunch':80000713,
    'lunch':80000717,
    'dinner':80000714
}

def main():
    disney_df = pd.DataFrame(columns=['location', 'date', 'time'])

    park_days = [11,12,13,14,17]

    rest_list = [i for i in resturant_dict]
    
    for day in park_days:

        for t in meal_period:

            resturants = get_resturant_availability(day, meal_period[t])

            for i in resturants:
                if resturants[i]['hasAvailability']:
                    try:
                        if i.split(';')[0] in rest_list:
                            for place in resturants[i]['singleLocation']['offers']:
                                results = DisneyDiningAvailability(location=resturant_dict[i.split(';')[0]],
                                time=place['label'], date=place['date'])
                                row = pd.DataFrame([asdict(results)])
                                disney_df = pd.concat([disney_df, row], axis=0, ignore_index=True)

                    except KeyError as err:
                        print(err)

    disney_df.to_excel('disney_dining.xlsx', index=False)

    send_email('disney_dining.xlsx')

if __name__ == '__main__':
    main()
