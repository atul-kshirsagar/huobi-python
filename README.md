"# huobi-python" 

"#Getting Started"

"#Prerequisites"

To use Huobi Python, you need to have an API key and secret key for Huobi. 

You can create an API key and signature by following the instructions in the Huobi API documentation.

(https://huobiapi.github.io/docs/spot/v1/en/#authentication)

"#Usage"

huobi_subscribe_order_updates.py

This file subscribes to order updates and authenticates using an API key and signature.
To run the script, replace ACCESS_KEY and SECRET_KEY with your own keys

huobi_market_data.py

This file subscribes to market data for the BTC/USDT pair. 
All return data of websocket Market APIs are compressed with GZIP so they need to be unzipped.

"#Key Points"

First of all create api key by signing in. Give neccessary permission to API Key.
After creation, under settings add necessary trading pairs. 

You can create API key from here:

https://www.huobi.com/en-us/apikey/


Huobi had their own SDK ad Demo.
You can refer this from here: https://github.com/huobiapi?tab=repositories
Specifically for python3:  https://github.com/HuobiRDCenter/huobi_Python

"Access URLs:"

-REST API

https://api.huobi.pro

https://api-aws.huobi.pro

-Websocket Feed (market data except MBP incremental)

wss://api.huobi.pro/ws

wss://api-aws.huobi.pro/ws

-Websocket Feed (market data only MBP incremental)

wss://api.huobi.pro/feed

wss://api-aws.huobi.pro/feed

-Websocket Feed (account and order)

wss://api.huobi.pro/ws/v2

wss://api-aws.huobi.pro/ws/v2



"#References"

Huobi API documentation for Websocket Market Data:

https://huobiapi.github.io/docs/spot/v1/en/#websocket-market-data

Huobi API documentation for Websocket Account and Order:

https://huobiapi.github.io/docs/spot/v1/en/#websocket-account-and-order

Huobi API documentation for Authentication:

https://huobiapi.github.io/docs/spot/v1/en/#authentication