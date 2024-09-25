# magicMahler/__init__.py

# Import submodules
from .polytope import Polytope
from .auxiliary_functions import aux1, aux2, numerical_gradient, gradient_descent, safe_divide, double_integration
from .graham_scan import graham_scan, Point
from .mahler_translation import update_plots

# Define package-level constants
VERSION = "1.0"
AUTHOR = "Vlassis Mastrantonis"
EMAIL = "vmastr@icloud.com"

# Define the __all__ variable to control what symbols are exported when importing the package
__all__ = [
    # From polytope.py
    "Polytope",

    # From auxiliary_functions.py
    "aux1", "aux2", "numerical_gradient", "gradient_descent", "safe_divide", "double_integration",

    # From graham_scan.py
    "graham_scan", "Point",

    # From mahler_translation.py
    "update_plots",

    # Package-level constants
    "VERSION", "AUTHOR", "EMAIL"
]
