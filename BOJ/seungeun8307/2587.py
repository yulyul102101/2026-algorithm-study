import sys
import statistics

line = []
for i in range(5):
    line.append(int(sys.stdin.readline()))

mea, med = statistics.mean(line), statistics.median(line)
print(int(mea), int(med))