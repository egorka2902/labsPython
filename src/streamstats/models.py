
from datetime import *
from dataclasses import dataclass

@dataclass
class Event:
    """Модель события лога."""
    timestamp: datetime  
    level: str 
    source: str      
    message: str