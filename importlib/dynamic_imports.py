"""
The importlib module supports the ability to import a module that is passed to
it as a string.
"""
# importer.py}
import importlib
import foo


def dynamic_import(module):
    return importlib.import_module(module)


if __name__ == "__main__":
    module = dynamic_import("foo")
    module.main()

    module_two = dynamic_import("bar")
    module_two.main()
