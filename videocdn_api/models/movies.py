from pydantic import BaseModel, Field
from typing import Any, Optional, List, Union
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


class Movie(BaseModel):
    id: int
    ru_title: Optional[str]
    en_title: Optional[str]
    orig_title: Optional[str]
    imdb_id: Optional[str]
    kinopoisk_id: Optional[int]
    default_media_id: Optional[int]
    worldart_id: Optional[int]
    created: Optional[datetime.datetime]
    released: Optional[datetime.datetime]
    updated: Optional[datetime.datetime]
    blocked: bool
    content_id: Optional[int]
    content_type: str
    country_id: Optional[int]
    media: List[Media]
    preview_iframe_src: str
    iframe_src: str
    iframe: str
    translations: List[TranslationAlt]
    year: Optional[datetime.date]


