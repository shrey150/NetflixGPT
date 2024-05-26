from fastcrud import FastCRUD

from .models.episode import Episode
from .models.title import Title
from .models.source import Source
from .models.title_source import TitleSource

crud_episode = FastCRUD(Episode)
crud_title = FastCRUD(Title)
crud_source = FastCRUD(Source)
crud_title_source = FastCRUD(TitleSource)
