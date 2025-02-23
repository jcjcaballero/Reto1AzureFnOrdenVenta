import azure.functions as func
from azure.cosmos import CosmosClient
from azure.servicebus import ServiceBusClient
import logging
from services import insert_order
from models import Order
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
cosmos_db_connection_string = os.getenv("l_cosmos_db_connection_string")
service_bus_connection_string = os.getenv("l_service_bus_connection_string")

client = CosmosClient.from_connection_string(cosmos_db_connection_string)
clienteBus = ServiceBusClient.from_connection_string(service_bus_connection_string)

@app.route(route="registrarOrdenVenta")
def registrarOrdenVenta(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing sell order request')

    runnerId = 0    
    try:
        runnerId = req.get_json().get('runnerId')
    except ValueError:
        pass
    order = Order.generate_random_order(runnerId)
    insert_order(order, client, clienteBus)
    
    return func.HttpResponse(f"Order {order.id} created successfully", status_code=201)