"""Testing releaseit__init__()"""

from pathlib import Path
import pytest
from beetools.beearchiver import Archiver
import releaseit


_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = "0.0.3"

_TOML_CONTENTS_DEF_STRUCT = {
    "0": {
        "0": {
            "0": {
                "Description": [
                    "List all the changes to the project here.",
                    "Changes listed here will be in the release notes under the above heading.",
                ],
                "FileChanges": [
                    ["filename01.py", "Insert change description here."],
                    ["filename02.txt", "Insert change description here."],
                ],
                "Header": "Creation of the project",
                "Version": "0.0.0",
            },
        }
    }
}
_TOML_CONTENTS_EXIST_CONTENTS = """\
[0.0.0]
Header = 'Creation of the project'
Description = ['List all the changes to the project here.',
'Changes listed here will be in the release notes under the above heading.']
Version =  '0.0.0'
FileChanges = [['filename01.py',"Insert change description here."],
['filename02.txt',"Insert change description here."]]
[0.0.1]
Header = 'This is a new release .'
Description = ['Changes for 0.0.1 are listed here.',
'Add as many description lines as you like.']
Version =  '0.0.1'
FileChanges = [['README.rst', "Update with latest changes."],
['releaseit.py', "Update with latest changes."]]
"""
_TOML_CONTENTS_EXIST_STRUCT = {
    "0": {
        "0": {
            "0": {
                "FileChanges": [
                    ["filename01.py", "Insert change description here."],
                    ["filename02.txt", "Insert change description here."],
                ],
                "Description": [
                    "List all the changes to the project here.",
                    "Changes listed here will be in the release notes under the above heading.",
                ],
                "Header": "Creation of the project",
                "Version": "0.0.0",
            },
            "1": {
                "FileChanges": [
                    ["README.rst", "Update with latest changes."],
                    ["releaseit.py", "Update with latest changes."],
                ],
                "Description": [
                    "Changes for 0.0.1 are listed here.",
                    "Add as many description lines as you like.",
                ],
                "Header": "This is a new release .",
                "Version": "0.0.1",
            },
        }
    }
}
_TOML_CONTENTS_EXTENDED_CONTENTS = """[0.0.0]
Header = 'Release 0.0.0.'
Description = ['Description line 1 of release 0.0.0',
               'Description line 2 of release 0.0.0']
Version =  '0.0.0'
FileChanges = [['File001.py', 'File001 0.0.0'],
               ['File002.txt', 'File002 0.0.0']]

[0.0.1]
Header = 'Release 0.0.1.'
Description = ['Description line 1 of release 0.0.1',
               'Description line 2 of release 0.0.1']
Version =  '0.0.1'
FileChanges = [['File001.py', 'File001 0.0.1'],
               ['File002.txt', 'File002 0.0.1']]

[0.0.2]
Header = 'Release 0.0.2.'
Description = ['Description line 1 of release 0.0.2',
               'Description line 2 of release 0.0.2']
Version =  '0.0.2'
FileChanges = [['File001.py', 'File001 0.0.2'],
               ['File002.txt', 'File002 0.0.2']]

[0.1.0]
Header = 'Release 0.1.0.'
Description = ['Description line 1 of release 0.1.0',
               'Description line 2 of release 0.1.0']
Version =  '0.1.0'
FileChanges = [['File001.py', 'File001 0.1.0'],
               ['File002.txt', 'File002 0.1.0']]

[0.1.1]
Header = 'Release 0.1.1.'
Description = ['Description line 1 of release 0.1.1',
               'Description line 2 of release 0.1.1']
Version =  '0.1.1'
FileChanges = [['File001.py', 'File001 0.1.1'],
               ['File002.txt', 'File002 0.1.1']]

[0.1.2]
Header = 'Release 0.1.2.'
Description = ['Description line 1 of release 0.1.2',
               'Description line 2 of release 0.1.2']
Version =  '0.1.2'
FileChanges = [['File001.py', 'File001 0.1.2'],
               ['File002.txt', 'File002 0.1.2']]

[0.2.0]
Header = 'Release 0.2.0.'
Description = ['Description line 1 of release 0.2.0',
               'Description line 2 of release 0.2.0']
Version =  '0.2.0'
FileChanges = [['File001.py', 'File001 0.2.0'],
               ['File002.txt', 'File002 0.2.0']]

[0.2.1]
Header = 'Release 0.2.1.'
Description = ['Description line 1 of release 0.2.1',
               'Description line 2 of release 0.2.1']
Version =  '0.2.1'
FileChanges = [['File001.py', 'File001 0.2.1'],
               ['File002.txt', 'File002 0.2.1']]

[0.2.2]
Header = 'Release 0.2.2.'
Description = ['Description line 1 of release 0.2.2',
               'Description line 2 of release 0.2.2']
Version =  '0.2.2'
FileChanges = [['File001.py', 'File001 0.2.2'],
               ['File002.txt', 'File002 0.2.2']]

[1.0.0]
Header = 'Release 1.0.0.'
Description = ['Description line 1 of release 1.0.0',
               'Description line 2 of release 1.0.0']
Version =  '1.0.0'
FileChanges = [['File001.py', 'File001 1.0.0'],
               ['File002.txt', 'File002 1.0.0']]

[1.0.1]
Header = 'Release 1.0.1.'
Description = ['Description line 1 of release 1.0.1',
               'Description line 2 of release 1.0.1']
Version =  '1.0.1'
FileChanges = [['File001.py', 'File001 1.0.1'],
               ['File002.txt', 'File002 1.0.1']]

[1.0.2]
Header = 'Release 1.0.2.'
Description = ['Description line 1 of release 1.0.2',
               'Description line 2 of release 1.0.2']
Version =  '1.0.2'
FileChanges = [['File001.py', 'File001 1.0.2'],
               ['File002.txt', 'File002 1.0.2']]

[1.1.0]
Header = 'Release 1.1.0.'
Description = ['Description line 1 of release 1.1.0',
               'Description line 2 of release 1.1.0']
Version =  '1.1.0'
FileChanges = [['File001.py', 'File001 1.1.0'],
               ['File002.txt', 'File002 1.1.0']]

[1.1.1]
Header = 'Release 1.1.1.'
Description = ['Description line 1 of release 1.1.1',
               'Description line 2 of release 1.1.1']
Version =  '1.1.1'
FileChanges = [['File001.py', 'File001 1.1.1'],
               ['File002.txt', 'File002 1.1.1']]

[1.1.2]
Header = 'Release 1.1.2.'
Description = ['Description line 1 of release 1.1.2',
               'Description line 2 of release 1.1.2']
Version =  '1.1.2'
FileChanges = [['File001.py', 'File001 1.1.2'],
               ['File002.txt', 'File002 1.1.2']]

[1.2.0]
Header = 'Release 1.2.0.'
Description = ['Description line 1 of release 1.2.0',
               'Description line 2 of release 1.2.0']
Version =  '1.2.0'
FileChanges = [['File001.py', 'File001 1.2.0'],
               ['File002.txt', 'File002 1.2.0']]

[1.2.1]
Header = 'Release 1.2.1.'
Description = ['Description line 1 of release 1.2.1',
               'Description line 2 of release 1.2.1']
Version =  '1.2.1'
FileChanges = [['File001.py', 'File001 1.2.1'],
               ['File002.txt', 'File002 1.2.1']]

[1.2.2]
Header = 'Release 1.2.2.'
Description = ['Description line 1 of release 1.2.2',
               'Description line 2 of release 1.2.2']
Version =  '1.2.2'
FileChanges = [['File001.py', 'File001 1.2.2'],
               ['File002.txt', 'File002 1.2.2']]

[2.0.0]
Header = 'Release 2.0.0.'
Description = ['Description line 1 of release 2.0.0',
               'Description line 2 of release 2.0.0']
Version =  '2.0.0'
FileChanges = [['File001.py', 'File001 2.0.0'],
               ['File002.txt', 'File002 2.0.0']]

[2.0.1]
Header = 'Release 2.0.1.'
Description = ['Description line 1 of release 2.0.1',
               'Description line 2 of release 2.0.1']
Version =  '2.0.1'
FileChanges = [['File001.py', 'File001 2.0.1'],
               ['File002.txt', 'File002 2.0.1']]

[2.0.2]
Header = 'Release 2.0.2.'
Description = ['Description line 1 of release 2.0.2',
               'Description line 2 of release 2.0.2']
Version =  '2.0.2'
FileChanges = [['File001.py', 'File001 2.0.2'],
               ['File002.txt', 'File002 2.0.2']]

[2.1.0]
Header = 'Release 2.1.0.'
Description = ['Description line 1 of release 2.1.0',
               'Description line 2 of release 2.1.0']
Version =  '2.1.0'
FileChanges = [['File001.py', 'File001 2.1.0'],
               ['File002.txt', 'File002 2.1.0']]

[2.1.1]
Header = 'Release 2.1.1.'
Description = ['Description line 1 of release 2.1.1',
               'Description line 2 of release 2.1.1']
Version =  '2.1.1'
FileChanges = [['File001.py', 'File001 2.1.1'],
               ['File002.txt', 'File002 2.1.1']]

[2.1.2]
Header = 'Release 2.1.2.'
Description = ['Description line 1 of release 2.1.2',
               'Description line 2 of release 2.1.2']
Version =  '2.1.2'
FileChanges = [['File001.py', 'File001 2.1.2'],
               ['File002.txt', 'File002 2.1.2']]

[2.2.2]
Header = 'Release 2.2.2.'
Description = ['Description line 1 of release 2.2.2',
               'Description line 2 of release 2.2.2']
Version =  '2.2.2'
FileChanges = [['File001.py', 'File001 2.2.2'],
               ['File002.txt', 'File002 2.2.2']]

[2.2.1]
Header = 'Release 2.2.1.'
Description = ['Description line 1 of release 2.2.1',
               'Description line 2 of release 2.2.1']
Version =  '2.2.1'
FileChanges = [['File001.py', 'File001 2.2.1'],
               ['File002.txt', 'File002 2.2.1']]

[2.2.0]
Header = 'Release 2.2.0.'
Description = ['Description line 1 of release 2.2.0',
               'Description line 2 of release 2.2.0']
Version =  '2.2.0'
FileChanges = [['File001.py', 'File001 2.2.0'],
               ['File002.txt', 'File002 2.2.0']]
"""
_TOML_CONTENTS_EXTENDED_STRUCT = {
    "0": {
        "0": {
            "0": {
                "FileChanges": [
                    ["File001.py", "File001 0.0.0"],
                    ["File002.txt", "File002 0.0.0"],
                ],
                "Description": [
                    "Description line 1 of release 0.0.0",
                    "Description line 2 of release 0.0.0",
                ],
                "Header": "Release 0.0.0.",
                "Version": "0.0.0",
            },
            "1": {
                "FileChanges": [
                    ["File001.py", "File001 0.0.1"],
                    ["File002.txt", "File002 0.0.1"],
                ],
                "Description": [
                    "Description line 1 of release 0.0.1",
                    "Description line 2 of release 0.0.1",
                ],
                "Header": "Release 0.0.1.",
                "Version": "0.0.1",
            },
            "2": {
                "FileChanges": [
                    ["File001.py", "File001 0.0.2"],
                    ["File002.txt", "File002 0.0.2"],
                ],
                "Description": [
                    "Description line 1 of release 0.0.2",
                    "Description line 2 of release 0.0.2",
                ],
                "Header": "Release 0.0.2.",
                "Version": "0.0.2",
            },
        },
        "1": {
            "0": {
                "FileChanges": [
                    ["File001.py", "File001 0.1.0"],
                    ["File002.txt", "File002 0.1.0"],
                ],
                "Description": [
                    "Description line 1 of release 0.1.0",
                    "Description line 2 of release 0.1.0",
                ],
                "Header": "Release 0.1.0.",
                "Version": "0.1.0",
            },
            "1": {
                "FileChanges": [
                    ["File001.py", "File001 0.1.1"],
                    ["File002.txt", "File002 0.1.1"],
                ],
                "Description": [
                    "Description line 1 of release 0.1.1",
                    "Description line 2 of release 0.1.1",
                ],
                "Header": "Release 0.1.1.",
                "Version": "0.1.1",
            },
            "2": {
                "FileChanges": [
                    ["File001.py", "File001 0.1.2"],
                    ["File002.txt", "File002 0.1.2"],
                ],
                "Description": [
                    "Description line 1 of release 0.1.2",
                    "Description line 2 of release 0.1.2",
                ],
                "Header": "Release 0.1.2.",
                "Version": "0.1.2",
            },
        },
        "2": {
            "0": {
                "FileChanges": [
                    ["File001.py", "File001 0.2.0"],
                    ["File002.txt", "File002 0.2.0"],
                ],
                "Description": [
                    "Description line 1 of release 0.2.0",
                    "Description line 2 of release 0.2.0",
                ],
                "Header": "Release 0.2.0.",
                "Version": "0.2.0",
            },
            "1": {
                "FileChanges": [
                    ["File001.py", "File001 0.2.1"],
                    ["File002.txt", "File002 0.2.1"],
                ],
                "Description": [
                    "Description line 1 of release 0.2.1",
                    "Description line 2 of release 0.2.1",
                ],
                "Header": "Release 0.2.1.",
                "Version": "0.2.1",
            },
            "2": {
                "FileChanges": [
                    ["File001.py", "File001 0.2.2"],
                    ["File002.txt", "File002 0.2.2"],
                ],
                "Description": [
                    "Description line 1 of release 0.2.2",
                    "Description line 2 of release 0.2.2",
                ],
                "Header": "Release 0.2.2.",
                "Version": "0.2.2",
            },
        },
    },
    "1": {
        "0": {
            "0": {
                "FileChanges": [
                    ["File001.py", "File001 1.0.0"],
                    ["File002.txt", "File002 1.0.0"],
                ],
                "Description": [
                    "Description line 1 of release 1.0.0",
                    "Description line 2 of release 1.0.0",
                ],
                "Header": "Release 1.0.0.",
                "Version": "1.0.0",
            },
            "1": {
                "FileChanges": [
                    ["File001.py", "File001 1.0.1"],
                    ["File002.txt", "File002 1.0.1"],
                ],
                "Description": [
                    "Description line 1 of release 1.0.1",
                    "Description line 2 of release 1.0.1",
                ],
                "Header": "Release 1.0.1.",
                "Version": "1.0.1",
            },
            "2": {
                "FileChanges": [
                    ["File001.py", "File001 1.0.2"],
                    ["File002.txt", "File002 1.0.2"],
                ],
                "Description": [
                    "Description line 1 of release 1.0.2",
                    "Description line 2 of release 1.0.2",
                ],
                "Header": "Release 1.0.2.",
                "Version": "1.0.2",
            },
        },
        "1": {
            "0": {
                "FileChanges": [
                    ["File001.py", "File001 1.1.0"],
                    ["File002.txt", "File002 1.1.0"],
                ],
                "Description": [
                    "Description line 1 of release 1.1.0",
                    "Description line 2 of release 1.1.0",
                ],
                "Header": "Release 1.1.0.",
                "Version": "1.1.0",
            },
            "1": {
                "FileChanges": [
                    ["File001.py", "File001 1.1.1"],
                    ["File002.txt", "File002 1.1.1"],
                ],
                "Description": [
                    "Description line 1 of release 1.1.1",
                    "Description line 2 of release 1.1.1",
                ],
                "Header": "Release 1.1.1.",
                "Version": "1.1.1",
            },
            "2": {
                "FileChanges": [
                    ["File001.py", "File001 1.1.2"],
                    ["File002.txt", "File002 1.1.2"],
                ],
                "Description": [
                    "Description line 1 of release 1.1.2",
                    "Description line 2 of release 1.1.2",
                ],
                "Header": "Release 1.1.2.",
                "Version": "1.1.2",
            },
        },
        "2": {
            "0": {
                "FileChanges": [
                    ["File001.py", "File001 1.2.0"],
                    ["File002.txt", "File002 1.2.0"],
                ],
                "Description": [
                    "Description line 1 of release 1.2.0",
                    "Description line 2 of release 1.2.0",
                ],
                "Header": "Release 1.2.0.",
                "Version": "1.2.0",
            },
            "1": {
                "FileChanges": [
                    ["File001.py", "File001 1.2.1"],
                    ["File002.txt", "File002 1.2.1"],
                ],
                "Description": [
                    "Description line 1 of release 1.2.1",
                    "Description line 2 of release 1.2.1",
                ],
                "Header": "Release 1.2.1.",
                "Version": "1.2.1",
            },
            "2": {
                "FileChanges": [
                    ["File001.py", "File001 1.2.2"],
                    ["File002.txt", "File002 1.2.2"],
                ],
                "Description": [
                    "Description line 1 of release 1.2.2",
                    "Description line 2 of release 1.2.2",
                ],
                "Header": "Release 1.2.2.",
                "Version": "1.2.2",
            },
        },
    },
    "2": {
        "0": {
            "0": {
                "FileChanges": [
                    ["File001.py", "File001 2.0.0"],
                    ["File002.txt", "File002 2.0.0"],
                ],
                "Description": [
                    "Description line 1 of release 2.0.0",
                    "Description line 2 of release 2.0.0",
                ],
                "Header": "Release 2.0.0.",
                "Version": "2.0.0",
            },
            "1": {
                "FileChanges": [
                    ["File001.py", "File001 2.0.1"],
                    ["File002.txt", "File002 2.0.1"],
                ],
                "Description": [
                    "Description line 1 of release 2.0.1",
                    "Description line 2 of release 2.0.1",
                ],
                "Header": "Release 2.0.1.",
                "Version": "2.0.1",
            },
            "2": {
                "FileChanges": [
                    ["File001.py", "File001 2.0.2"],
                    ["File002.txt", "File002 2.0.2"],
                ],
                "Description": [
                    "Description line 1 of release 2.0.2",
                    "Description line 2 of release 2.0.2",
                ],
                "Header": "Release 2.0.2.",
                "Version": "2.0.2",
            },
        },
        "1": {
            "0": {
                "FileChanges": [
                    ["File001.py", "File001 2.1.0"],
                    ["File002.txt", "File002 2.1.0"],
                ],
                "Description": [
                    "Description line 1 of release 2.1.0",
                    "Description line 2 of release 2.1.0",
                ],
                "Header": "Release 2.1.0.",
                "Version": "2.1.0",
            },
            "1": {
                "FileChanges": [
                    ["File001.py", "File001 2.1.1"],
                    ["File002.txt", "File002 2.1.1"],
                ],
                "Description": [
                    "Description line 1 of release 2.1.1",
                    "Description line 2 of release 2.1.1",
                ],
                "Header": "Release 2.1.1.",
                "Version": "2.1.1",
            },
            "2": {
                "FileChanges": [
                    ["File001.py", "File001 2.1.2"],
                    ["File002.txt", "File002 2.1.2"],
                ],
                "Description": [
                    "Description line 1 of release 2.1.2",
                    "Description line 2 of release 2.1.2",
                ],
                "Header": "Release 2.1.2.",
                "Version": "2.1.2",
            },
        },
        "2": {
            "0": {
                "FileChanges": [
                    ["File001.py", "File001 2.2.0"],
                    ["File002.txt", "File002 2.2.0"],
                ],
                "Description": [
                    "Description line 1 of release 2.2.0",
                    "Description line 2 of release 2.2.0",
                ],
                "Header": "Release 2.2.0.",
                "Version": "2.2.0",
            },
            "1": {
                "FileChanges": [
                    ["File001.py", "File001 2.2.1"],
                    ["File002.txt", "File002 2.2.1"],
                ],
                "Description": [
                    "Description line 1 of release 2.2.1",
                    "Description line 2 of release 2.2.1",
                ],
                "Header": "Release 2.2.1.",
                "Version": "2.2.1",
            },
            "2": {
                "FileChanges": [
                    ["File001.py", "File001 2.2.2"],
                    ["File002.txt", "File002 2.2.2"],
                ],
                "Description": [
                    "Description line 1 of release 2.2.2",
                    "Description line 2 of release 2.2.2",
                ],
                "Header": "Release 2.2.2.",
                "Version": "2.2.2",
            },
        },
    },
}
b_tls = Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)


class TestReleaseIt:
    def test__init__default(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        t_releaseit = releaseit.ReleaseIt(working_dir, p_parent_log_name=_PROJ_NAME)
        assert t_releaseit.release_notes == _TOML_CONTENTS_DEF_STRUCT
        assert t_releaseit.seq == [["0", "0", "0"]]
        assert t_releaseit.src_pth.exists()
        assert t_releaseit.success
        pass

    def test__init__existing(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXIST_CONTENTS)

        t_releaseit = releaseit.ReleaseIt(working_dir)

        assert t_releaseit.release_notes == _TOML_CONTENTS_EXIST_STRUCT
        assert t_releaseit.seq == [["0", "0", "0"], ["0", "0", "1"]]
        assert t_releaseit.src_pth.exists()
        assert t_releaseit.success
        pass

    def test__init__extended(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaseit = releaseit.ReleaseIt(working_dir)

        assert t_releaseit.release_notes == _TOML_CONTENTS_EXTENDED_STRUCT
        assert t_releaseit.seq == [
            ["0", "0", "0"],
            ["0", "0", "1"],
            ["0", "0", "2"],
            ["0", "1", "0"],
            ["0", "1", "1"],
            ["0", "1", "2"],
            ["0", "2", "0"],
            ["0", "2", "1"],
            ["0", "2", "2"],
            ["1", "0", "0"],
            ["1", "0", "1"],
            ["1", "0", "2"],
            ["1", "1", "0"],
            ["1", "1", "1"],
            ["1", "1", "2"],
            ["1", "2", "0"],
            ["1", "2", "1"],
            ["1", "2", "2"],
            ["2", "0", "0"],
            ["2", "0", "1"],
            ["2", "0", "2"],
            ["2", "1", "0"],
            ["2", "1", "1"],
            ["2", "1", "2"],
            ["2", "2", "0"],
            ["2", "2", "1"],
            ["2", "2", "2"],
        ]
        assert t_releaseit.src_pth.exists()
        assert t_releaseit.success
        pass

    def test__iter__(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXIST_CONTENTS)

        t_releaseit = releaseit.ReleaseIt(working_dir)

        assert isinstance(t_releaseit, releaseit.ReleaseIt)
        assert t_releaseit.curr_pos == 0
        pass

    def test__next__(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXIST_CONTENTS)

        t_releaseit = releaseit.ReleaseIt(working_dir)
        elements = iter(t_releaseit)

        assert next(elements) == {
            "Description": [
                "List all the changes to the project here.",
                "Changes listed here will be in the release notes under the above heading.",
            ],
            "FileChanges": [
                ["filename01.py", "Insert change description here."],
                ["filename02.txt", "Insert change description here."],
            ],
            "Header": "Creation of the project",
            "Version": "0.0.0",
        }
        assert next(elements) == {
            "Description": [
                "Changes for 0.0.1 are listed here.",
                "Add as many description lines as you like.",
            ],
            "FileChanges": [
                ["README.rst", "Update with latest changes."],
                ["releaseit.py", "Update with latest changes."],
            ],
            "Header": "This is a new release .",
            "Version": "0.0.1",
        }
        with pytest.raises(StopIteration):
            assert next(elements)

    def test_has_header(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaseit = releaseit.ReleaseIt(working_dir)

        assert t_releaseit.has_header("Release 1.1.1.")
        pass

    def test_do_example(self):
        assert releaseit.do_examples()
        pass


del b_tls
