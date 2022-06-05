from videocdn_api.models.responses import MoviesResponse
from videocdn_api.api.main import Api
from typing import Optional


class MoviesApi:
    def __init__(self, api: Api):
        self.api = api

    async def get_movies(self,
                         ordering: Optional[str] = None,
                         direction: Optional[str] = None,
                         query: Optional[str] = None,
                         field: Optional[str] = None,
                         translation: Optional[int] = None,
                         year: Optional[int] = None,
                         page: Optional[int] = None,
                         limit: Optional[int] = None,
                         **params) -> MoviesResponse:
        """
        :param ordering: Sorting by a specific value. Possible values: id, created, released
        :param direction: Sort order. Possible values: acr, desc
        :param query: Search value. A string longer than two characters.
         For example, "Home Alone" (title) or 797840 (Kinopoisk ID)
        :param field: Search field. Possible values: title(searches through all *_title fields), imdb_id, kinopoisk_id
        :param translation: ID of translation. Get a list of translations - Api.translations.get()
        :param year: Release year
        :param page: Pagination page
        :param limit: Number of results per page
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return MoviesResponse(**(await self.api.make_get_request('movies', {"ordering": ordering,
                                                                            "direction": direction,
                                                                            "query": query,
                                                                            "field": field,
                                                                            "translation": translation,
                                                                            "year": year,
                                                                            "page": page,
                                                                            "limit": limit,
                                                                            **params})))

    async def get_anime(self,
                        ordering: Optional[str] = None,
                        direction: Optional[str] = None,
                        query: Optional[str] = None,
                        field: Optional[str] = None,
                        translation: Optional[int] = None,
                        year: Optional[int] = None,
                        page: Optional[int] = None,
                        limit: Optional[int] = None,
                        **params) -> MoviesResponse:
        """
        :param ordering: Sorting by a specific value. Possible values: id, created, released
        :param direction: Sort order. Possible values: acr, desc
        :param query: Search value. A string longer than two characters.
         For example, "Jin Roh: The Wolf Brigade" (title) or 38 (Kinopoisk ID)
        :param field: Search field. Possible values: title(searches through all *_title fields), imdb_id, kinopoisk_id,
         worldart_id
        :param translation: ID of translation. Get a list of translations - Api.translations.get()
        :param year: Release year
        :param page: Pagination page
        :param limit: Number of results per page
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return MoviesResponse(**(await self.api.make_get_request('animes', {"ordering": ordering,
                                                                            "direction": direction,
                                                                            "query": query,
                                                                            "field": field,
                                                                            "translation": translation,
                                                                            "year": year,
                                                                            "page": page,
                                                                            "limit": limit,
                                                                            **params})))
