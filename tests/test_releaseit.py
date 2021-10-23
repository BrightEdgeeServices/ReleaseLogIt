"""Testing releaseit__init__()"""

from pathlib import Path
from beetools.beearchiver import Archiver
import releaseit


_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = "0.0.1"


b_tls = Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)


class TestReleaseIt:
    def test__init__default(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        relit = releaseit.ReleaseIt(working_dir)
        assert relit.release_cfg == {
            "release": {"0": {"0": {"1": ["Creation of the project"]}}}
        }
        assert relit.release_pth.exists()
        assert relit.success
        pass

    def test_create_release_config(self, setup_env):
        working_dir = setup_env
        relit = releaseit.ReleaseIt(working_dir)
        relit._create_release_config()
        assert relit.release_cfg == {
            "release": {"0": {"0": {"1": ["Creation of the project"]}}}
        }
        assert relit.release_pth.exists()
        assert relit.success
        pass


del b_tls
