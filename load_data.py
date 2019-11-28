from pprint import pprint
import json
import time

import pandas as pd
from visikim_api import get_geocode
from api import api

# load school data
res = pd.read_excel("school.xlsx", sheet_name="dnipro")

# list for save school
res_list = []

# create list of schools
for school in range(res.shape[0]):   # range(5)
    data = res.iloc[school]
    res_list.append(
        {
            'school_id': str(data['school_id']),
            'address_name': data['address_name'],
            'city_name': data['city_name']
        }
    )
pprint(res_list)
print(len(res_list))

# add geo coding to list of schools
for school in res_list:
    city = school['city_name']
    address = school['address_name']
    school['result_api'] = get_geocode(city_name=city, street_name=address, api_key=api)
    time.sleep(1)
    print(school['result_api'])


# save list of schools with geo coding to json
with open('json_coord_data/dnipro.json', 'w', encoding="utf8") as file:
    json.dump(res_list,
              file,
              sort_keys=False,
              indent=4,
              ensure_ascii=False)
