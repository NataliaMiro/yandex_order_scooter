import configuration
import data
import requests

# Функция для создания нового заказа
def create_new_order(body):
    return requests.post(configuration.URL + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers
                         )
response = create_new_order(data.order_body)
print(response.json())

#Сохранение трек-номера
track = response.json()['track']
print(track)
#Поиск заказа по трекеру
def get_order_by_track(track):
    return requests.get(configuration.URL + configuration.GET_ORDER,
                        params={'t' : track})
response = get_order_by_track(track)
print(response.status_code)
print(response.json())
