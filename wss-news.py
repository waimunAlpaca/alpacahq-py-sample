import asyncio
import json
import websockets


async def WebSocketStream():
    uri = "wss://stream.data.alpaca.markets/v1beta1/news"

    async with websockets.connect(uri) as ws:
        await ws.send(
            json.dumps(
                {
                    "action": "auth",
                    "key": "",
                    "secret": "",
                }
            )
        )
        await ws.send(json.dumps({"action": "subscribe", "news": ["*"]}))

        while True:
            message = await ws.recv()

            try:
                data = json.loads(message)
            except json.JSONDecodeError:
                continue

            for msg in data:
                print(msg)


if __name__ == "__main__":
    asyncio.run(WebSocketStream())
