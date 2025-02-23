from dataclasses import dataclass
import uuid
from datetime import datetime, timezone
import random

ASSET_SYMBOLS = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "FB", "NVDA", "NFLX" ]
PRICES = [num for num in range(10, 201, 5)]
USERS_IDS = ["user-1234", "user-5678", "user-8910", "user-4321", "user-8765", "user-8910", "user-1027" ]


@dataclass
class Order:
    id: str
    type: str
    assetSymbol: str
    quantity: int
    price: float
    status: str
    created_at: str
    updated_at: str
    user_id: str
    matching: dict | None
    partitionKey:str

    @staticmethod
    def generate_random_order():
        Random_asset_symbol = random.choice(ASSET_SYMBOLS)
        return Order(
            id=str(uuid.uuid4()),
            type="sell",
            assetSymbol= Random_asset_symbol,
            quantity=1,
            price=random.choice(PRICES),
            status="open",
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=datetime.now(timezone.utc).isoformat(),
            user_id=random.choice(USERS_IDS),
            matching=None,
            partitionKey = Random_asset_symbol
        )