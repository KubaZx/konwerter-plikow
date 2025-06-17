import asyncio
from utils import json_handler

async def test_async():
    data = {"imie": "Jakub", "wiek": 22}
    await json_handler.save_json_async(data, "async_output.json")

asyncio.run(test_async())