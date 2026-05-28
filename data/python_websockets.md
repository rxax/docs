## WebSocket API 

Used for two-way communication – client and server

The Client:

```python
import asyncio
import websockets
async def hello():
	async with websockets.connect("ws://url:8765") as websocket:
	    await websocket.send("Hello world!")
	    await websocket.recv()
asyncio.run(hello())
```

The Server:

```python
import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
```