import os
import importlib


def import_submodules(package_dir, package_name):
    """
    Recursively imports all modules in the given package directory.

    :param package_dir: Path to the directory of the package
    :param package_name: Name of the package
    """
    for entry in os.listdir(package_dir):
        entry_path = os.path.join(package_dir, entry)
        if os.path.isdir(entry_path) and os.path.exists(os.path.join(entry_path, "__init__.py")):
            # Recursively import subpackages
            import_submodules(entry_path, f"{package_name}.{entry}")
        elif entry.endswith(".py") and entry != "__init__.py":
            # Import the module
            module_name = entry[:-3]  # Remove the .py extension
            importlib.import_module(f"{package_name}.{module_name}")


# Set the base directory and package name
base_dir = os.path.dirname(__file__)
base_package = os.path.basename(base_dir)

# Import all submodules recursively
import_submodules(base_dir, base_package)
