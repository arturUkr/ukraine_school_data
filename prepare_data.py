import json
import pandas as pd


with open("json_coord_data/c4.json", 'r', encoding="utf-8") as file:
    data = json.load(file)


final_result = []
for school in data:
    geo_data = school['result_api']
    if geo_data.get('features'):
        geo_data = geo_data['features'][0]['geo_centroid']['coordinates']
    else:
        geo_data = geo_data['geo_centroid']['coordinates'] if geo_data.get('geo_centroid') else None
    final_result.append(
        {
            'school_id': str(school['school_id']),
            'school_lng': geo_data[0] if geo_data else None,
            'school_lat': geo_data[1] if geo_data else None
        }
    )


final_result_prep = {'school_id': [], 'school_lng': [], 'school_lat': []}

for school in final_result:
    final_result_prep['school_id'].append(school['school_id'])
    final_result_prep['school_lng'].append(school['school_lng'])
    final_result_prep['school_lat'].append(school['school_lat'])


final_result_prep_df = pd.DataFrame(data=final_result_prep)

final_result_prep_df.to_excel("coord_result_data/c4_school_coord.xlsx", index=False)
