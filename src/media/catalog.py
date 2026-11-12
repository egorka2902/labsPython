from .error import CatalogError,CatalogTypeError,NotFoundErr,FileErr,DublicateError
import json, os

from .models import MediaItem, FORMAT_VERSION


class Catalog:
    def __init__(self):
        self.items = {}

    def add(self, item):
        if not (isinstance(item,MediaItem)):
            raise CatalogTypeError("объект класса не MediaItem")
        if item.item_id in self.items:
            raise DublicateError("id уже существует")
        self.items[item.item_id] = item

    def get(self, itemid):
        if itemid not in self.items:
            raise NotFoundErr("id не найден")
        return self.items[itemid]

    def remove(self, itemid):
        if itemid not in self.items:
            raise CatalogError("объекта не существует")
        del self.items[itemid]
    def find_by_category(self, cat):
        res = []
        for item in self.items.values():
            if cat.lower() == item.category.lower():
                res.append(item)

        if len(res) == 0:
            raise CatalogError("0 совпадений по категориям")
        return res

    def find_by_name(self, name):
        res = []
        for item in self.items.values():
            if name.lower() in item.name.lower():
                res.append(item)
        if len(res) == 0:
            raise CatalogError("0 совпадений по названиям")
        return res

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items.values())

    def __contains__(self, item_id):
        return item_id in self.items

    def save(self, path):
        data = {"format_version" : FORMAT_VERSION, "items": [item.todict() for item in self.items.values()]}
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data,f, ensure_ascii=False, indent=2)#ensure_ascii норм чтение, indent отступы для читаемости
        except FileNotFoundError as e:
            raise NotFoundErr("файл не найден")
    def load(self, path):
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise NotFoundErr("файл не найден")
        except json.JSONDecodeError as e:
            raise FileErr("нечитаемый файл")
        if not isinstance(data,dict):
            raise CatalogTypeError("не словарь")
        if data.get("format_version") != FORMAT_VERSION:
            raise FileErr("неправильная версия")

        items_dict = data.get("items")
        if items_dict is None:
            raise CatalogTypeError("нету items")
        if not isinstance(items_dict, list):
            raise CatalogTypeError("items не список")
        nrw_items = {}

        for i, raw in enumerate(items_dict):
            try:
                item = MediaItem.fromdict(raw)
            except CatalogError as err:
                raise CatalogTypeError("невалидный объект")
            if item.item_id in nrw_items:
                raise DublicateError(f"дубликат id: {item.item_id}")
            nrw_items[item.item_id] = item
        self.items = nrw_items