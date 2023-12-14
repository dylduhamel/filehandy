from filehandy import read_lines
import pytest
import tempfile
import os

def test_read_lines_text():
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".txt") as tmpfile:
        tmpfile.write(" Line 1 \n Line 2 \n Line 3 ")
        tmpfile.seek(0) # Set file ptr to start
        lines = read_lines(tmpfile.name)
        assert lines == [" Line 1 \n", " Line 2 \n", " Line 3 "]

def test_read_lines_text_strip():
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".txt") as tmpfile:
        tmpfile.write(" Line 1 \n Line 2 \n Line 3 ")
        tmpfile.seek(0) # Set file ptr to start
        lines = read_lines(tmpfile.name, strip=True)
        assert lines == ["Line 1", "Line 2", "Line 3"]

def test_read_lines_csv():
    with tempfile.NamedTemporaryFile(mode='w+', suffix=".csv") as tmpfile:
        tmpfile.write("Name,DOB\nDylan Duhamel,10/20/00\nJack Duhamel,12/29/03\n")
        tmpfile.seek(0)
        lines = read_lines(tmpfile.name)
        assert lines == ['Name,DOB', 'Dylan Duhamel,10/20/00', 'Jack Duhamel,12/29/03']

def test_read_lines_csv_strip():
    with tempfile.NamedTemporaryFile(mode='w+', suffix=".csv") as tmpfile:
        tmpfile.write("Name,DOB\nDylan Duhamel,10/20/00\nJack Duhamel,12/29/03\n")
        tmpfile.seek(0)
        lines = read_lines(tmpfile.name, strip=True)
        assert lines == ['Name,DOB', 'Dylan Duhamel,10/20/00', 'Jack Duhamel,12/29/03']

def test_read_lines_wrong_file():
    with tempfile.NamedTemporaryFile(suffix='.jpg') as tmpfile:
        with pytest.raises(ValueError) as context:
            _ = read_lines(tmpfile.name)
    
    assert "Unsupported file type:" in str(context.value)

def test_read_lines_empty_file():
    pass

def test_read_lines_proper_closure():
    pass