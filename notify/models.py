from datetime import datetime as dt

from config.mongo import mongo


class NotifyOrderModel:
    collection = mongo.db.orders

    @staticmethod
    def create_notify_order(event_type, event):
        notify_order_data = {
            'event_type': event_type,
            'event': event
        }

        return NotifyOrderModel.collection.insert_one(notify_order_data)

    @staticmethod
    def list_notify_orders():
        return list(NotifyOrderModel.collection.find())
