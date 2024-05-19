from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class SkipMarker(BaseModel):
    start: Optional[int]
    end: Optional[int]

class Bookmark(BaseModel):
    watchedDate: int
    offset: int

class LiveEvent(BaseModel):
    hasLiveEvent: bool

class TaglineMessages(BaseModel):
    tagline: str
    classification: str

class Thumb(BaseModel):
    w: int
    h: int
    url: str

class Still(BaseModel):
    w: int
    h: int
    url: str

class Episode(BaseModel):
    start: int
    end: int
    synopsis: str
    episodeId: int
    liveEvent: LiveEvent
    taglineMessages: TaglineMessages
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
    bookmark: Bookmark
    skipMarkers: Dict[str, SkipMarker | List[str]]
    hd: bool
    thumbs: List[Thumb]
    stills: List[Still]
    seq: int
    hiddenEpisodeNumbers: bool

class Season(BaseModel):
    year: int
    shortName: str
    longName: str
    hiddenEpisodeNumbers: bool
    title: str
    id: int
    seq: int
    episodes: List[Episode]

class UserRating(BaseModel):
    matchScore: int
    tooNewForMatchScore: bool
    type: str
    userRating: int

class Artwork(BaseModel):
    w: int
    h: int
    url: str

class Video(BaseModel):
    title: str
    synopsis: str
    rating: str
    artwork: List[Artwork]
    boxart: List[Artwork]
    storyart: List[Artwork]
    type: str
    unifiedEntityId: str
    id: int
    userRating: UserRating
    skipMarkers: Dict[str, SkipMarker | List[str]]
    currentEpisode: int
    hiddenEpisodeNumbers: bool
    requiresAdultVerification: bool
    requiresPin: bool
    requiresPreReleasePin: bool
    seasons: List[Season]

class TrackIds(BaseModel):
    nextEpisode: int
    episodeSelector: int

class NetflixPayload(BaseModel):
    version: str
    trackIds: TrackIds
    video: Video

# Example instantiation:
example_payload = NetflixPayload(
    version="2.1",
    trackIds=TrackIds(
        nextEpisode=200257858,
        episodeSelector=200257859
    ),
    video=Video(
        title="Better Call Saul",
        synopsis="This Emmy-nominated prequel to \"Breaking Bad\" follows small-time attorney Jimmy McGill as he transforms into morally challenged lawyer Saul Goodman.",
        rating="TV-MA",
        artwork=[
            Artwork(w=1280, h=720, url="https://example.com/artwork1"),
            Artwork(w=1280, h=720, url="https://example.com/artwork2")
        ],
        boxart=[
            Artwork(w=426, h=607, url="https://example.com/boxart1"),
            Artwork(w=284, h=405, url="https://example.com/boxart2")
        ],
        storyart=[
            Artwork(w=1280, h=720, url="https://example.com/storyart1"),
            Artwork(w=1920, h=1080, url="https://example.com/storyart2")
        ],
        type="show",
        unifiedEntityId="Video:80021955",
        id=80021955,
        userRating=UserRating(
            matchScore=99,
            tooNewForMatchScore=True,
            type="thumb",
            userRating=0
        ),
        skipMarkers={
            "credit": SkipMarker(start=None, end=None),
            "recap": SkipMarker(start=None, end=None),
            "content": []
        },
        currentEpisode=80084671,
        hiddenEpisodeNumbers=False,
        requiresAdultVerification=False,
        requiresPin=False,
        requiresPreReleasePin=False,
        seasons=[
            Season(
                year=2015,
                shortName="S1",
                longName="Season 1",
                hiddenEpisodeNumbers=False,
                title="Season 1",
                id=80021755,
                seq=1,
                episodes=[
                    Episode(
                        start=1454313600000,
                        end=1808031600000,
                        synopsis="Struggling lawyer Jimmy McGill tries to leave his seedy past behind him, but old habits die hard when a big opportunity presents itself.",
                        episodeId=80021956,
                        liveEvent=LiveEvent(hasLiveEvent=False),
                        taglineMessages=TaglineMessages(tagline="", classification="REGULAR"),
                        requiresAdultVerification=False,
                        requiresPin=False,
                        requiresPreReleasePin=False,
                        creditsOffset=3140,
                        runtime=3191,
                        displayRuntime=3191,
                        watchedToEndOffset=3078,
                        autoplayable=True,
                        title="Uno",
                        id=80021956,
                        bookmark=Bookmark(watchedDate=1570568348745, offset=3151),
                        skipMarkers={
                            "credit": SkipMarker(start=361000, end=372539),
                            "recap": SkipMarker(start=0, end=0),
                            "content": []
                        },
                        hd=True,
                        thumbs=[
                            Thumb(w=350, h=197, url="https://example.com/thumb1")
                        ],
                        stills=[
                            Still(w=1920, h=1080, url="https://example.com/still1")
                        ],
                        seq=1,
                        hiddenEpisodeNumbers=False
                    )
                ]
            )
        ]
    )
)
