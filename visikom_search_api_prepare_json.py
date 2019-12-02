import json
from pprint import pprint
import pandas as pd


with open('data_file.json', 'r', encoding='utf-8') as file:
    res = json.load(file)
pprint(res.get('features')[0])
pprint(res.get('features')[0]['geo_centroid']['coordinates'])

pprint(res.get('features')[0].get('properties'))
final_result = {
    'point_id': [],
    'point_lng': [],
    'point_lat': [],
    'point_address': [],
    'address_info': [],
    'dist_meters': []
}
for obj in res.get('features'):
    final_result['point_id'].append(obj.get('id'))
    final_result['point_lng'].append(obj['geo_centroid']['coordinates'][0])
    final_result['point_lat'].append(obj['geo_centroid']['coordinates'][1])
    final_result['point_address'].append(obj['properties'].get('address'))
    final_result['address_info'].append(obj['properties'].get('address_info'))
    final_result['dist_meters'].append(obj['properties']['dist_meters'])

pprint(len(final_result['point_id']))

pd.DataFrame(final_result).to_excel('dd.xlsx', index=False)
