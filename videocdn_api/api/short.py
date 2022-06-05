from videocdn_api.models.responses import ShortResponse
from videocdn_api.api.main import Api
from typing import Optional


class ShortApi:
    def __init__(self, api: Api):
        self.api = api

    async def get(self,
                  internal_id: Optional[int] = None,
                  title: Optional[str] = None,
                  kinopoisk_id: Optional[int] = None,
                  imdb_id: Optional[str] = None,
                  world_art_id: Optional[int] = None,
                  page: Optional[int] = None,
                  limit: Optional[int] = None,
                  **params) -> ShortResponse:
        """
        :param internal_id: ID of the video from this server
        :param title:
        :param kinopoisk_id: ID of the video from the site kinopoisk.ru
        :param imdb_id: ID of the video from the site imdb.com
        :param world_art_id: ID of the video from the site world-art.ru
        :param page: Pagination page
        :param limit: Number of results per page
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return ShortResponse(**(await self.api.make_get_request('short', {"id": internal_id,
                                                                          "title": title,
                                                                          "kinopoisk_id": kinopoisk_id,
                                                                          "imdb_id": imdb_id,
                                                                          "world_art_id": world_art_id,
                                                                          "page": page,
                                                                          "limit": limit,
                                                                          **params})))
