from videocdn_api.models.responses import SeriesResponse, SeriesSeasonsResponse, SeriesEpisodesResponse
from videocdn_api.api.main import Api
from typing import Optional


class SeriesApi:
    def __init__(self, api: Api):
        self.api = api

    async def get_series(self,
                         ordering: Optional[str] = None,
                         direction: Optional[str] = None,
                         query: Optional[str] = None,
                         field: str = None,
                         translation: int = None,
                         year: Optional[int] = None,
                         page: Optional[int] = None,
                         limit: Optional[int] = None,
                         **params) -> SeriesResponse:
        """
        :param ordering: Sorting by a specific value. Possible values: id, start_date, end_date, created
        :param direction: Sort order. Possible values: acr, desc
        :param query: Search value. A string longer than two characters.
         For example, "Infinity Train" (title) or 1132500 (Kinopoisk ID)
        :param field: Search field. Possible values: title(searches through all *_title fields), imdb_id, kinopoisk_id
        :param translation: ID of translation. Get a list of translations - Api.translations.get()
        :param year: Release year
        :param page: Pagination page
        :param limit: Number of results per page
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return SeriesResponse(**(await self.api.make_get_request('tv-series',
                                                                 {"ordering": ordering,
                                                                  "direction": direction,
                                                                  "query": query,
                                                                  "field": field,
                                                                  "translation": translation,
                                                                  "year": year,
                                                                  "page": page,
                                                                  "limit": limit,
                                                                  **params})))

    async def get_series_seasons(self,
                                 tv_series_id: Optional[int] = None,
                                 ordering: Optional[str] = None,
                                 direction: Optional[str] = None,
                                 page: Optional[int] = None,
                                 limit: Optional[int] = None,
                                 **params) -> SeriesSeasonsResponse:
        """
        :param tv_series_id: Any ID of the series
        :param ordering: Sorting by a specific value. Possible values: id, start_date, end_date, created
        :param direction: Sort order. Possible values: acr, desc
        :param page: Pagination page
        :param limit: Number of results per page
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return SeriesSeasonsResponse(**(await self.api.make_get_request('tv-series/seasons',
                                                                        {"tv_series_id": tv_series_id,
                                                                         "ordering": ordering,
                                                                         "direction": direction,
                                                                         "page": page,
                                                                         "limit": limit,
                                                                         **params})))

    async def get_series_episodes(self,
                                  tv_series_id: Optional[int] = None,
                                  season_id: Optional[int] = None,
                                  ordering: Optional[str] = None,
                                  direction: Optional[str] = None,
                                  query: Optional[str] = None,
                                  field: str = None,
                                  translation: int = None,
                                  year: Optional[int] = None,
                                  page: Optional[int] = None,
                                  limit: Optional[int] = None,
                                  **params) -> SeriesEpisodesResponse:
        """
        :param tv_series_id: Any ID of the series
        :param season_id: Any season ID
        :param ordering: Sorting by a specific value. Possible values: id, released, ru_released, created
        :param direction: Sort order. Possible values: acr, desc
        :param query: Search value. A string longer than two characters.
         For example, "Infinity Train" (title) or 1132500 (Kinopoisk ID)
        :param field: Search field. Possible values: title(searches through all *_title fields), imdb_id, kinopoisk_id
        :param translation: ID of translation. Get a list of translations - Api.translations.get()
        :param year: Release year
        :param page: Pagination page
        :param limit: Number of results per page
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return SeriesEpisodesResponse(**(await self.api.make_get_request('tv-series/episodes',
                                                                         {"tv_series_id": tv_series_id,
                                                                          "season_id": season_id,
                                                                          "ordering": ordering,
                                                                          "direction": direction,
                                                                          "query": query,
                                                                          "field": field,
                                                                          "translation": translation,
                                                                          "year": year,
                                                                          "page": page,
                                                                          "limit": limit,
                                                                          **params})))

    async def get_anime_series(self,
                               ordering: Optional[str] = None,
                               direction: Optional[str] = None,
                               query: Optional[str] = None,
                               field: str = None,
                               translation: int = None,
                               year: Optional[int] = None,
                               page: Optional[int] = None,
                               limit: Optional[int] = None,
                               **params) -> SeriesResponse:
        """
        :param ordering: Sorting by a specific value. Possible values: id, start_date, end_date, created
        :param direction: Sort order. Possible values: acr, desc
        :param query: Search value. A string longer than two characters.
         For example, "" (title) or  (Kinopoisk ID)
        :param field: Search field. Possible values: title(searches through all *_title fields),
        imdb_id, kinopoisk_id, worldart_id
        :param translation: ID of translation. Get a list of translations - Api.translations.get()
        :param year: Release year
        :param page: Pagination page
        :param limit: Number of results per page
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return SeriesResponse(**(await self.api.make_get_request('anime-tv-series',
                                                                 {"ordering": ordering,
                                                                  "direction": direction,
                                                                  "query": query,
                                                                  "field": field,
                                                                  "translation": translation,
                                                                  "year": year,
                                                                  "page": page,
                                                                  "limit": limit,
                                                                  **params})))

    async def get_anime_series_seasons(self,
                                       tv_series_id: Optional[int] = None,
                                       ordering: Optional[str] = None,
                                       direction: Optional[str] = None,
                                       page: Optional[int] = None,
                                       limit: Optional[int] = None,
                                       **params) -> SeriesSeasonsResponse:
        """
        :param tv_series_id: Any ID of the series
        :param ordering: Sorting by a specific value. Possible values: id, start_date, end_date, created
        :param direction: Sort order. Possible values: acr, desc
        :param page: Pagination page
        :param limit: Number of results per page
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return SeriesSeasonsResponse(**(await self.api.make_get_request('anime-tv-series/seasons',
                                                                        {"tv_series_id": tv_series_id,
                                                                         "ordering": ordering,
                                                                         "direction": direction,
                                                                         "page": page,
                                                                         "limit": limit,
                                                                         **params})))

    async def get_anime_series_episodes(self,
                                        tv_series_id: Optional[int] = None,
                                        season_id: Optional[int] = None,
                                        ordering: Optional[str] = None,
                                        direction: Optional[str] = None,
                                        query: Optional[str] = None,
                                        field: str = None,
                                        translation: int = None,
                                        year: Optional[int] = None,
                                        page: Optional[int] = None,
                                        limit: Optional[int] = None,
                                        **params) -> SeriesEpisodesResponse:
        """
        :param tv_series_id: Any ID of the series
        :param season_id: Any season ID
        :param ordering: Sorting by a specific value. Possible values: id, released, ru_released, created
        :param direction: Sort order. Possible values: acr, desc
        :param query: Search value. A string longer than two characters.
         For example, "" (title) or  (Kinopoisk ID)
        :param field: Search field. Possible values: title(searches through all *_title fields),
        imdb_id, kinopoisk_id, worldart_id
        :param translation: ID of translation. Get a list of translations - Api.translations.get()
        :param year: Release year
        :param page: Pagination page
        :param limit: Number of results per page
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return SeriesEpisodesResponse(**(await self.api.make_get_request('anime-tv-series/episodes',
                                                                         {"tv_series_id": tv_series_id,
                                                                          "season_id": season_id,
                                                                          "ordering": ordering,
                                                                          "direction": direction,
                                                                          "query": query,
                                                                          "field": field,
                                                                          "translation": translation,
                                                                          "year": year,
                                                                          "page": page,
                                                                          "limit": limit,
                                                                          **params})))

    async def get_show_series(self,
                              ordering: Optional[str] = None,
                              direction: Optional[str] = None,
                              query: Optional[str] = None,
                              field: str = None,
                              translation: int = None,
                              year: Optional[int] = None,
                              page: Optional[int] = None,
                              limit: Optional[int] = None,
                              **params) -> SeriesResponse:
        """
        :param ordering: Sorting by a specific value. Possible values: id, start_date, end_date, created
        :param direction: Sort order. Possible values: acr, desc
        :param query: Search value. A string longer than two characters.
         For example, "" (title) or  (Kinopoisk ID)
        :param field: Search field. Possible values: title(searches through all *_title fields),
        imdb_id, kinopoisk_id, worldart_id
        :param translation: ID of translation. Get a list of translations - Api.translations.get()
        :param year: Release year
        :param page: Pagination page
        :param limit: Number of results per page
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return SeriesResponse(**(await self.api.make_get_request('show-tv-series',
                                                                 {"ordering": ordering,
                                                                  "direction": direction,
                                                                  "query": query,
                                                                  "field": field,
                                                                  "translation": translation,
                                                                  "year": year,
                                                                  "page": page,
                                                                  "limit": limit,
                                                                  **params}
                                                                 )))

    async def get_show_series_seasons(self,
                                      tv_series_id: Optional[int] = None,
                                      ordering: Optional[str] = None,
                                      direction: Optional[str] = None,
                                      page: Optional[int] = None,
                                      limit: Optional[int] = None,
                                      **params) -> SeriesSeasonsResponse:
        """
        :param tv_series_id: Any ID of the show
        :param ordering: Sorting by a specific value. Possible values: id, start_date, end_date, created
        :param direction: Sort order. Possible values: acr, desc
        :param page: Pagination page
        :param limit: Number of results per page
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return SeriesSeasonsResponse(**(await self.api.make_get_request('show-tv-series/seasons',
                                                                        {"tv_series_id": tv_series_id,
                                                                         "ordering": ordering,
                                                                         "direction": direction,
                                                                         "page": page,
                                                                         "limit": limit,
                                                                         **params})))

    async def get_show_series_episodes(self,
                                       tv_series_id: Optional[int] = None,
                                       season_id: Optional[int] = None,
                                       ordering: Optional[str] = None,
                                       direction: Optional[str] = None,
                                       query: Optional[str] = None,
                                       field: str = None,
                                       translation: int = None,
                                       year: Optional[int] = None,
                                       page: Optional[int] = None,
                                       limit: Optional[int] = None,
                                       **params) -> SeriesEpisodesResponse:
        """
        :param tv_series_id: Any ID of the series
        :param season_id: Any season ID
        :param ordering: Sorting by a specific value. Possible values: id, released, ru_released, created
        :param direction: Sort order. Possible values: acr, desc
        :param query: Search value. A string longer than two characters.
         For example, "" (title) or  (Kinopoisk ID)
        :param field: Search field. Possible values: title(searches through all *_title fields), imdb_id, kinopoisk_id
        :param translation: ID of translation. Get a list of translations - Api.translations.get()
        :param year: Release year
        :param page: Pagination page
        :param limit: Number of results per page
        :param params: Any additional parameters. In case they appear in the (not) distant future.
        """
        return SeriesEpisodesResponse(**(await self.api.make_get_request('show-tv-series/episodes',
                                                                         {"tv_series_id": tv_series_id,
                                                                          "season_id": season_id,
                                                                          "ordering": ordering,
                                                                          "direction": direction,
                                                                          "query": query,
                                                                          "field": field,
                                                                          "translation": translation,
                                                                          "year": year,
                                                                          "page": page,
                                                                          "limit": limit,
                                                                          **params})))
