
from errors import InvalidEventError as err1
from datetime import *


def validate_csv(reader):
    fields = {"timestamp", "level", "source", "message"}
    levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
    for row in reader:
        for place in fields:
            if place not in row:
                raise err1(f'отсутствует поле {place}')
        if row["level"] not in levels:
            r = row["level"]
            raise err1(f'неккоректный level {r}')
        try:
            tim = datetime.fromisoformat(row["timestamp"])
        except Exception as err:
            raise err1(f'невозможно перевести в iso формат, error : {err}')
        if len(str(row["source"])) <= 0:
            raise err1(f'пустая строка в поле source')
        yield row