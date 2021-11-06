"""Create a conftest.py

Define the fixture functions in this file to make them accessible across multiple test files.
"""


from pathlib import Path
import pytest
from beetools.beearchiver import Archiver
from beetools.beeutils import rm_tree


_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = "0.0.1"


b_tls = Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)


@pytest.fixture
def setup_env(tmp_path):
    """Setup the environment base structure"""
    working_dir = tmp_path
    yield working_dir
    rm_tree(working_dir)


del b_tls
