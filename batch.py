import json
from pprint import pp
from config import workdir, number


problem_ranges: dict[int, tuple[int, int]] = {}

problem_number = 510
last_problem_number = 1062
# for i in range(119, 120):
for i in range(118, 233 + 1):
    with open(f"{workdir}/pars/{i}.json") as f:
        pars = json.load(f)
    s = ""
    for par in pars:
        s += par[1]
    # print(s)
    a = problem_number
    search_string = str(problem_number)
    while any(str(i) in s for i in range(problem_number, problem_number + 6)) and problem_number <= last_problem_number:
        problem_number += 1
        search_string = str(problem_number)
    b = problem_number - 1
    if b >= a:
        problem_ranges[i] = (a, b)
a, b = problem_ranges[i]
b += 1
problem_ranges[i] = (a, b)

json_object = json.dumps(problem_ranges, indent=4).replace("-1", "")
with open(f"{workdir}/problem_ranges.json", "w") as outfile:
    outfile.write(json_object)
