import importlib
import pkgutil

def run_package(package_name):
    package = importlib.import_module(package_name)

    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package_name}.{module_name}")

        if hasattr(module, "run"):
            print(f"\n▶ Running {package_name}.{module_name}")
            module.run()
