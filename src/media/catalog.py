from .error import CatalogError,TypeError


from .models import MediaItem


class Catalog:
    def __init__(self):
        self.items = {}

    def add(self, item):
        if not (isinstance(item,MediaItem)):
            raise TypeError("объект класса не MediaItem")
        if item.item_id in self.items:
            raise CatalogError("id уже существует")
        self.items[item.item_id] = item

    def get(self, itemid):
        if itemid not in self.items:
            raise CatalogError("id не найден")
        return self.items[itemid]

    def remove(self, itemid):
        if itemid not in self.items:
            raise CatalogError("объекта не существует")
        del self.items[itemid]
    def find_cat(self, cat):
        res = []
        for item in self.items.values():
            if cat.lower() == item.category:
                res.append(item)

        if len(res) == 0:
            raise CatalogError("0 совпадений по категориям")
        return res

    def find_name(self, name):
        res = []
        for item in self.items.values():
            if name.lower() == item.name:
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