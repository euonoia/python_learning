import importlib.util
import os
import sys

# Change ONLY this when practicing
CURRENT_PROBLEM = "../primitivesvsreferences/manualdeepclone.py"

def run():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    module_path = os.path.normpath(os.path.join(base_dir, CURRENT_PROBLEM))

    if not os.path.exists(module_path):
        print("❌ Problem file not found:", module_path)
        sys.exit(1)

    spec = importlib.util.spec_from_file_location("problem", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "solve"):
        print("❌ Missing `solve()` function.")
        sys.exit(1)

    print("Running:", CURRENT_PROBLEM)
    print("Output:", module.solve())

if __name__ == "__main__":
    run()
