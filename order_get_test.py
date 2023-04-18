import data
import sender_stend_request

# Функция для позитивной проверки
def positive_assert_200(track):
    response = sender_stend_request.get_order_by_track(track)
    assert response.status_code == 200

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

# Тест 2. Ошибка. Запрос с несуществующим трекером
def test_get_order_error_response():
    negative_assert_404(111111)

# Тест 3. Ошибка. Запрос без трекера
def test_get_order_with_empty_track_error_response():
    no_parametr_track_negative_assert_400('')