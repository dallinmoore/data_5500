# Dallin Moore

import requests
import json
import os
import csv
import json
from datetime import datetime
import networkx as nx
import ast
from alpaca.trading import TradingClient, MarketOrderRequest, OrderSide, TimeInForce


# 1 - Setup variables

threshold = 2


tickers = {"link":"link",
           "polkadot":"dot",
           "bitcoin-cash":"bch",
           "litecoin":"ltc",
           "ethereum":"eth",
           "bitcoin":"btc"}
           



coingecko_base_url = 'https://api.coingecko.com/api/v3/simple/price?ids='
coingecko_base_url2 = '&vs_currencies='
coingecko_url = coingecko_base_url+','.join([ticker for ticker in tickers])+coingecko_base_url2+','.join([tickers[ticker] for ticker in tickers])

 
api_key = 'PKHAHFEZ7ZB0REFYHLOR'
secret_key = 'tXPcnvjVNJp3y4UKMIeOUuWcw21XLrWv405RKoTf'
url = 'https://paper-api.alpaca.markets/v2'

# for alpaca api
headers = {
    'Apca-Api-Key-Id': api_key,
    'Apca-Api-Secret-Key': secret_key,
    'Content-Type': 'application/json'
}

cryptos_trade = {tickers[crypto]:tickers[crypto].upper()+'/USD' for crypto in tickers}


# 2 - Find the arbitrage


req = requests.get(coingecko_url)
data = json.loads(req.text)

# create an empty graph
g = nx.DiGraph()

# add nodes to the graph
for currency in data:
    g.add_node(tickers[currency])

edges = []
# add edges to the graph
for source, targets in data.items():
    for target, weight in targets.items():
        if tickers[source] != target:
            edges.append((tickers[source], target, weight))
            # print(f"Source: {tickers[source]}, Target: {target}, Weight: {weight}")
        
g.add_weighted_edges_from(edges) 



def find_arbitrage(graph,threshold):
    arbitrage = []
    # find all simple cycles in the graph
    cycles = nx.simple_cycles(graph)

    # iterate over each cycle, going both directions
    # if there is a cycle one direction, there must be one in the other direction
    for cycle in cycles:
        opposite_cycle = cycle[::-1]
        weight_product = 1.0
        weight_product2 = 1.0
        for i in range(len(cycle) - 1):
            source = cycle[i]
            source2 = opposite_cycle[i]
            target = cycle[i + 1]
            target2 = opposite_cycle[i + 1]
            # get the weight of the edge between source and target
            weight = graph[source][target]['weight']
            weight2 = graph[source2][target2]['weight']
            weight_product *= weight
            weight_product2 *= weight2

        # check if the product is greater or less than 1
        product = weight_product*weight_product2
        if product > 1+threshold:
            arbitrage.append((cycle, product))

    return arbitrage


arbitrage = find_arbitrage(g,threshold)


# 3 - Make the trades through USDC


trade_client = TradingClient(api_key,secret_key, paper=True)

#save data for the results.json
results = {
    "start_time":datetime.now().strftime('%Y.%m.%d:%H.%M'),
    "end_time":"",
    "start_buying_power": trade_client.get_account().non_marginable_buying_power,
    "end_buying_power":0,
    "total_cycles": len(arbitrage),
    "total_trades": 0,
    "arbitrage_taken_or_attempted": arbitrage
}

# buy crypto based on a symbol
def buy_crypto(symbol):
    payload = {
    'symbol': symbol,
    'notional':trade_client.get_account().non_marginable_buying_power,
    'side': 'buy',
    'type': 'market',
    'time_in_force': 'ioc' # immediate or cancel
    }
    # Send the buy request
    response = requests.post(url+'/orders', headers=headers, json=payload)
    
    # Check the response status
    if response.status_code == 200:
        print(f"Order placed successfully to buy ${payload['notional']} of {payload['symbol']}!")
        trade_to_csv(symbol,payload['notional'])
        return payload['notional']
    else:
        print("Error placing order:", ast.literal_eval(response.text)['message'])

# sell crypto based on a symbol
def sell_crypto(symbol,amount):
    url_symbol = symbol.replace("/","").upper()
    response = requests.delete(url+'/positions/'+url_symbol, headers=headers)
    
    if response.status_code == 200:
        print(f"Successfully closed position of ${amount} in {symbol}!")
        trade_to_csv(symbol,amount)
    else:
        print("Error closing position:", ast.literal_eval(response.text)['message'])

# function to save as a csv
def trade_to_csv(currencies, exchange_rate):
    folder_name = 'final-project/data'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    timestamp = datetime.now().strftime('%Y.%m.%d:%H.%M')
    filename = f'{currencies.replace("/","")}_{timestamp}.csv'
    filepath = os.path.join(folder_name, filename)
    data = currencies.split("/")
    data.append(exchange_rate)
    
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(data)


# cycle through all of the arbitrage opportunites that are above the threshold
for cycle in arbitrage:
    for crypto in cycle[0]:
        amount = buy_crypto(cryptos_trade[crypto])
        sell_crypto(cryptos_trade[crypto], amount)
        results["total_trades"] += 1

results['end_time'] = datetime.now().strftime('%Y.%m.%d:%H.%M')
results['end_buying_power'] = trade_client.get_account().non_marginable_buying_power

results_file_path = 'final-project/results.json'
with open(results_file_path, 'w') as results_file:
    json.dump(results, results_file, indent=4)
print("Program complete! File 'results.json' created!")