from dataclasses import dataclass
from .error import CatalogError as err

@dataclass
class MediaItem:
    item_id: str
    name: str
    category: str
    year: int
    mediatype: str
    creator: str
    duration: int

    def __post_init__(self):
        if not (isinstance(self.item_id,str) and self.item_id.strip()):
            raise err("некорректный id")
        if not (isinstance(self.name, str) and self.name.strip()):
            raise err("пустое название")
        if not (isinstance(self.category, str) and self.category.strip()):
            raise err("пустая категория")
        if not (type(self.year) is int and self.year <= 2026):
            raise err("некорректный год")
        if not (isinstance(self.mediatype, str) and self.mediatype.strip()):
            raise err("пустой тип")
        if not (isinstance(self.creator, str) and self.creator.strip()):
            raise err("пустой создатель")
        if not (type(self.duration) is int and self.duration > 0):
            raise err("неправильный формат длительности")
        