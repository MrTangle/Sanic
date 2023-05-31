import sanic
from sanic import Websocket, Request

app = sanic.Sanic("Websocketing")

'''
@app.websocket("/wsendpoint")
async def endpoint_server(request, ws: Websocket):
    while True:
        data = "Hello!"
        print("Sending: " + data)
        await ws.send(data)
        data = await ws.recv()
        print("Received: " + data)
'''


# Versión simplificada loop https://sanic.dev/en/guide/advanced/websockets.html#routing


@app.websocket("/feed")
async def feed(request: Request, ws: Websocket):
    async for msg in ws:
        await ws.send(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
