def exchange_money(budget, exchange_rate):
    """
    Convirtiendo monedas a las de otros países (Colombia, Estados Unidos y Cuba)

    Parámetros:
    budget (float): Ingrese su moneda a cambiar
    exchange_rate (float): Ingrese el valor de la tasa de cambio.

    Retorna:
    float: valor equivalente en la moneda extranjera.
    """
    return budget * exchange_rate  



budget = float(input("Ingrese la cantidad que desea cambiar: "))
exchange_rate = float(input("Ingrese el precio actual de su país: "))

resultado = exchange_money(budget, exchange_rate)
print(f"El monto equivalente en la moneda extranjera es: {resultado:.2f}")
