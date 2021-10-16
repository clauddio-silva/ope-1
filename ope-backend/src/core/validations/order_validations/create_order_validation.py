def create_order_validation(
        done: bool,
        consumed_in: str,
        table: int,
        payment_method: str,
        obs: str,
        confirmed: bool):
    message: list[str] = []
    if not isinstance(done, bool) or done is None or done == "":
        message.append("status inválido")
    if not isinstance(consumed_in, str) or consumed_in is None or consumed_in == "":
        message.append("Data de consumo inválida")
    if not isinstance(table, int) or table is None or table == "":
        message.append("Mesa inválida")
    if not isinstance(payment_method, str) or payment_method is None or payment_method == "":
        message.append("Forma de pagamento inválida")
    if not isinstance(obs, str) or obs is None or obs == "":
        message.append("Observação inválida")
    if not isinstance(confirmed, bool) or confirmed is None or confirmed == "":
        message.append("Confirmação inválida")
    return message
