import csv
from collections import defaultdict
from random import choices

import numpy as np

def bootstrap_ci(x, repetitions = 1000, alpha = 0.05): 
    
    size = len(x) 
    
    means = np.array([
        sum(choices(x, k=size)) / size
        for i in range(repetitions)
    ])
    
    left = np.percentile(means, alpha/2 * 100)
    right = np.percentile(means, 100-alpha/2 * 100)
    point_est = means.mean()
    return round(point_est, 2), round(left,2), round(right,2)


with open('results/tts_experiment/mushra.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lines = [l for l in csv_reader]

stimulus = set([l[4] for l in lines[1:]])
results = defaultdict(list)  # contain samples for each models

for l in lines[1:]:
    results[l[4]].append(float(l[5]))
    

fmt = "|{:<25}" * 4 + "|"
print('Total respondents: ', len(lines[1:])/(10*len(results.keys())))
print(fmt.format('model', 'MOS', 'left', 'right'))
print('|-------------------------'*4 + "|")
for k, v in results.items():
    m, l, r = bootstrap_ci(v)
    print(fmt.format(k, m, l, r))
