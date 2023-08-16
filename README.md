<h1>Multiple exchange websocket ticker to JSON with CCXT Pro</h1>
Depending on the configuration variables, this script reads from various
exchanges, via websocket, the tickets of the configured currency pair, and
saves them in a file in JSON format for later analysis.

<h3>Installation:</h3>
To run the script you need Python 3.10 or higher.
The dependencies are installed from the CMD with the following commands:<br><br>

<b>pip install ccxt</b><br>
<b>pip install ccxtpro</b>

<h3>Data packaging:</h3>
Each time a price update is obtained from a market of a exchange, a new 
frame data package is created, containing the last market tickers on 
each of the exchanges.
The frame package tickers are found in the "exchanges" property and
It consists of a dictionary where the keys are the names of the exchanges.
Each ticker contained in the frame package contains its own tickers.
timestamp time and datetime, corresponding to the instant of reception.
Because each exchange sends data at its own pace, which depends on 
liquidity and volume of operations, it is normal that not all the 
tickers contained in the frame packet have the same timestamp.
Tickers are constantly received from each exchange and are always saved
the most up-to-date value of each exchange. Every time you get a new
ticker, a frame package is created that contains the value of all the 
last ticker of the exchanges including the new ticker received.
In turn, each frame packet contains a timestamp of the instant in which 
the package is created. Although each ticket inside the frame packet
has its own timestamp, we recommend analysts use in the graphs and 
analysis the timestamp of the package frame. The timestamp of each 
ticker within the frame is used to know how updated the ticker data is.

Timestamps are saved in Timestamp format and Datetime format:<br><br>
<b>"timestamp"</b><br>
<b>"datetime"</b>

The data file resulting from the capture consists of multiple lines,
where each line contains a packet frame. The name of the data file
has the following format: data_base_quote_milliseconds.json

The market metadata file is made up of multiple lines, where each 
line contains a json object with the metadata of the market.
In the market metadata you can find the fees of the markets on 
each exchange and details on how to apply the fee.
The name of the market metadata file has the following format:
market_base_quote_milliseconds.json
'''

Santiago A. Orellana Perez<br>
tecnochago@gmail.com<br>
14/agosto/2023<br>

___________________________________________________________

<h1>Capturador de tickers de multiples exchanges con CCXT Pro.</h1>
En dependencia de las variables de configuración, este script lee de varios
exchanges, mediante websocket, los tickets del par de monedas configurado, y
los guarda en un fichero con formato JSON para su posterior análisis.

<h3>Instalación:</h3>
Para ejecutar el script se necesita Python 3.10 o superior.
Las dependencias se instalan desde el CMD con los siguientes comandos:<br><br>

<b>pip install ccxt</b><br>
<b>pip install ccxtpro</b>

<h3>Empaquetado de datos:</h3>
Cada vez que se optiene una actualización de precios de un mercado de un
exchange, se crea un nuevo paquete de datos frame, que contiene los ultimos
tickers del mercado en cada uno de los exchanges. 
Los tickers del paquete frame se encuentran en la propiedad "exchanges" y
consiste en un diccionario donde las llaves son los nombres de los exchanges.
Cada tickers contenido en el paquete frame contiene sus propias marcas de
tiempo timestamp y datetime, correspondientes al instante de recepción.
Debido a que cada exchange envía los datos a su propio ritmo, el cual
depende de la liquidez y volúmen de operaciones, es normal que no todos
los tickers contenidos en el paquete frame tengan la misma marca de tiempo.
Los tickers se reciben constantemente de cada exchange y siempre se guarda
el valor más actualizado de cada exchange. Cada vez que se recibe un nuevo
ticker, se crea un paquete frame que contiene el valor de todos los ultimos
ticker de los exchanges incluyendo el nuevo ticker recibido.
A su vez, cada paquete frame contiene una marca de tiempo del instante
en que se crea el paquete. Aunque cada ticket dentro del paquete frame
tiene su propia marca de tiempo, recomendamos a los analistas utilizar
en las graficas y análisis la marca de tiempo timestamp del paquete
frame. La marca de tiempo de cada ticker dentro del frame, sirve para
conocer que tan actualizado está el dato del ticker.

Las marcas de tiempo se guardan en formato Timestamp y Datetime:<br><br>
<b>"timestamp"</b><br>
<b>"datetime"</b>

El fichero de datos resultante de la captura se compone de multiples lineas,
donde cada linea contiene un paquete frame. El nombre del fichero de datos
tiene el siguiente formato: data_base_quote_milliseconds.json

El fichero de metadatos de mercado se compone de multiples lineas,
donde cada linea contiene un objeto json con los metadatos del mercado.
En los metadatos de mercado se pueden encontrar los fee de los mercados
en cada exchange y los datos sobre cómo aplicar el fee.
El nombre del fichero de metadatos de mercado tiene el siguiente formato:
market_base_quote_milliseconds.json
'''

Santiago A. Orellana Perez<br>
tecnochago@gmail.com<br>
14/agosto/2023<br>
