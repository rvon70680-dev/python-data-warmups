import csv, argparse
import random
from faker import Faker


fake = Faker()
parser = argparse.ArgumentParser(
    description="Generate random trades and write to a CSV file."
)
parser.add_argument(
    "--rows",
    type=int,
    default=100,
    help="Number of trades to generate (default: 100)",
)
args = parser.parse_args()

print(f"Generating {args.rows} random trades...")
print("Writing trades to trades_big.csv...")

rows = []
for i in range(1, args.rows + 1):
    rows.append(
        {
            "trade_id": f"T{i:06d}",
            "trade_date": fake.date_between("-1y", "today"),
            "desk": random.choice(["Rates", "FX", "Equities", "Credit"]),
            "counterparty": fake.company(),
            "lei": fake.bothify(
                "????????????????????"
            ).upper(),  # 20-character legal entity code
            "product": random.choice(["Swap", "Bond", "Option", "Spot"]),
            "notional": round(random.uniform(1e5, 5e7), 2),
            "currency": random.choice(["USD", "EUR", "GBP", "INR"]),
            "trader_id": f"TR{random.randint(1, 50):03d}",
            "status": random.choice(["Booked", "Settled", "Cancelled"]),
        }
    )


with open("trades_big.csv", "w", newline="") as file:
    fieldnames = [
        "trade_id",
        "trade_date",
        "desk",
        "counterparty",
        "lei",
        "product",
        "notional",
        "currency",
        "trader_id",
        "status",
    ]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
