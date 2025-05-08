from config.mongo import mongo


class NotifyOrderModel:
    collection = mongo.db.orders

    @staticmethod
    def create_notify_order(**kwargs):
        notify_order_data = {
            'event_type': kwargs['event_type'],
            'timestamp': kwargs['timestamp'],
            'product': kwargs['product'],
            'product_cost_price': kwargs['product_cost_price'],
            'product_selling_price': kwargs['product_selling_price'],
            'quantity': kwargs['quantity'],
            'description': kwargs['description']
        }

        return NotifyOrderModel.collection.insert_one(notify_order_data)

    @staticmethod
    def list_notify_orders():
        return list(NotifyOrderModel.collection.find())
