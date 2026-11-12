class CatalogError(Exception):
    pass

class CatalogTypeError(CatalogError):
    pass

class DublicateError(CatalogError):
    pass
class NotFoundErr(CatalogError):
    pass

class FileErr(CatalogError):
    pass