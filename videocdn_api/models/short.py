from pydantic import BaseModel, Field
from typing import Optional, List
import datetime
from videocdn_api.models.translations import TranslationAlt


class Quality(BaseModel):
    id: int
    url: str
    resolution: int
    media_id: int


class Media(BaseModel):
    id: int
    translation_id: int
    content_id: int
    content_type: str
    tv_series_id: Optional[int]
    source_quality: Optional[str]
    max_quality: Optional[int]
    path: str
    duration: int
    created: Optional[datetime.datetime]
    accepted: Optional[datetime.datetime]
    deleted_at: Optional[datetime.datetime]
    blocked: bool
    qualities: List[Quality]
    translation: TranslationAlt


class Item(BaseModel):
    id: int
    title: Optional[str]
    orig_title: Optional[str]
    imdb_id: Optional[str]
    kinopoisk_id: Optional[int] = Field(..., alias='kp_id')
    default_media_id: Optional[int]
    worldart_id: Optional[int]
    type: str
    add: Optional[datetime.datetime]
    update: Optional[datetime.datetime]
    quality: Optional[str]
    translations: List[str]
    translation: Optional[str]
    seasons_count: Optional[int]
    episodes_count: Optional[int]
    episodes: Optional[int]
    iframe_src: str
    year: Optional[datetime.date]


