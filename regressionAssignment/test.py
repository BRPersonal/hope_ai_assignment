import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.utils import generate_parameter_combinations

absPath = os.path.abspath(__file__)
print(absPath)
print(os.path.dirname(absPath))
print(os.path.dirname(os.path.dirname(absPath)))

param_dict = {
    "C": [10,100,500,1000,2000,3000],
    "kernel": ["linear", "poly", "rbf", "sigmoid"]
}

combinations = generate_parameter_combinations(param_dict)
print(f"length={len(combinations)},combinations={combinations}")