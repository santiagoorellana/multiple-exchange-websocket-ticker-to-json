# -*- coding: utf-8 -*-
'''
Capturador de datos multiple exchange mediante CCXT Pro.
En dependencia de las variables de configuración, este script lee de varios
exchanges, mediante websocket, los tickets del par de monedas configurado, y
los guarda en un fichero con formato JSON para su posterior análisis.
'''
__version__ = '1.0'
__author__ = 'Santiago A. Orellana Perez'
__created__ = '14/ogosto/2023'
__tested__ = 'Python 3.10'


from asyncio import run, gather, sleep
import ccxt.pro
import time


#############################################################################
# PARAMETROS DE CONFIGURACION

# Lista de exchanges en los que se van a capturar los datos.
# Pueden ser varios de esta lista:

# alpaca, ascendex, bequant, binance, binancecoinm, binanceus, binanceusdm,
# bitfinex, bitget, bitmart, bitmex, bitopro, bitpanda, bitrue, bitstamp,
# bittrex, bitvavo, blockchaincom, bybit, cex, coinbaseprime, coinbasepro,
# coinex, cryptocom, currencycom, deribit, fmfwio, gate, gemini, hitbtc,
# hollaex, huobi, huobijp, idex, independentreserve, kraken, krakenfutures,
# kucoin, kucoinfutures, luno, mexc, ndax, okcoin, okx, phemex, poloniex,
# poloniexfutures, probit, upbit, wazirx, whitebit, woo

EXCHANGES_ID = [
    'hitbtc',
    'kucoin',
    'okx',
    'bitfinex',
    'bitget',
    'bitmart',
    'bitmex',
    'huobi',
    'bittrex',
    'bybit'
]


# Par de monedas (market) a las que se van a capturar los precios.
# Las monedas pueden ser cualquiera de las que soporte el exchange seleccionado.
# El par seleccionado debe existir en el exchange como un par válido.

BASE = 'BTC'        # Primera moneda del par.
QUOTE = 'USDT'      # Segunda moneda del par.

# Directorio donde se van a crear los ficheros de salida.
# Por defecto se utiliza el directorio actual.

BASE_DIRECTORY = "./"

#############################################################################


fileNameData = ""
fileNameMarket = ""
frame = {}
frame["exchanges"] = {}
frame["timestamp"] = None
frame["datetime"] = None

def to_file(fileName, data):
    '''Agrega una nueva linea (data) de datos al fichero (fileName).'''
    try:
        fileOut = open(fileName, 'a')
        fileOut.write(data+'\n')
        fileOut.close()
    except Exception as e:
        print('Error guardando en fichero!')
        print('Exception: '+str(e))



def report_ticker(exchangeID, ticker):
    global fileNameData
    global frame
    error = False
    try:
        frame["exchanges"][exchangeID] = {
            "timestamp": ticker["timestamp"],
            "datetime": ticker["datetime"],
            "last": str(ticker["last"]),
            "bid24h": str(ticker["bid"]),
            "ask24h": str(ticker["ask"]),
            "volumeBase24h": str(ticker["baseVolume"]),
            "volumeQuote24h": str(ticker["quoteVolume"])
        }
    except:
        frame["exchanges"][exchangeID] = {}
        error = True
    frame["timestamp"] = ticker["timestamp"]
    frame["datetime"] = ticker["datetime"]
    if not error:
        to_file(fileNameData, str(frame))


async def exchange_loop(exchangeId, symbol):
    global fileNameMarket
    exchange = getattr(ccxt.pro, exchangeId)()
    errors = 0
    while errors < 120:
        try:
            markets = await exchange.load_markets()
            marketData = {
                "exchange": exchangeId,
                "symbol": symbol,
                "market": markets[symbol]
            }
            to_file(fileNameMarket, str(marketData))
            await watch_ticker_loop(exchange, symbol)
        except Exception as e:
            errors += 1
            await sleep(1)
    await exchange.close()
            


async def watch_ticker_loop(exchange, symbol):
    # exchange.verbose = True  # uncomment for debugging purposes if necessary
    error = False
    while True:
        try:
            ticker = await exchange.watch_ticker(symbol)
            now = exchange.milliseconds()
            error = False
            report_ticker(exchange.id, ticker)
            print(
                exchange.iso8601(now),
                exchange.id,
                symbol,
                'bid:', ticker['bid'],
                'ask:', ticker['ask'],
                'last:', ticker['last']
            )
        except Exception as e:
            if not error: 
                print(exchange.id, "Error:", str(e))
            error = True


async def main():
    global fileNameData
    global fileNameMarket
    print('CCXT Version:', ccxt.__version__)
    symbol = BASE +"/"+ QUOTE
    fileName = "{}_{}_{}.json".format(
        BASE.lower(),
        QUOTE.lower(),
        round(time.time()*1000)
        )
    fileNameData = "{}data_{}".format(BASE_DIRECTORY, fileName)
    fileNameMarket = "{}market_{}".format(BASE_DIRECTORY, fileName)
    print(f"output data: {fileNameData}\n")
    print(f"output metadata: {fileNameMarket}\n")
    
    loops = [exchange_loop(exchange_id, symbol) for exchange_id in EXCHANGES_ID]
    await gather(*loops)


run(main())

