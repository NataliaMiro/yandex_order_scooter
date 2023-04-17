import data
import configuration
import requests



def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

def get_order(order_track):
    ORDER_TRACK = configuration.ORDER_TRACK_PATH
    ORDER_TRACK = ORDER_TRACK+"?t=" + str(order_track)
    return requests.get(configuration.URL_SERVICE + ORDER_TRACK, headers=data.headers)