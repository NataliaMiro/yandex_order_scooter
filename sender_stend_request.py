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



#Функция для получения заказа по трекеру
def get_order_by_track(track):
    return requests.get(configuration.URL + configuration.GET_ORDER,
                        params={'t' : track})
response = get_order_by_track(track)
print(response.status_code)
print(response.json())



def get_orders_courier_id(courier_id):
    return requests.get(configuration.URL + configuration.GET_ORDER,
                        params={'coirierId' : courier_id})


# Функция для создания курьера
def create_courier(courier_body):
    return requests.post(configuration.URL + configuration.GET_COURIER,
                         json=courier_body)


# Функция для передачи логина курьера
def post_courier_login(courier_login):
    return requests.post(configuration.URL + configuration.GET_COURIER_LOGIN,
                         json=courier_login)
