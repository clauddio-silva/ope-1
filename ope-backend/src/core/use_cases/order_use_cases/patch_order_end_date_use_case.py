from src.core.validations import patch_order_end_date_validation as validate


class PatchOrderEndDate:

    def __init__(self, order_repository):
        self.order_repository = order_repository

    def patch_order_end_date(self, order_id: int):
        invalid_inputs = validate(order_id=order_id)

        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.order_repository.patch_order_end_date(order_id=order_id)

            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
