import pandas as pd
import sentry_sdk
sentry_sdk.set_tag('script','statistics_api_exporter')

df = pd.read_csv('https://api.llama.fi/simpleChainDataset/Ethereum?staking=true&doublecounted=true&liquidstaking=true')

print(df)

json_row = df.iloc[0:1].to_json(orient='records')
# print(json_row)

@db_session
def some_function(timestamp, some_number):
    StatsDatapoint(chain=cache_chain(), timestamp=timestamp, ethtvl=some_number)