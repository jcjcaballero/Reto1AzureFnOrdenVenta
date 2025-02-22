import azure.functions as func
import logging
from services import insert_order
from models import Order

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="registrarOrdenVenta")
def registrarOrdenVenta(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing sell order request')

    order = Order.generate_random_order()
    insert_order(order)
    
    return func.HttpResponse(f"Order {order.id} created successfully", status_code=201)