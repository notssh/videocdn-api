from pydantic import BaseModel
from typing import Optional, List
import datetime
from videocdn_api.models.translations import TranslationSeriesAlt


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
    translation: TranslationSeriesAlt


class Episode(BaseModel):
    id: int
    tv_series_id: int
    season_id: int
    num: Optional[str]
    season_num: int
    ru_title: Optional[str]
    en_title: Optional[str]
    orig_title: Optional[str]
    imdb_id: Optional[str]
    kinopoisk_id: Optional[int]
    default_media_id: Optional[int]
    worldart_id: Optional[int]
    created: Optional[datetime.datetime]
    released: Optional[datetime.datetime]
    ru_released: Optional[datetime.datetime]
    media: List[Media]


class Season(BaseModel):
    id: int
    tv_series_id: int
    num: Optional[str]
    ru_title: Optional[str]
    en_title: Optional[str]
    orig_title: Optional[str]
    episode_count: int
    start_date: Optional[datetime.datetime]
    end_date: Optional[datetime.datetime]
    created: Optional[datetime.datetime]
    episodes: List[Episode]


class Serial(BaseModel):
    id: int
    ru_title: Optional[str]
    en_title: Optional[str]
    orig_title: Optional[str]
    imdb_id: Optional[str]
    kinopoisk_id: Optional[int]
    default_media_id: Optional[int]
    worldart_id: Optional[int]
    last_episode_id: int
    created: Optional[datetime.datetime]
    released: Optional[datetime.datetime]
    updated: Optional[datetime.datetime]
    blocked: bool
    content_id: Optional[int]
    content_type: str
    country_id: Optional[int]
    preview_iframe_src: str
    iframe_src: str
    iframe: str
    translations: List[TranslationSeriesAlt]
    episodes: List[Episode]
