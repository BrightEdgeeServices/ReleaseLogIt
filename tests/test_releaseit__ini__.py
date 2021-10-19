"""Testing releaseit__init__()"""

from pathlib import Path
from beetools.beearchiver import Archiver
from beetools.beeutils import rm_tree
from conftest import setup_env
import releaseit


_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = "0.0.1"


b_tls = Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)


def test_releaseit__init__():
    """Assert class __init__"""
    working_dir = setup_env()

    t_releaseit = releaseit.ReleaseIt(_PROJ_NAME)

    assert t_releaseit.success

    rm_tree(working_dir)


del b_tls
