from fastcrud import FastCRUD

from .models.episode import EpisodeBase, Episode
from .models.title import Title

crud_episode = FastCRUD(Episode)
crud_title = FastCRUD(Title)