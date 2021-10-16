from src.infra.repository import OrderRepository
from src.core.controllers import PatchOrderEndDateController
from src.core.use_cases import PatchOrderEndDate


def patch_order_end_date_composer():
    repository = OrderRepository()
    use_case = PatchOrderEndDate(repository)
    controller = PatchOrderEndDateController(use_case)
    return controller

