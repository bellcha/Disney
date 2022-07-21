import requests
import json
from dataclasses import dataclass

@dataclass
class DisneyDiningAvailability:
    location:str
    date:str
    time:str
    label:str
    url:str
    productType:str

url = f"https://disneyworld.disney.go.com/finder/api/v1/explorer-service/dining-availability-list/false/wdw/80007798;entityType=destination/2022-09-11/4/?mealPeriod=80000714"

headers = {
  'authority': 'disneyworld.disney.go.com',
  'method': 'GET',
  'path': '/finder/api/v1/explorer-service/dining-availability-list/false/wdw/80007798;entityType=destination/2022-09-11/2/?mealPeriod=80000714',
  'scheme': 'https',
  'accept': 'application/json, text/plain, */*',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'en_US',
  'cookie': 'SWID=1a655483-2715-4fe0-9b0d-eb64f2a5e699; geolocation_aka_jar=%7B%22zipCode%22%3A%2236561%22%2C%22region%22%3A%22AL%22%2C%22country%22%3A%22US%22%2C%22metro%22%3A%22ORANGEBEACH%22%2C%22metroCode%22%3A%22686%22%7D; languageSelection_jar_aka=%7B%22preferredLanguage%22%3A%22en_US%22%2C%22version%22%3A%221%22%2C%22precedence%22%3A0%2C%22language%22%3A%22en_US%22%2C%22akamai%22%3A%22true%22%7D; akavpau_disneyworld_disney_go_com_homepage=1658369874~id=1ec904b33a3cc1535c41c2c76cb25a8d; bm_sz=D4F1D64ED28058E63182D7A180996DBF~YAAQjT83FyRczx2CAQAAXYeHHhCL81vSDKhK7inL+zUrxTYRhdid+ZPWAzEtmxPT//E2lAJDKMKRdV70k4CB0G3h0Hk6kqpjytZI+nWN/Yp/HfKWuPJDDwNcia0hvbE7ezB9xURgH/LjO23jjzuLYizPG2E9OSrlTRcmFhvwQjt4mTBKOM2NBM4Bk7W/ixwobqgBMr8qqdTiKQXobNBanRFddSN2fWZoRC5/y5874yLZZLpcmlMxdyFXmJNJJB8pz3m2DgafyHhpWoAqlvoEXDhkwyoTGuJA+5EEn0wFwQ==~4277552~4469559; GEOLOCATION_jar=%7B%22zipCode%22%3A%2236561%22%2C%22region%22%3A%22alabama%22%2C%22country%22%3A%22united+states%22%2C%22metro%22%3A%22mobile-pensacola+%28ft+walt%29%22%2C%22metroCode%22%3A%22686%22%2C%22countryisocode%22%3A%22USA%22%7D; PHPSESSID=p3eq65g9q6vubdtfehshb53tl6; pep_oauth_token=5a20b698d3ba4e62aeb2fe946dccb825; pep_oauth_token_expiration=461; dvicSpaApplication=%7B%22dvicSpaApplication%22%3Atrue%7D; LANGUAGE_MESSAGE_DISPLAY=1; Conversation_UUID=a4ef37c0-089a-11ed-82c3-8d2639a0ad67; personalization_jar=%7B%22id%22%3A%22f979941b-a9b8-41a7-9a52-9eee9145e7ae%22%7D; WDPROView=%7B%22version%22%3A2%2C%22preferred%22%3A%7B%22device%22%3A%22desktop%22%2C%22screenWidth%22%3A1280%2C%22screenHeight%22%3A1024%7D%2C%22deviceInfo%22%3A%7B%22device%22%3A%22desktop%22%2C%22screenWidth%22%3A1280%2C%22screenHeight%22%3A1024%7D%2C%22browserInfo%22%3A%7B%22agent%22%3A%22Chrome%22%2C%22version%22%3A%22103.0.5060.134%22%7D%7D; ak_bmsc=9D9D1B7B591333D41095109FA791A6F7~000000000000000000000000000000~YAAQjT83F0tezx2CAQAAl6CHHhC49wlABsZJh3v6AqL+ELJ4JVY5MTSY5M0s4gCL3E9BIHqqnlELDdLfNphUkxVcafkXFBtKSvKbPLxOpI1Nou+cZHqnnf4iZHVEebOhw/mLxyH0UZmXfr0xtuV6Vbbk0Wn9EdEfrbdQQfVCX2jOT9zwSdy1VlYsEko4H7exo/tM1cfISrOtni9o2m7vuqTu3oC2EEMXbZ8coRx6cZe4PXAVbdYi8HzsqL0vNqsbPBwm5a+Fg3L61Z4CLTAoaY4RvBSvOp6wV+JZTGjav/hNCFfr+5xtEM3nWCHt5iaKTZ+b3gpdro8+4E9DF0K9zunNfUs9HP+ntLb+4Pa46nPWqhqYrPgOknjBXfLHnUoiMVpZOZ5IwM6OeErAgzVrHqyvKA2e2sXnpJJCcYAnNCNw77eFjCaQsviK1LXLQLA5SCYWxIF2k5oQ7o2qyUU0JXO5FA7e48zy0BLR59BiEboz3px7QXziQjm5n0aI2v0ZiNxVrQ==; localeCookie_jar_aka=%7B%22contentLocale%22%3A%22en_US%22%2C%22version%22%3A%223%22%2C%22precedence%22%3A0%2C%22akamai%22%3A%22true%22%7D; akavpau_disneyworld_disney_go_com_dine=1658370186~id=99c80d491f7b12e058cb5bc678928b6d; _abck=AA61855C2247557A66BC9F3DF9EC23F0~0~YAAQjT83FyNfzx2CAQAAeLaHHghpu2Wrz2QRI74kIu+FUqlf4VilfqZ1NWfsILib+6BoCVprIboKdGbSBtUJwgMouvohasIJU2Vv6cKXvA08i6Jh1tK564yaVDyQlj7ZFDRokqOxY41oqi2nbsSeww14X6sY3ne4dsSCke7q0EvoGqfXRAsxWed55AiaXudiZnQHFRS6+vdRw6ZVZ67UL/h/O9eZ1ERjLoKr4gaeaUgpTUM5W9el0Or3gDzyzI/wcTZ/OojltJCUYZZJnx85+YjdjELfVfJFvHzEJML4YLDcOFLKHeoN1vm5QK1sfF5rDGCmFCU9ccDXBPGYa+jXQt0B7WMDP1GQ8NsvumbXgYQRK7PF9cdGyICjIqvzxzU4BMduCHtTojAyQRGurSWzRUBgrVY=~-1~-1~-1; akacd_RWASP-default-phased-release=3835822386~rv=37~id=a4335d8f997f40a12748a6a607ffff27; __d=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhY2Nlc3NfdG9rZW4iOiJhNjVjYTM3Njk5MjY0ZjJlOTBhOWZmODBjZTE2YWMxZiIsInRva2VuX3R5cGUiOiJCRUFSRVIiLCJleHBpcmVzX2luIjoiMjg4MDAiLCJpYXQiOjE2NTgzNjk1ODd9.SKvywyl6JwX6TOBAhPDem53GhYo6FHpryOYj03TwDCBGb8iTV9Z8oC6lvjomqG7SmTPStiRLQXP0nKRGEXGydg; finderPublicTokenExpireTime=1658398327304; surveyThreshold_jar=%7B%22pageViewThreshold%22%3A3%7D; WDPROGeoIP=YToxODp7czo4OiJhcmVhY29kZSI7czozOiIyNTEiO3M6NzoiY291bnRyeSI7czoxMzoidW5pdGVkIHN0YXRlcyI7czo5OiJjb250aW5lbnQiO3M6MjoibmEiO3M6MTA6ImNvbm5lY3Rpb24iO3M6OToiYnJvYWRiYW5kIjtzOjExOiJjb3VudHJ5Y29kZSI7czozOiI4NDAiO3M6MTQ6ImNvdW50cnlpc29jb2RlIjtzOjM6InVzYSI7czo2OiJkb21haW4iO3M6MTA6ImNzcGlyZS5jb20iO3M6MzoiZHN0IjtzOjE6InkiO3M6MzoiaXNwIjtzOjEzOiJjIHNwaXJlIGZpYmVyIjtzOjU6Im1ldHJvIjtzOjI2OiJtb2JpbGUtcGVuc2Fjb2xhIChmdCB3YWx0KSI7czo5OiJtZXRyb2NvZGUiO3M6MzoiNjg2IjtzOjY6Im9mZnNldCI7czo0OiItNTAwIjtzOjg6InBvc3Rjb2RlIjtzOjU6IjM2NTYxIjtzOjM6InNpYyI7czo1NToiV2lyZWxlc3MgVGVsZWNvbW11bmljYXRpb25zIENhcnJpZXJzIChleGNlcHQgU2F0ZWxsaXRlKSI7czo3OiJzaWNjb2RlIjtzOjY6IjUxNzMxMiI7czo1OiJzdGF0ZSI7czo3OiJhbGFiYW1hIjtzOjM6InppcCI7czo1OiIzNjU2MSI7czoyOiJpcCI7czoxNDoiMTk4LjI4LjE4NC4xNTMiO307; akacd_dineplan=1658542442~rv=76~id=551128767adee1873578a1d945235ef6; bm_sv=3E371A96BE358A94809F0426530A2087~YAAQrj83Fwe3gfuBAQAAtI6IHhCe3sjGAvxm1nwUdbiMfUuidhc7m0+sOEEjrPcig3t/goH8yRZZRlDzID/Xe9UeyGGpVk5DOXDXHvUdFdeBVD2hrOBqBfrshYjzxGi47Eo0KFusMacl/q8mm9TVANakk9e0rn2/3iX6D+RDFg6T/NG5dFq27hU7dg6lJL2jKn5XKSLgNnK/aIDMj8GBhb2VZy37HJp8deKRvbcLjOlFRbNarhkWcfuHalEnoa9RFWXvsg==~1; _abck=AA61855C2247557A66BC9F3DF9EC23F0~-1~YAAQrD83F4s7Ov2BAQAArgOPHgguT5uA6x6ugBn+KsK4QkbZ7nc5EAQEYLcvYZBv8SK7WTsPV1ibBiJd+tvZGanH9hshXSTnjTl8/t2T8M3NrZ3wtCKh61v2Vsv29mHvbJYNfRMVc2+2GNHxC2e2iFKsLZ6bGpa4WPcha+zV3oeehIBR2uxNVKprrx/HpRef2H/Z5vvoJa0v/4cIjeA1CxpmPh3vbiSLW2cezca58ggQEtpZcS6b6b1zeoXBGQqZx6uBBSnOeMedgN+q+0q0HilXuJYU+JslfXi6/M+yX/0xQQPEOCn2HIzoxPwW2/pUTYRGmukg53u2qmh7PK1XZgV/l3seSC8tMG5TJnDFZAWMXjy/Rj0oIkpFHz6vtFSCkbPDB7h0Kc2d3+8NGX5PEATjkR8=~0~-1~-1; ADRUM_BT=R:40|i:11467454|g:09b47636-08ab-49ea-8a64-53ba743c211a824086|e:732|n:Disney-Prod_e4dfe7aa-6e26-4d68-9dc7-886d09949252; akacd_dineplan=1658542865~rv=76~id=1011b0a61016a041b9d817ed0a953653',
  'referer': 'https://disneyworld.disney.go.com/dining',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sec-gpc': '1',
  'undefined': 'a4ef37c0-089a-11ed-82c3-8d2639a0ad67',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
}

resturant_dict = {
    '90002237':'Garden Grill Resturant',
    '90001744': 'Hollywood & Vine',
    '90002688':'Tusker House Resturant',
    '90001369':'Chef Mickey',
    '90001248':'Story Book Dining at Artist Point with Snow White',
    '19233597':'Topolinos Terrace - Flavors of the Riveria',
    '19046067':'Wonderland Tea Party at 1900 Park Fare'
}

meal_period = {
    'lunch':80000717,
    'dinner':80000714,
    'breakfast':80000712,
    'brunch':80000713
}

response = requests.request("GET", url, headers=headers)

json_raw = json.loads(response.text)

resturants = json_raw['availability']

for i in resturants:
    if resturants[i]['hasAvailability']:
        try:
            rest_list = [i for i in resturant_dict]
            if i.split(';')[0] in rest_list:
                for place in resturants[i]['singleLocation']['offers']:
                    results = DisneyDiningAvailability(resturant_dict[i.split(';')[0]],**place)
                    print(results)
                print('\n')

        except KeyError as err:
            print(err)