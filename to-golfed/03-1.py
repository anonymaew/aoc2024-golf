import sys
import re

f = []
for l in sys.stdin:
  f+=re.findall(r'mul\((\d+),(\d+)\)',l)
print(f)
