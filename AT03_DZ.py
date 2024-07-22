from config import TOKEN_CAT
import requests

def get_cat_breeds():
   url = "https://api.thecatapi.com/v1/breeds"
   headers = {"x-api-key": TOKEN_CAT}
   response = requests.get(url, headers=headers)
   return response.json()


def get_cat_image_by_breed(breed_id):
   url = f"https://api.thecatapi.com/v1/images/search?breed_ids={breed_id}"
   headers = {"x-api-key": TOKEN_CAT}
   response = requests.get(url, headers=headers)
   data = response.json()
   return data[0]['url']

def get_breed_info(breed_name):
   breeds = get_cat_breeds()
   for breed in breeds:
       if breed['name'].lower() == breed_name.lower():
           return breed
   return None

name_cat = "Мурзик"
name_cat = "Bengal"

breed_name = name_cat
breed_info = get_breed_info(breed_name)
if breed_info:
   cat_image_url = get_cat_image_by_breed(breed_info['id'])
   info = (
       f"Порода - {breed_info['name']}\n"
       f"Описание - {breed_info['description']}\n"
       f"Продолжительность жизни - {breed_info['life_span']} лет"
   )
   print(cat_image_url)
   print(info)
else:
   print("Порода не найдена. Попробуйте еще раз.")