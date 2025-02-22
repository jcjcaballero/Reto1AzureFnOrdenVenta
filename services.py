import json
from azure.cosmos import CosmosClient
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os

from models import Order

cosmos_db_connection_string = os.getenv("l_cosmos_db_connection_string")
cosmos_db_name = os.getenv("l_cosmos_db_name")
container_name = os.getenv("l_container_name")
service_bus_connection_string = os.getenv("l_service_bus_connection_string")
queue_name = os.getenv("l_queue_name")

def insert_order(order: Order):
    client = CosmosClient.from_connection_string(cosmos_db_connection_string)
    database = client.get_database_client(cosmos_db_name)
    container = database.get_container_client(container_name)
    
    container.upsert_item(order.__dict__)
    send_message_to_queue(order)

def send_message_to_queue(order: Order):
    message_body = json.dumps({
        "type": order.type,
        "price": order.price,
        "asset_symbol": order.asset_symbol
    })
    with ServiceBusClient.from_connection_string(service_bus_connection_string) as client:
        with client.get_queue_sender(queue_name) as sender:
            message = ServiceBusMessage(message_body)
            sender.send_messages(message)