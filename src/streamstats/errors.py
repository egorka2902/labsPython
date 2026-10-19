class StreamStatsError(Exception):
    """ьазовый тип ошибок streamstats"""
    pass

class FormatError(StreamStatsError):
    """ошибки формата данных"""
    pass


class EventError(StreamStatsError):
    """ошибки события"""
    pass


class InvalidEventError(EventError):
    """ошибка невалидного события"""
    pass


class TimeError(StreamStatsError):
    """ошибки времени"""
    pass

