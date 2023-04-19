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
# Функция для сохранения трек-номера
track = response.json()['track']
print(track)



# Функция для создания нового заказа и сохранения треек-номера для короткой карты
def create_new_order_with_short_card(body):
    return requests.post(configuration.URL + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers
                         )
response = create_new_order_with_short_card(data.order_body_short)
print(response.json())
# Функция для сохранения трек-номера
track_with_short = response.json()['track']
print(track_with_short)



# Функция для создания нового заказа и сохранения треек-номера для полной карты
def create_new_order_with_full_card(body):
    return requests.post(configuration.URL + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers
                         )
response = create_new_order_with_full_card(data.order_body_full)
print(response.json())
# Функция для сохранения трек-номера
track_with_full = response.json()['track']
print(track_with_full)



#Функция для получения заказа по трекеру
def get_order_by_track(track):
    return requests.get(configuration.URL + configuration.GET_ORDER,
                        params={'t' : track})
response = get_order_by_track(track)
print(response.status_code)
print(response.json())



#Функция для поиска заказа по трекеру для короткой карточки
def get_order_with_short_by_track(track_with_short):
    return requests.get(configuration.URL + configuration.GET_ORDER,
                        params={'t' : track})
response = get_order_with_short_by_track(track_with_short)
print(response.status_code)
print(response.json())



#Функция для поиска заказа по трекеру для полной карточки
def get_order_with_full_by_track(track_with_full):
    return requests.get(configuration.URL + configuration.GET_ORDER,
                        params={'t' : track})
response = get_order_with_full_by_track(track_with_full)
print(response.status_code)
print(response.json())



# Функция для удаления заказа
def cancel_order(track):
    return requests.put(configuration.URL + configuration.CANCEL_ORDER_PATH,
                        params={'track': track})
