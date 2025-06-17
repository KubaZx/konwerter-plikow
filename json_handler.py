import aiofiles
import json
import asyncio

async def save_json_async(data, filename):
    async with aiofiles.open(filename, "w") as f:
        await f.write(json.dumps(data, indent=2))

async def load_json_async(filename):
    async with aiofiles.open(filename, "r") as f:
        contents = await f.read()
        return json.loads(contents)