"""Testing releaseit__init__()"""

from pathlib import Path
from beetools.beearchiver import Archiver
import releaseit


_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = "0.0.2"

_TOML_CONTENTS_DEF_STRUCT = {
    "release": {
        "0": {
            "0": {
                "1": {
                    "Detail": {"Description": "Creation of the project"},
                    "Changes": {
                        "File001": ["filename01.py", "Insert change description here."],
                        "File002": [
                            "filename02.txt",
                            "Insert change description here.",
                        ],
                    },
                }
            }
        }
    }
}
_TOML_CONTENTS_EXIST_CONTENTS = """[release]
[release.0]
[release.0.0.1.Detail]
Description = 'Creation of the project'
[release.0.0.1.Changes]
File001 = ['filename01.py',"Insert change description here."]
File002 = ['filename02.txt',"Insert change description here."]
[release.0.0.2.Detail]
Description = 'This is a new release.'
[release.0.0.2.Changes]
File001 = ['README.rst', "Update with latest changes."]
File002 = ['releaseit.py', "Update with latest changes."]
"""
_TOML_CONTENTS_EXIST_STRUCT = {
    "release": {
        "0": {
            "0": {
                "1": {
                    "Changes": {
                        "File001": [
                            "filename01.py",
                            "Insert change " "description here.",
                        ],
                        "File002": [
                            "filename02.txt",
                            "Insert change description here.",
                        ],
                    },
                    "Detail": {"Description": "Creation of the project"},
                },
                "2": {
                    "Changes": {
                        "File001": ["README.rst", "Update with latest changes."],
                        "File002": ["releaseit.py", "Update with latest changes."],
                    },
                    "Detail": {"Description": "This is a new release."},
                },
            }
        }
    }
}
b_tls = Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)


class TestReleaseIt:
    def test__init__default(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        relit = releaseit.ReleaseIt(working_dir)
        assert relit.release_cfg == _TOML_CONTENTS_DEF_STRUCT
        assert relit.release_pth.exists()
        assert relit.success
        pass

    def test__init__existing(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXIST_CONTENTS)

        relit = releaseit.ReleaseIt(working_dir)

        assert relit.release_cfg == _TOML_CONTENTS_EXIST_STRUCT
        assert relit.release_pth.exists()
        assert relit.success
        pass

    def test_create_release_config(self, setup_env):
        working_dir = setup_env
        relit = releaseit.ReleaseIt(working_dir)
        relit._create_release_config()
        assert relit.release_cfg == _TOML_CONTENTS_DEF_STRUCT
        assert relit.release_pth.exists()
        assert relit.success
        pass


del b_tls
