import data
import sender_stend_request

# Функция для позитивной проверки
def positive_assert_200(track):
    response = sender_stend_request.get_order_by_track(track)
    assert response.status_code == 200
    print(sender_stend_request.track)



# Функция для позитивной проверки короткой карточки
def positive_short_card_assert_200(track_with_short):
    response = sender_stend_request.get_order_with_short_by_track(track_with_short)
    assert response.status_code == 200
    print(sender_stend_request.track_with_short)



# Функция для позитивной проверки полной карточки
def positive_full_card_assert_200(track_with_full):
    response = sender_stend_request.get_order_with_full_by_track(track_with_full)
    assert response.status_code == 200
    print(sender_stend_request.track_with_full)



# Функция для негативной проверки (несуществующий трек)
def negative_assert_404(track):
    response = sender_stend_request.get_order_by_track(track)
    assert response.status_code == 404
    assert response.json()['message'] == 'Заказ не найден'

# Функция для негативной проверки (трек не передан)
def no_parametr_track_negative_assert_400(track):
    response = sender_stend_request.get_order_by_track(track)
    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для поиска'

# Тест 1. Запрос с существующим трекером
def test_get_order_success_response():
    positive_assert_200(sender_stend_request.track)
    print(sender_stend_request.track)


# Тест 1. Запрос с существующим трекером короткая карта
def test_get_order_success_response_for_short():
    positive_short_card_assert_200(sender_stend_request.track_with_short)
    print(sender_stend_request.track_with_short)



# Тест 1. Запрос с существующим трекером полная карта
def test_get_order_success_response_for_full():
    positive_full_card_assert_200(sender_stend_request.track_with_full)
    print(sender_stend_request.track_with_full)



# Тест 2. Ошибка. Запрос с несуществующим трекером
def test_get_order_error_response():
    negative_assert_404(111111)

# Тест 3. Ошибка. Запрос без трекера
def test_get_order_with_empty_track_error_response():
    no_parametr_track_negative_assert_400('')