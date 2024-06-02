from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl
from datetime import datetime

# CrunchyRoll PyDantic Model
class Version(BaseModel):
    audio_locale: str
    guid: str
    is_premium_only: bool
    media_guid: str
    original: bool
    season_guid: str
    variant: str

class ExtendedMaturityRating(BaseModel):
    level: str
    rating: str
    system: str

class AdBreak(BaseModel):
    offset_ms: int
    type: str

class Thumbnail(BaseModel):
    height: int
    source: HttpUrl
    type: str
    width: int

class Images(BaseModel):
    thumbnail: List[List[Thumbnail]]

class EpisodeData(BaseModel):
    available_offline: bool
    episode_number: Optional[int]
    media_type: str
    availability_starts: datetime
    recent_audio_locale: str
    channel_id: str
    id: str
    availability_ends: datetime
    slug_title: str
    season_title: str
    is_clip: bool
    title: str
    upload_date: datetime
    listing_id: str
    audio_locale: str
    is_premium_only: bool
    duration_ms: int
    seo_description: str
    versions: List[Version]
    closed_captions_available: bool
    production_episode_id: str
    extended_maturity_rating: ExtendedMaturityRating
    content_descriptors: List[str]
    streams_link: str
    episode: str
    season_slug_title: str
    series_title: str
    images: Images
    season_display_number: str
    next_episode_id: Optional[str] = None
    subtitle_locales: List[str]
    recent_variant: str
    availability_notes: str
    seo_title: str
    sequence_number: Union[int, float]
    series_slug_title: str
    premium_available_date: datetime
    free_available_date: datetime
    season_sequence_number: int
    is_mature: bool
    ad_breaks: List[AdBreak]
    eligible_region: str
    season_id: str
    next_episode_title: Optional[str] = None
    is_dubbed: bool
    description: str
    season_tags: List[str]
    slug: str
    season_number: int
    hd_flag: bool
    maturity_ratings: List[str]
    available_date: Optional[datetime]
    premium_date: Optional[datetime]
    identifier: str
    mature_blocked: bool
    is_subbed: bool
    episode_air_date: datetime
    series_id: str

class SeasonsMeta(BaseModel):
    versions_considered: bool

class SeasonsData(BaseModel):
    total: int
    data: List[EpisodeData]
    meta: SeasonsMeta

class CrunchyPayload(BaseModel):
    title: str
    current_episode: str
    lang: str
    synopsis: str
    seasons: List[SeasonsData]