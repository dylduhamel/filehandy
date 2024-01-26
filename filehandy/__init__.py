from .file import read_lines
from .metadata import fetch_metadata
from .compression import compress_data

__version__ = '0.0.1a1'

# Exporing of functions 
__all__ = ['read_lines', 'fetch_metadata', 'compress_data']
