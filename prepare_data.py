import json
from pprint import pprint
import pandas as pd


with open("kyiv.json", 'r', encoding="utf-8") as file:
    data = json.load(file)


final_result = []
for school in data:
    geo_data = school['result_api']
    if geo_data.get('features'):
        geo_data = geo_data['features'][0]['geo_centroid']['coordinates']
    else:
        geo_data = geo_data['geo_centroid']['coordinates']
    final_result.append(
        {
            'school_id': str(school['school_id']),
            'school_lng': geo_data[0],
            'school_lat': geo_data[1]
        }
    )

# pprint(final_result)
# print(len(final_result))


final_result_prep = {'school_id': [], 'school_lng': [], 'school_lat': []}
for school in final_result:
    final_result_prep['school_id'].append(school['school_id'])
    final_result_prep['school_lng'].append(school['school_lng'])
    final_result_prep['school_lat'].append(school['school_lat'])

# pprint(final_result_prep)

final_result_prep_df = pd.DataFrame(data=final_result_prep)

final_result_prep_df.to_excel("coord_result_data/kyiv_school_coord.xlsx", index=False)