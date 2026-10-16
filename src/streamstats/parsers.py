import csv
import json
from pathlib import *
from models import Event
from validate import validate_csv
from datetime import *






def parse_csv(path):
    path = Path(path)
    with path.open(mode='r',encoding='utf-8', newline = '') as file:
        reader = csv.DictReader(file)
        for validated_row in validate_csv(reader):
            yield Event(
                timestamp=datetime.fromisoformat(validated_row["timestamp"]),
                level=validated_row["level"],
                source=validated_row["source"],
                message=validated_row["message"]
            )


def parse_json(path):
    path = Path(path)
    with path.open(mode = 'r',encoding='utf-8', newline='') as file:
        reader = json.load(file)
        for validated_row in validate_csv(reader):
            yield Event(
                timestamp=datetime.fromisoformat(validated_row["timestamp"]),
                level=validated_row["level"],
                source=validated_row["source"],
                message=validated_row["message"]
            )

def jsonl_reader(file):
    for line in file:
        line = line.strip()
        if line:  
            yield json.loads(line)

def parse_jsonl(path):
    path = Path(path)
    with path.open(mode='r', encoding='utf-8') as file:
        
        for validated_row in validate_csv(jsonl_reader(file)):
            yield Event(
                timestamp=datetime.fromisoformat(validated_row["timestamp"]),
                level=validated_row["level"],
                source=validated_row["source"],
                message=validated_row["message"]
            )
