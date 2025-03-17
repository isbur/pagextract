import json
from typing import Any
from config import workdir

with open(f"{workdir}/problem_ranges_edited.json", "r") as f:
    problem_ranges: dict[int, list[int]] = json.load(f)

A = list(problem_ranges.values())
for i, range in enumerate(A):
    if i == len(problem_ranges) - 1:
        continue
    if A[i+1][0] - range[1] != 1:
        print(f"Wrong bounds between {i + 1} and {i + 2}")