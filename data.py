headers = {
    "Content-Type": "application/json"
}


order_body = {
    "firstName": "Vika",
    "lastName": "Vika",
    "address": "Ulitsa 2",
    "metroStation": 4,
    "phone": "+77777777777",
    "rentTime": 5,
    "deliveryDate": "2023-05-05",
    "comment": "Пожалуйста, привезите самокат",
    "color": [
        "BLACK"
    ]
}


# Проверка для короткой карты
order_body_short = {
    "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
    "metroStation": 204,
    "deliveryDate": "2023-04-18"
}


# Проверка для полной карты
order_body_full = {
    "firstName": "Абдурахмангаджи",
    "lastName": "Убдурахмангаджи",
    "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
    "metroStation": 4,
    "phone": "+34916123451",
    "rentTime": 5,
    "deliveryDate": "2023-04-18",
    "comment": "Привет, Абдурахмангаджи!",
    "color": [
        "BLACK"
    ]
}