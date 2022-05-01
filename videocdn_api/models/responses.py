from pydantic import BaseModel, Field
from typing import Optional, List
from videocdn_api.models.movies import Movie
from videocdn_api.models.series import Serial, Season, Episode
from videocdn_api.models.translations import Translation
from videocdn_api.models.short import Item


class ShortResponse(BaseModel):
    result: bool
    data: List[Item]
    current_page: int
    first_page_url: str
    from_: Optional[int] = Field(..., alias='from')
    last_page: int
    last_page_url: str
    next_page_url: Optional[str]
    prev_page_url: Optional[str]
    path: str
    per_page: int
    to: Optional[int]
    total: int


class MoviesResponse(BaseModel):
    result: bool
    data: List[Movie]
    current_page: int
    first_page_url: str
    from_: Optional[int] = Field(..., alias='from')
    last_page: int
    last_page_url: str
    next_page_url: Optional[str]
    prev_page_url: Optional[str]
    path: str
    per_page: int
    to: Optional[int]
    total: int
    total_count: int


class SeriesResponse(BaseModel):
    result: bool
    data: List[Serial]
    current_page: int
    first_page_url: str
    from_: Optional[int] = Field(..., alias='from')
    last_page: int
    last_page_url: str
    next_page_url: Optional[str]
    prev_page_url: Optional[str]
    path: str
    per_page: int
    to: Optional[int]
    total: int


class SeriesSeasonsResponse(BaseModel):
    result: bool
    data: List[Season]
    current_page: int
    first_page_url: str
    from_: Optional[int] = Field(..., alias='from')
    last_page: int
    last_page_url: str
    next_page_url: Optional[str]
    prev_page_url: Optional[str]
    path: str
    per_page: int
    to: Optional[int]
    total: int


class SeriesEpisodesResponse(BaseModel):
    result: bool
    data: List[Episode]
    current_page: int
    first_page_url: str
    from_: Optional[int] = Field(..., alias='from')
    last_page: int
    last_page_url: str
    next_page_url: Optional[str]
    prev_page_url: Optional[str]
    path: str
    per_page: int
    to: Optional[int]
    total: int


class TranslationsResponse(BaseModel):
    result: bool
    data: List[Translation]
