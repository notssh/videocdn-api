# videocdn-api
An asynchronous Python library for interacting with the [Videocdn.tv](https://videocdn.tv) API.

Uses aiohttp as client and pydantic for models

[VideoCDN API Documentaion](https://videocdn.tv/docs/short)

## Usage example
```python
import asyncio
from videocdn-api import Api
api = Api('your_videocdn_token')

async def example():
    response = await api.short.get(title='Миньоны')
    print(response)
    return
if __name__ == '__main__':
    asyncio.run(example())
```

## Development progress
- [X] Official API Support 
    - [X] short
    - [X] translations
    - [X] movies
    - [X] anime
    - [X] \*-series
    - [X] \*-series/seasons
    - [X] \*-series/episodes
- [ ] Features
    - [ ] Direct links extractor
