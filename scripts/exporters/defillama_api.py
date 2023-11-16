import pandas as pd
from decimal import Decimal
from datetime import datetime
import sentry_sdk
from pony.orm import db_session
from yearn.entities import StatsData

sentry_sdk.set_tag('script','defillama_api')

df = pd.read_csv('https://api.llama.fi/simpleChainDataset/Ethereum?staking=true&doublecounted=true&liquidstaking=true')

@db_session
def main(protocol, timestamp, tvl):
    StatsData(chain="ETH", timestamp=timestamp, tvl=tvl)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Get the protocol name
    protocol = row['Protocol']

    # Iterate over each date column in the row
    for column in df.columns:
        if column != 'Protocol':
            # Convert the column name to a timestamp
            timestamp = datetime.strptime(column, '%d/%m/%Y').strftime('%Y-%m-%d')

            # Extract the value and convert it to a Decimal
            tvl = Decimal(str(row[column]))
            
            # Call the function to insert data into the database
            main(protocol, timestamp, tvl)