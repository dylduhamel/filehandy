import os
import zipfile
import gzip 
import bz2
import lzma

def compress_data(filepath: str, algo: str = 'gzip') -> str:
    """Returns path to new compressed file in the same directory as *filepath*.
    Compresses data with gzip, bzip2, or lzma algorithm. 
    Select compression algo with *algo*, default is ``gzip``.
    
    Args:
        filepath (str): Path for file to be compressed.
        algo (str): Compression algo to use. Select from
                    gzip, bzip2, or lzma. Default is gzip.
                    
    Returns:
        str: Path to the compressed file.
    """
    
    # Check if the file exists
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File {filepath} not found")

    # Define output filename based on the selected algorithm
    if algo == 'gzip':
        out_filename = os.path.splitext(filepath)[0] + '.gz'
        open_func = gzip.open
    elif algo == 'bzip2':
        out_filename = os.path.splitext(filepath)[0] + '.bz2'
        open_func = bz2.open
    elif algo == 'lzma':
        out_filename = os.path.splitext(filepath)[0] + '.xz'
        open_func = lzma.open
    else:
        raise ValueError(f"Unsupported compression algorithm: {algo}")

    # Read file contents and write compressed data
    with open(filepath, 'rb') as file_in, open_func(out_filename, 'wb') as file_out:
        file_out.write(file_in.read())

    return out_filename
        
def compress_zip(filepath: str, compression_method: str=zipfile.ZIP_DEFLATED):
    pass