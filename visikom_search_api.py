import json
from pprint import pprint

from api import api
import requests




def get_data_search_api(category: str, point_lng: float, point_lat: float, radius: int, api_key: str):
    base_str = "https://api.visicom.ua/data-api/4.0/uk/search/"
    search_str = f"{category}.json?n={point_lng},{point_lat}&radius={radius}&key={api_key}"
    request_str = f"{base_str}{search_str}"
    response = requests.get(request_str)
    return response.json()


rr = get_data_search_api(category="poi_atm",
                           point_lat=50.441267,
                           point_lng=30.522033,
                           radius=500,
                           api_key=api)

with open("data_file.json", "w", encoding="utf8") as write_file:
    json.dump(rr,
              write_file,
              sort_keys=False,
              indent=4,
              ensure_ascii=False)


# class SearchApiStr:
#
#     def __init__(self, category: str, point_lng: float, point_lat: float, radius: int, api_key: str):
#         self.__category = category
#         self.__point_lng = point_lng
#         self.__point_lat = point_lat
#         self.__radius = radius
#         self.__api_key = api_key
#         self.request_str = self.__get_request_str()
#
#     def __get_request_str(self):
#         base_str = "https://api.visicom.ua/data-api/4.0/uk/search/"
#         search_str = f"{self.__category}.json" \
#             f"?n={self.__point_lng},{self.__point_lat}&" \
#             f"radius={self.__radius}&key={self.__api_key}"
#         request_str = f"{base_str}{search_str}"
#         return request_str
#
#
# class SearchApiRequest:
#
#     def __init__(self, request_str):
#         self.__request_str = request_str
#
#     def response_search_api_json(self, file_name=None):
#         response = requests.get(self.request_str)
#         if file_name:
#             with open(file_name, 'w', encoding='utf8') as file:
#                 json.dump(response.json(),
#                           file,
#                           sort_keys=False,
#                           indent=4,
#                           ensure_ascii=False)
#         return response.json()
#
#     def response_search_api_df(self, file_name=None):


