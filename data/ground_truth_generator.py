"""
Ground truth generator.
Generates GT markdown from Engine A's cached output.
Run via: python data/ground_truth_generator.py <cache_a_path>
"""
import pathlib, sys

def generate(cache_a_path: str) -> str:
    return pathlib.Path(cache_a_path).read_text().strip()

if __name__ == "__main__":
    print(generate(sys.argv[1]))
