from dataclasses import dataclass
from .error import CatalogError as err
FORMAT_VERSION = 1
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
    def todict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
            "year": self.year,
            "mediatype": self.mediatype,
            "creator": self.creator,
            "duration": self.duration,
        }
    @classmethod
    def fromdict(cls,raw):
        fields = ("item_id", "name", "category", "year", "mediatype", "creator", "duration")
        if not isinstance(raw, dict):
            raise TypeError("Не словарь")
        for field in raw:
            if field not in raw:
                raise TypeError(f"не существующее поле {field}")
        return cls(
            item_id=raw["item_id"],
            name=raw["name"],
            category=raw["category"],
            year=raw["year"],
            mediatype=raw["mediatype"],
            creator=raw["creator"],
            duration=raw["duration"],
        )