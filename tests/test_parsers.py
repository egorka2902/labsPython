import pytest
from io import StringIO
from streamstats.parsers import parse_csv, parse_jsonl, jsonl_reader
from streamstats.models import Event

from pathlib import Path
import tempfile #ВРЕМЕННЫЙ ФАЙЛ чтоб правилтно проверить

def test_parse_csv_valid():
    try:    
        csv_text = 'timestamp,level,source,message\n2026-10-07T12:00:00+03:00,INFO,loader,start reading\n2026-10-07T12:01:00+03:00,ERROR,loader,file not found'
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv',delete=False, encoding='utf-8') as f:
            f.write(csv_text)
            temp_path = f.name
        
        events = list(parse_csv(temp_path))
        assert len(events) == 2
        assert events[0].level == "INFO"
        assert events[0].source == "loader"
        assert events[1].level == "ERROR"
    finally:
        Path(temp_path).unlink() #удаление файла после работы с ним


def test_parse_jsonl_valid():
    try:
        jsonl_text = '''{"timestamp":"2026-10-07T12:00:00+03:00","level":"INFO","source":"loader","message":"start"}
    {"timestamp":"2026-10-07T12:01:00+03:00","level":"ERROR","source":"loader","message":"error"}'''
        with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl',delete=False, encoding='utf-8') as f:
            f.write(jsonl_text)
            temp_path = f.name
        events = list(parse_jsonl(temp_path))
        assert len(events) == 2
        assert events[0].level == "INFO"
        assert events[1].level == "ERROR"
    finally:
        Path(temp_path).unlink() #удаление файла после работы с ним



def test_jsonl_reader():
    jsonl_text = '{"timestamp":"2026-10-07T12:00:00+03:00","level":"INFO","source":"loader","message":"start"}\n{"timestamp":"2026-10-07T12:01:00+03:00","level":"ERROR","source":"loader","message":"error"}'
    reader = jsonl_reader(StringIO(jsonl_text))
    rows = list(reader)
    assert len(rows) == 2
    assert rows[0]["level"] == "INFO"
    assert rows[1]["level"] == "ERROR"
