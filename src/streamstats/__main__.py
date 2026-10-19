from argparse import *
import json
import sys
import logging
from pathlib import Path
from streamstats.parsers import parse_csv, parse_jsonl
from streamstats.statistics import events_lvl, generate_report
from streamstats.errors import StreamStatsError, InvalidEventError,FormatError

logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')

def parse_skip(path, fmt, skip_invalid=False):
    """парсинг с пропуском невалидных строк"""
    skipped_count = 0
    events = []
    if fmt == 'jsonl' and str(path)[-5:] != 'jsonl':
        raise FormatError('ошибка форматов')
    if fmt == 'csv' and str(path)[-3:] != 'csv':
        raise FormatError('ошибка форматов')
    try:
        if fmt == 'jsonl':
            parsed_events = parse_jsonl(path)
        else:
            parsed_events = parse_csv(path)
            
        for event in parsed_events:
            events.append(event)
            
    except InvalidEventError as e:
        if skip_invalid:
            logging.warning(f"невалидная строка/запись скип {e}")
            skipped_count += 1
        else:
            raise StreamStatsError(f"ошибка события: {e}")
    except StreamStatsError as e:
        raise StreamStatsError(f"ошибка потока: {e}")
    except Exception as e:
        raise StreamStatsError(f"нежданная ошибка: {e}")
        
    return events, skipped_count

def analyze(args):
    """анализ csv или jsonl файла, сохранение отчёта"""
    try:
        out_path = Path(args.output)   # куда пишем отчёт (в путь из --output)
        all_events = []                # сюда кладём события из всех файлов
        total_skipped = 0              # число пропущенных строк
        for input_file in args.input:  #← перебираем ВСЕ переданные файлы
            input_path = Path(input_file)
            events, skipped = parse_skip(input_path, args.format, args.skip_invalid) #читаем один файл
            all_events.extend(events)          # добавляем прочитанные события
            total_skipped += skipped           # суммируем пропущенные
        
        level_counts, source_counts = events_lvl(all_events) # агрегация
        report = generate_report(level_counts, source_counts, top_n=5, skipped_count=total_skipped)
        
        with out_path.open('w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
            
        print(f"отчёт сохранён в {out_path}")
    
    except StreamStatsError as e:
        print(f"ошибка: {e}")
    except Exception as e:
        print(f"ошибка: {e}")

def help_func(args):
    print('python -m streamstats analyze INPUT [INPUT ...] --format csv|jsonl --output REPORT.json [--skip-invalid]')

def main():
    """парсер входных данных CLI"""
    parser = ArgumentParser(prog="streamstats", description="Анализатор потоков событий")
    
    sub = parser.add_subparsers(dest='command', help='доступные команды')
    
    analyze_p = sub.add_parser("analyze", help="анализ csv или jsonl файла")
    analyze_p.add_argument("input", nargs='+', help="путь к csv или jsonl файлу (можно несколько)")
    analyze_p.add_argument("--format", required=True, choices=['csv', 'jsonl'], help="формат входного файла")
    analyze_p.add_argument("--output", required=True, help="имя файла отчёта (сохраняется в текущей папке)")
    analyze_p.add_argument("--skip-invalid", action="store_true", help="пропуск невалидных строк")
    analyze_p.set_defaults(func=analyze)
    
    help_p = sub.add_parser("help")
    help_p.set_defaults(func=help_func)
    
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
