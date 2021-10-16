class CreateOrderController:

    def __init__(self, create_order_use_case):
        self.create_order_use_case = create_order_use_case

    def route(self, body):

        if body is not None:
            print("controller", body)
            done = body["done"] if "done" in body else None
            consumed_in = body["consumed_in"] if "consumed_in" in body else None
            table = body["table"] if "table" in body else None
            payment_method = body["payment_method"] if "payment_method" in body else None
            obs = body["obs"] if "obs" in body else None
            confirmed = body["confirmed"] if "confirmed" in body else None

            response = self.create_order_use_case.create_order(done=done,
                                                         consumed_in=consumed_in,
                                                         table=table,
                                                         payment_method=payment_method,
                                                         obs=obs, confirmed=confirmed)
            return response
        return {"data": None, "status": 400, "errors": ["Invalid request"]}
