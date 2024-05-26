from sqlmodel import SQLModel, Field

class TitleSource(SQLModel, table=True):
    '''Junction table for many-to-many relationship between titles and sources.'''
    __tablename__ = "titles_sources"
    title_id: int = Field(foreign_key="titles.id", primary_key=True)
    source_id: int = Field(foreign_key="sources.id", primary_key=True)

class TitleSourceCreate(TitleSource):
    pass