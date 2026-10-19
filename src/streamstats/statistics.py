from collections import defaultdict
from datetime import datetime

def events_lvl(events):
    """агрегация событий по уровням и лвлам"""
    level_counts = defaultdict(int)
    counts = defaultdict(int)
    
    for event in events:
        if event.level:
            level_counts[event.level] += 1
        if event.source:
            counts[event.source] += 1
            
    return dict(level_counts), dict(counts)

def sortk(s):
    """ключ сортировки сначала количество  потом имя"""
    return (s[-1],s[0])

def top_sources(counts, top_n=5):
    """возвращает топ источников по количеству событий."""
    sorted_s = sorted(counts.items(),key=sortk)
    return sorted_s[:top_n]

def generate_report(level_counts, counts, top_n=5, skipped_count=0):
    """ отчёт в виде словаря"""
    return {
        "levels": level_counts,
        "sources": counts,
        "top_sources": dict(top_sources(counts, top_n)),
        "skipped": skipped_count
    }
