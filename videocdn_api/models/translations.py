from pydantic import BaseModel
from typing import Optional


class Translation(BaseModel):
    id: int
    title: str
    priority: int
    short_title: str
    smart_title: str
    shorter_title: str


class TranslationAlt(BaseModel):
    id: int
    title: str
    priority: int
    source_quality: Optional[str]
    max_quality: Optional[int]
    iframe_src: Optional[str]
    iframe: Optional[str]
    short_title: str
    smart_title: str
    shorter_title: str


class TranslationSeriesAlt(BaseModel):
    id: int
    title: str
    priority: int
    episodes_count: Optional[int]
    source_quality: Optional[str]
    max_quality: Optional[int]
    iframe_src: Optional[str]
    iframe: Optional[str]
    short_title: str
    smart_title: str
    shorter_title: str
