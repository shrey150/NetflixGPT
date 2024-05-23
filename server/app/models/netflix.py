from typing import List, Optional
from pydantic import BaseModel

class Artwork(BaseModel):
    w: int
    h: int
    url: str

class Boxart(BaseModel):
    w: int
    h: int
    url: str

class Storyart(BaseModel):
    w: int
    h: int
    url: str

class Thumbs(BaseModel):
    w: int
    h: int
    url: str

class Bookmark(BaseModel):
    watchedDate: int
    offset: int

class SkipMarkers(BaseModel):
    credit: Optional[dict]
    recap: Optional[dict]
    content: List[dict]

class Episode(BaseModel):
    start: int
    end: int
    synopsis: str
    episodeId: int
    taglineMessages: Optional[dict]
    requiresAdultVerification: bool
    requiresPin: bool
    requiresPreReleasePin: bool
    creditsOffset: int
    runtime: int
    displayRuntime: int
    watchedToEndOffset: int
    autoplayable: bool
    title: str
    id: int
    bookmark: Optional[Bookmark]
    skipMarkers: Optional[SkipMarkers]
    hd: bool
    thumbs: Optional[List[Thumbs]]
    stills: Optional[List[Thumbs]]
    seq: int
    hiddenEpisodeNumbers: bool

class Seasons(BaseModel):
    year: int
    shortName: str
    longName: str
    hiddenEpisodeNumbers: bool
    title: str
    id: int
    seq: int
    episodes: List[Episode]

class UserRating(BaseModel):
    matchScore: Optional[int]
    tooNewForMatchScore: bool
    type: str
    userRating: int

class TrackIds(BaseModel):
    nextEpisode: int
    episodeSelector: int

class Video(BaseModel):
    title: str
    synopsis: str
    rating: str
    artwork: List[Artwork]
    boxart: List[Boxart]
    storyart: List[Storyart]
    type: str
    unifiedEntityId: str
    id: int
    userRating: UserRating
    skipMarkers: SkipMarkers
    currentEpisode: int
    hiddenEpisodeNumbers: bool
    requiresAdultVerification: bool
    requiresPin: bool
    requiresPreReleasePin: bool
    seasons: List[Seasons]

    def __init__(self, **data):
        super().__init__(**data)
        self.seasons.sort(key=lambda season: season.year)

class NetflixPayload(BaseModel):
    version: str
    trackIds: TrackIds
    video: Video
