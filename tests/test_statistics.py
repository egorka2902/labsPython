import pytest
from streamstats.statistics import events_lvl, top_sources, generate_report
from streamstats.models import Event
from datetime import datetime


def test_events():
    events = [
        Event(timestamp=datetime.fromisoformat("2026-10-07T12:00:00+03:00"), level="INFO", source="loader", message="start"),
        Event(timestamp=datetime.fromisoformat("2026-10-07T12:01:00+03:00"), level="ERROR", source="loader", message="error"),
        Event(timestamp=datetime.fromisoformat("2026-10-07T12:02:00+03:00"), level="INFO", source="parser", message="parse"),
    ]
    
    level_counts, source_counts = events_lvl(events)
    
    assert level_counts == {"INFO": 2, "ERROR": 1}
    assert source_counts == {"loader": 2, "parser": 1}


def test_top():
    source_counts = {"loader": 5, "parser": 3, "validator": 5}
    
    top = top_sources(source_counts, top_n=3)
    assert top == [("loader", 5), ("validator", 5), ("parser", 3)]


def test_generate_report():
    level_counts = {"INFO": 2, "ERROR": 1}
    source_counts = {"loader": 2, "parser": 1}
    
    report = generate_report(level_counts, source_counts, top_n=2, skipped_count=1)
    assert report["levels"] == {"INFO": 2, "ERROR": 1}
    assert report["sources"] == {"loader": 2, "parser": 1}
    assert report["skipped"] == 1
    assert "top_sources" in report
