from my_package.main import func


# It gives an error because the import statement in `my_package/main.py` is trying to import from `module_a`, `module_b`, and `module_c`, which are not in the same directory as `my_package`.
#   File "/Users/carlohcs/Documents/repository/100-days-of-code-python-pro-bootcamp-for-2022/days/12-import-from-submodules/main.py", line 1, in <module>
#     from my_package.main import func
#   File "/Users/carlohcs/Documents/repository/100-days-of-code-python-pro-bootcamp-for-2022/days/12-import-from-submodules/my_package/main.py", line 1, in <module>
#     from module_a.script_a import var_a
# ModuleNotFoundError: No module named 'module_a'
# func()

# So in the `my_package/main.py`, we need to use relative imports to import from the submodules correctly.
# from .module_a.script_a import var_a
# from .module_b.script_b import var_b
# from .module_c.script_c import var_c

# or

# from my_package.module_a.script_a import var_a
# from my_package.module_b.script_b import var_b
# from my_package.module_c.script_c import var_c

# But this will only work if the `my_package` is in the Python path. If it's not, we need to add it to the Python path.
# Let's create a `__init__.py` file in the `my_package` directory to make it a package.

# Also, maybe it's necessary to use the setuptools package to install the package correctly, so we can use it in the main script.
# pip install setuptools

# Install the package using setuptools
# This will allow us to use the package in the main script without any issues.
# pip install -e .
func()