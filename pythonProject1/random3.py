import random
import sys


for module_name, module_path in sys.modules.items():
    print(module_name, module_path)