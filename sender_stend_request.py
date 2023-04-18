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
#Функция для поиска заказа по трекеру
def get_order_by_track(track):
    return requests.get(configuration.URL + configuration.GET_ORDER,
                        params={'t' : track})
response = get_order_by_track(track)
print(response.status_code)
print(response.json())


# Функция для удаления заказа
def cancel_order(track):
    return requests.put(configuration.URL + configuration.CANCEL_ORDER_PATH,
                        params={'track': track})
