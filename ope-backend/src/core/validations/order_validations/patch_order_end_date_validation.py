def patch_order_end_date_validation(order_id: int):
    message: list[str] = []
    if not isinstance(order_id, int) or order_id is None or order_id == 0:
        message.append("Produto inválido")

    return message


