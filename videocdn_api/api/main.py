import random
from typing import List, Dict
from videocdn_api import api
import aiohttp


class Api:
    """
    The main class.
    """
    def __init__(self,
                 api_token: str,
                 proxy_list: List[str] = None,
                 client_headers: dict = None,
                 api_server: str = 'https://videocdn.tv/api'):

        # Settings
        self.api_token = api_token
        self.api_server = api_server
        self.proxy_list = proxy_list if proxy_list else []
        self.client_headers = client_headers if client_headers else {}

        # APIs
        self.movies = api.movies.MoviesApi(self)
        self.series = api.series.SeriesApi(self)
        self.short = api.short.ShortApi(self)
        self.translations = api.translations.TranslationsApi(self)

    async def make_get_request(self, route, params: dict = None) -> Dict:
        async with aiohttp.ClientSession(headers=self.client_headers) as session:
            if not params:
                params = {}
            async with session.get(f'{self.api_server}/{route}/',
                                   proxy=random.choice(self.proxy_list) if self.proxy_list else None,
                                   params={**{key: val for key, val in params.items() if val is not None},
                                           'api_token': self.api_token}) as response:
                # TODO: Exceptions
                if response.status == 200:
                    if 'login' in response.url.path:
                        print('Invalid token')
                        raise Exception
                    json_res = await response.json()
                    if json_res['result'] is True:
                        return json_res
                else:
                    raise Exception

    def set_token(self, api_token: str):
        self.api_token = api_token

    def set_proxy_list(self, proxy_list: List[str]):
        self.proxy_list = proxy_list

    def set_client_headers(self, client_headers: dict):
        self.client_headers = client_headers
