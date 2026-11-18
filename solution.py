import csv
import io

def solve(value):
    return list(csv.DictReader(io.StringIO(value, newline="")))
