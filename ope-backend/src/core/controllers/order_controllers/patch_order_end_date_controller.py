class PatchOrderEndDateController:

    def __init__(self, patch_order_end_date_use_case):
        self.patch_order_end_date_use_case = patch_order_end_date_use_case

    def route(self, body):

        if body is not None:
            order_id = body["id"] if "id" in body else None

            response = self.patch_order_end_date_use_case.patch_order_end_date(order_id=order_id)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}