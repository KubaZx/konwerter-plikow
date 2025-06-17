import aiofiles
import yaml

async def load_yaml(path):
    async with aiofiles.open(path, 'r') as f:
        content = await f.read()
        return yaml.safe_load(content)

async def save_yaml(data, path):
    async with aiofiles.open(path, 'w') as f:
        content = yaml.dump(data, sort_keys=False, allow_unicode=True)
        await f.write(content)