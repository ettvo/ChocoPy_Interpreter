import shutil
import subprocess
import os
import tempfile
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/precomputed.json", "r") as r:
    precomputed = json.load(r)

def get_speedup(p: str, input: str, out: str):
    with tempfile.TemporaryDirectory() as tmpdirname:
        try:
            shutil.copy(f"{dir_path}/{p}", f"{tmpdirname}/program.py")
            shutil.copy(f"{dir_path}/{input}", f"{tmpdirname}/program.py.in")
            shutil.copy(f"{dir_path}/{out}", f"{tmpdirname}/program.py.ast.typed.s.result")
        except FileNotFoundError:
            print(f"Could not find the program ({p}), input ({input}), or output ({out}) file")
            return 0

        try:
            sample_test_output = subprocess.run([
                'java',
                '-Xmx1g',
                '-cp', 'chocopy-ref.jar:target/assignment.jar',
                'chocopy.ChocoPy',
                '--pass=rrs',
                "--run",
                "--dir",
                f"{tmpdirname}",
                "--test"
            ], stdout=subprocess.PIPE, timeout=5).stdout.decode('utf-8').split('\n')

            sample_test_summary = sample_test_output[-2]

            passing_sample_tests = int(sample_test_summary.split()[1])
            failing_sample_tests = int(sample_test_summary.split()[3])

            if passing_sample_tests == 1 and failing_sample_tests == 0:
                cycle_count_student_line = subprocess.run([
                    'java',
                    '-Xmx1g',
                    '-cp', 'chocopy-ref.jar:target/assignment.jar',
                    'chocopy.ChocoPy',
                    '--pass=rrs',
                    "--run",
                    "--profile",
                    "--dir",
                    f"{tmpdirname}"
                ], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
                cycle_count_student = int(cycle_count_student_line[-2].split(" = ")[-1])
                
                cycle_count_reference = precomputed[input]

                print(f"Got speedup of {cycle_count_reference / cycle_count_student} for {p} with input {input} and output {out}")
                return cycle_count_reference / cycle_count_student
            else:
                print(f"Student compiler produced wrong output for ({p}), input ({input}), and output ({out}) file")
                return 0
        except subprocess.TimeoutExpired:
            print(f"Student compiler timed out (> 5 seconds) for ({p}), input ({input}), and output ({out}) file")
            return 0

all_benchmarks = []
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(".py") and not file.endswith("bench_all.py"):
            if precomputed[f"{file}.in"] < 500000:
                all_benchmarks.append(
                    get_speedup(file, f"{file}.in", f"{file}.ast.typed.s.result")
                )

pass_count = len([x for x in all_benchmarks if x != 0])
all_count = len(all_benchmarks)

# get top 80% of benchmarks
all_benchmarks.sort()
all_benchmarks = all_benchmarks[::-1]
all_benchmarks = all_benchmarks[:round(0.8 * len(all_benchmarks))]

if 0 in all_benchmarks:
    print(f"Warning: fewer than 80\% of benchmarks passed (only {pass_count}/{all_count} passed)")
    all_benchmarks = [x for x in all_benchmarks if x != 0]

geomean = 1
for benchmark in all_benchmarks:
    geomean *= benchmark
geomean = geomean ** (1.0 / len(all_benchmarks))
print("Geometric mean of speedups: ", geomean)
