import sender_stand_reqest
import data


# Создание заказа
def get_new_order_track():
    order_response = sender_stand_reqest.post_create_order(data.order_body)
    order_track = order_response.json()["track"]
    # Возвращает номер трека
    return order_track


# Получение заказа по треку
def get_order(order_track):
    order_response = sender_stand_reqest.get_order(order_track)
    return order_response


# Тест
def test_get_order():
    track = get_new_order_track()
    order_response = get_order(track)
    #Проверяется, что код ответа равен 200
    assert order_response.status_code == 200
    #Проверяется, что в ответе присутствует тело
    assert order_response.json()

