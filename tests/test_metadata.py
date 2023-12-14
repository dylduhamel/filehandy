from filehandy import fetch_metadata
import os
import tempfile

def test_fetch_metadata_existing_file():
    # Temp file
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        filepath = tmpfile.name

    # Testing function
    metadata = fetch_metadata(filepath)

    assert 'size' in metadata
    assert 'last_accessed' in metadata
    assert 'last_modified' in metadata
    assert 'creation_time' in metadata
    assert 'mode' in metadata
    assert 'inode' in metadata
    assert 'device' in metadata
    assert 'n_links' in metadata
    assert 'uid' in metadata
    assert 'gid' in metadata

    os.remove(filepath)