import data
import sender_stend_request

# Функция для позитивной проверки
def positive_assert_200(track):
    response = sender_stend_request.get_order_by_track(track)
    assert response.status_code == 200
    print(sender_stend_request.track)



# Тест 1. Запрос с существующим трекером
def test_get_order_success_response():
    positive_assert_200(sender_stend_request.track)
    print(sender_stend_request.track)





