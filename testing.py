from binance import Client
from binance import BinanceSocketManager
import pandas as pd
import numpy as np
import time
import asyncio

api_key = 'fCBUzQtECIrp4dfeuc4AsahRalt48Or0HKbagFyMgdqXia112FjevdjSe7qdAgC4'
api_secret = 'nVdJOZXc42vZYPtX2GBHzHHXMueHAL6atAMYIN4I08nscaqM6Cyj6zM9gnevJmLg'

client = Client(api_key, api_secret)

li = []
li2 = []
li3 = []

asset = ''

ST = 35
LT = 125

counter = 0

while True:
    try:
        def get_money():
            li = []
            acc = client.get_account()

            for i in acc['balances']:
                li.append(i)

            usd = li[2]
            amount = usd['free']
            print('im at get_money')

            return round(float(amount)) - 20


        def get_top_symbol():
            global asset
            x = pd.DataFrame(client.get_symbol_ticker())
            y = x[x.symbol.str.contains('USD')]
            z = y[~(y.symbol.str.contains('BUSD') | y.symbol.str.contains('UP') | y.symbol.str.contains(
                'DOWN') | y.symbol.str.contains('USDT') | y.symbol.str.contains('USDC'))]

            for i in z.symbol:
                global li
                li.append(i)

            for i in li:
                global li2
                xx = (client.get_ticker(symbol=i))
                yy = xx['priceChangePercent']
                li2.append(yy)

            for i in li2:
                li3.append(float(i))

            di = dict(zip(li, li3))
            
            di.pop('AXSUSD')

            max_key = max(di, key=di.get)
            
            di.pop(max_key)
            
            sec_key = max(di, key=di.get)
            
            di.pop(sec_key)
            
            third_key = max(di, key=di.get)
            
            if counter == 0:
                asset = str(max_key)
                print(max_key)
                return max_key
            
            if counter == 1:
                asset = str(sec_key)
                print(sec_key)
                return sec_key
            
            if counter == 2:
                asset = str(third_key)
                print(third_key)
                return third_key
            
            if counter >= 3:
                print(f'other top 3 coins didnt work so going back to first {max_key}')
                asset = str(max_key)
                return max_key


        # this is from SMA portion
        def gethistoricals(symbol, LT):
            df = pd.DataFrame(
                client.get_historical_klines(symbol, '5m', str(LT) + 'minutes ago UTC', '1 minute ago UTC'))
            time.sleep(3)
            closes = pd.DataFrame(df[4])
            closes.columns = ['Close']
            time.sleep(3)
            closes['ST'] = closes.Close.rolling(7).sum()
            closes['LT'] = closes.Close.rolling(25).sum()
            time.sleep(3)
            closes.dropna(inplace=True)
            print(f'{closes} from get historicals')
            
            return closes


        historicals = gethistoricals(get_top_symbol(), LT)


        def liveSMA(hist, live):
            liveST = (hist['ST'].values + live.Price.values) / 8
            liveLT = (hist['LT'].values + live.Price.values) / 26
            print('im liveST', liveST, 'im liveLT', liveLT)
            return liveST, liveLT


        def createframe(msg):
            df = pd.DataFrame([msg])
            df = df.loc[:, ['s', 'E', 'p']]
            df.columns = ['symbol', 'Time', 'Price']
            df.Price = df.Price.astype(float)
            df.Time = pd.to_datetime(df.Time, unit='ms')
            print('im at createframe')
            return df

        def get_qty():
            coin_dic = (client.get_ticker(symbol=asset))
            coin_price = float(coin_dic['lastPrice'])
            x = get_money()
            qty = round(x / coin_price)
            print(qty)
            return qty

        # strategy is to buy when SL crosses TL to upside and sell when SL crosses TL to downside
        async def strategy(qty, SL_limit=0.97, open_position=False):
            global asset
            bm = BinanceSocketManager(client)
            ts = bm.trade_socket(asset)

            async with ts as tscm:
                while True:
                    print('im at res await')
                    res = await tscm.recv()
                    time.sleep(3)
                    frame = createframe(res)
                    livest, livelt = liveSMA(historicals, frame)
                    global counter
                    print('im checking for livest and livelt')
                    in_counter = 0
                    time.sleep(10)

                    if livest > livelt and not open_position:
                        print('im trying to make order')
                        order = client.create_order(symbol=asset,
                                                    side='BUY',
                                                    type='MARKET',
                                                    quantity=qty)
                        print('will place order')
                        print(order)
                        buyprice = float(order['fills'][0]['price'])
                        open_position = True
                        in_counter += 1
                        counter = 0
                        time.sleep(30)

                    elif open_position:
                        if frame.Price[0] < buyprice * SL_limit or frame.Price[0] > 1.05 * buyprice:
                            print('will sell order')
                            order = client.create_order(symbol=asset,
                                                        side='SELL',
                                                        type='MARKET',
                                                        quantity=(qty *.95))
                            in_counter = 0
                            print(order)
                            counter = 0
                            loop.stop()
                    
                    elif in_counter == 0 and counter <= 3 and not open_position and livest.size > 0:
                        counter += 1
                        print('ST is not greater than LT, so we arent buying yet')
                        break
                    
                    elif not open_position:
                        break

        if __name__ == "__main__":
            loop = asyncio.new_event_loop()
            loop.run_until_complete(strategy(get_qty()))

    except:
        print('either order sold or something went wrong. going to sleep for 15 seconds.')
        time.sleep(15)
