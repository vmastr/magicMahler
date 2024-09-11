# MahlerMagic/__init__.py

# Import submodules to make them accessible when importing the package
from auxiliary_functions import *
from .polytope import *
from .graham_scan import *
from .mahler import *
from .visualization import *
from .polytope import Polytope

# Define package-level constants
VERSION = "1.0"
AUTHOR = "Vlassis Mastrantonis"
EMAIL = "vmastr@icloud.com"

# Define the __all__ variable to control what symbols are exported when importing the package
__all__ = ["Polytope", "compute_volume", "compute_polar_polytope", "compute_l_polars",
           "compute_mahler_volumes", "compute_isotropic_constant", "compute_b_constant",
           "find_extreme_points", "run_mahler_algorithm", "generate_random_polytopes",
           "graph_polytopes", "graph_mahler_volume", "graph_isotropic_constant",
           "graph_b_constant", "VERSION", "AUTHOR", "EMAIL"]
