import csv
from collections import defaultdict

with open('results/tts_experiment/mushra.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lines = [l for l in csv_reader]

stimulus = set([l[4] for l in lines[1:]])
results = defaultdict(float)

for l in lines[1:]:
    results[l[4]] += float(l[5])
    
results = {k: v/len(lines[1:]) * len(results.keys()) for k, v in results.items()}

for k, v in results.items():
    print(k, ': ', v)
