## Лабораторная N2 (анализ событий streamstats)


## Структура проекта
- src/streamstats содержит все файлы для обработки(cli,ошибки,валидация,парсер,статистика формируемая в отчет, модель событий Event)
- src/tests(pytest тесты работы программы)

# error.py
ошибки
`StreamStatsError` - базовый ошибки
 `FormatError` - ошибки формата
  `EventError` - ошибка отдельного событиая
   `InvalidEventError` - ошибка валидации
    `TimeError ` - ошибка времени

# models.py
класс Event с 4 полями: timestamp, level, source, message

# validate.py
валидация строк, проверяет:
1) есть все 4 поля timestamp, level, source, message
2) level содержит один из  элементов : `DEBUG, INFO, WARNING, ERROR, CRITICAL`
3) попытка преобразования времени в iso формат 
4) source не пустое

# parsers.py
парсинг jsonl через json,csv файлов

вызывает валидация для строк, возврат Event

# statistics.py
статистика и отчёты
events_lvl - суммирование и обобщение 
sortk - возвращает кортеж по количесту имени
top_sources - сортирует источники и берет первые top_n
generate_report - собирает итоговый словарь топ 5(n) и сколько пропущенно skipped

это все и записывается в итоговый json файл

# __main__.py
основной файл для обработки cli и вызова всего остального —(длинный дефис через win+. поставил НЕ ИИ) входная точка программы 
1) настраивает какие команды могут приниматься
2) разбирает введенные аргументы
3) вызов ф-ии analyze или help_func

разбирает вводные данные где:

args.input — списков файлов
args.format — формат файла (csv|jsonl)
args.output — имя файла отчета
args_skipinvalid — True|FAlse
args.command — analyze или help


ф-ии:
parse_skip(path, fmt, skip_invalid=False):
    вся работа с файлом через Try чтобы не заврешалась программа

    выбор парсера if fmt == 'jsonl'
    for event in parsed_events: events.append(event) добавляем событие

analyze
    читает файлы,собирает статистику и делает отчёт
    out_path = Path(args.output) преобразует строку в тип Path 