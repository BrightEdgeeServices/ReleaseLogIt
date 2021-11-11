"""Testing releaseit__init__()"""

import copy
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
                "Title": "Creation of the project",
                "Version": "0.0.0",
            },
        }
    }
}
_TOML_CONTENTS_EXIST_CONTENTS = """\
[0.0.0]
Title = 'Creation of the project'
Description = ['List all the changes to the project here.',
'Changes listed here will be in the release notes under the above heading.']
Version =  '0.0.0'
FileChanges = [['filename01.py',"Insert change description here."],
['filename02.txt',"Insert change description here."]]
[0.0.1]
Title = 'This is a new release.'
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
                "Title": "Creation of the project",
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
                "Title": "This is a new release.",
                "Version": "0.0.1",
            },
        }
    }
}
_TOML_CONTENTS_EXTENDED_CONTENTS = """[0.0.0]
Title = 'Release 0.0.0.'
Description = ['Description line 1 of release 0.0.0',
               'Description line 2 of release 0.0.0']
Version =  '0.0.0'
FileChanges = [['File001.py', 'File001 0.0.0'],
               ['File002.txt', 'File002 0.0.0']]

[0.0.1]
Title = 'Release 0.0.1.'
Description = ['Description line 1 of release 0.0.1',
               'Description line 2 of release 0.0.1']
Version =  '0.0.1'
FileChanges = [['File001.py', 'File001 0.0.1'],
               ['File002.txt', 'File002 0.0.1']]

[0.0.2]
Title = 'Release 0.0.2.'
Description = ['Description line 1 of release 0.0.2',
               'Description line 2 of release 0.0.2']
Version =  '0.0.2'
FileChanges = [['File001.py', 'File001 0.0.2'],
               ['File002.txt', 'File002 0.0.2']]

[0.1.0]
Title = 'Release 0.1.0.'
Description = ['Description line 1 of release 0.1.0',
               'Description line 2 of release 0.1.0']
Version =  '0.1.0'
FileChanges = [['File001.py', 'File001 0.1.0'],
               ['File002.txt', 'File002 0.1.0']]

[0.1.1]
Title = 'Release 0.1.1.'
Description = ['Description line 1 of release 0.1.1',
               'Description line 2 of release 0.1.1']
Version =  '0.1.1'
FileChanges = [['File001.py', 'File001 0.1.1'],
               ['File002.txt', 'File002 0.1.1']]

[0.1.2]
Title = 'Release 0.1.2.'
Description = ['Description line 1 of release 0.1.2',
               'Description line 2 of release 0.1.2']
Version =  '0.1.2'
FileChanges = [['File001.py', 'File001 0.1.2'],
               ['File002.txt', 'File002 0.1.2']]

[0.2.0]
Title = 'Release 0.2.0.'
Description = ['Description line 1 of release 0.2.0',
               'Description line 2 of release 0.2.0']
Version =  '0.2.0'
FileChanges = [['File001.py', 'File001 0.2.0'],
               ['File002.txt', 'File002 0.2.0']]

[0.2.1]
Title = 'Release 0.2.1.'
Description = ['Description line 1 of release 0.2.1',
               'Description line 2 of release 0.2.1']
Version =  '0.2.1'
FileChanges = [['File001.py', 'File001 0.2.1'],
               ['File002.txt', 'File002 0.2.1']]

[0.2.2]
Title = 'Release 0.2.2.'
Description = ['Description line 1 of release 0.2.2',
               'Description line 2 of release 0.2.2']
Version =  '0.2.2'
FileChanges = [['File001.py', 'File001 0.2.2'],
               ['File002.txt', 'File002 0.2.2']]

[1.0.0]
Title = 'Release 1.0.0.'
Description = ['Description line 1 of release 1.0.0',
               'Description line 2 of release 1.0.0']
Version =  '1.0.0'
FileChanges = [['File001.py', 'File001 1.0.0'],
               ['File002.txt', 'File002 1.0.0']]

[1.0.1]
Title = 'Release 1.0.1.'
Description = ['Description line 1 of release 1.0.1',
               'Description line 2 of release 1.0.1']
Version =  '1.0.1'
FileChanges = [['File001.py', 'File001 1.0.1'],
               ['File002.txt', 'File002 1.0.1']]

[1.0.2]
Title = 'Release 1.0.2.'
Description = ['Description line 1 of release 1.0.2',
               'Description line 2 of release 1.0.2']
Version =  '1.0.2'
FileChanges = [['File001.py', 'File001 1.0.2'],
               ['File002.txt', 'File002 1.0.2']]

[1.1.0]
Title = 'Release 1.1.0.'
Description = ['Description line 1 of release 1.1.0',
               'Description line 2 of release 1.1.0']
Version =  '1.1.0'
FileChanges = [['File001.py', 'File001 1.1.0'],
               ['File002.txt', 'File002 1.1.0']]

[1.1.1]
Title = 'Release 1.1.1.'
Description = ['Description line 1 of release 1.1.1',
               'Description line 2 of release 1.1.1']
Version =  '1.1.1'
FileChanges = [['File001.py', 'File001 1.1.1'],
               ['File002.txt', 'File002 1.1.1']]

[1.1.2]
Title = 'Release 1.1.2.'
Description = ['Description line 1 of release 1.1.2',
               'Description line 2 of release 1.1.2']
Version =  '1.1.2'
FileChanges = [['File001.py', 'File001 1.1.2'],
               ['File002.txt', 'File002 1.1.2']]

[1.2.0]
Title = 'Release 1.2.0.'
Description = ['Description line 1 of release 1.2.0',
               'Description line 2 of release 1.2.0']
Version =  '1.2.0'
FileChanges = [['File001.py', 'File001 1.2.0'],
               ['File002.txt', 'File002 1.2.0']]

[1.2.1]
Title = 'Release 1.2.1.'
Description = ['Description line 1 of release 1.2.1',
               'Description line 2 of release 1.2.1']
Version =  '1.2.1'
FileChanges = [['File001.py', 'File001 1.2.1'],
               ['File002.txt', 'File002 1.2.1']]

[1.2.2]
Title = 'Release 1.2.2.'
Description = ['Description line 1 of release 1.2.2',
               'Description line 2 of release 1.2.2']
Version =  '1.2.2'
FileChanges = [['File001.py', 'File001 1.2.2'],
               ['File002.txt', 'File002 1.2.2']]

[2.0.0]
Title = 'Release 2.0.0.'
Description = ['Description line 1 of release 2.0.0',
               'Description line 2 of release 2.0.0']
Version =  '2.0.0'
FileChanges = [['File001.py', 'File001 2.0.0'],
               ['File002.txt', 'File002 2.0.0']]

[2.0.1]
Title = 'Release 2.0.1.'
Description = ['Description line 1 of release 2.0.1',
               'Description line 2 of release 2.0.1']
Version =  '2.0.1'
FileChanges = [['File001.py', 'File001 2.0.1'],
               ['File002.txt', 'File002 2.0.1']]

[2.0.2]
Title = 'Release 2.0.2.'
Description = ['Description line 1 of release 2.0.2',
               'Description line 2 of release 2.0.2']
Version =  '2.0.2'
FileChanges = [['File001.py', 'File001 2.0.2'],
               ['File002.txt', 'File002 2.0.2']]

[2.1.0]
Title = 'Release 2.1.0.'
Description = ['Description line 1 of release 2.1.0',
               'Description line 2 of release 2.1.0']
Version =  '2.1.0'
FileChanges = [['File001.py', 'File001 2.1.0'],
               ['File002.txt', 'File002 2.1.0']]

[2.1.1]
Title = 'Release 2.1.1.'
Description = ['Description line 1 of release 2.1.1',
               'Description line 2 of release 2.1.1']
Version =  '2.1.1'
FileChanges = [['File001.py', 'File001 2.1.1'],
               ['File002.txt', 'File002 2.1.1']]

[2.1.2]
Title = 'Release 2.1.2.'
Description = ['Description line 1 of release 2.1.2',
               'Description line 2 of release 2.1.2']
Version =  '2.1.2'
FileChanges = [['File001.py', 'File001 2.1.2'],
               ['File002.txt', 'File002 2.1.2']]

[2.2.2]
Title = 'Release 2.2.2.'
Description = ['Description line 1 of release 2.2.2',
               'Description line 2 of release 2.2.2']
Version =  '2.2.2'
FileChanges = [['File001.py', 'File001 2.2.2'],
               ['File002.txt', 'File002 2.2.2']]

[2.2.1]
Title = 'Release 2.2.1.'
Description = ['Description line 1 of release 2.2.1',
               'Description line 2 of release 2.2.1']
Version =  '2.2.1'
FileChanges = [['File001.py', 'File001 2.2.1'],
               ['File002.txt', 'File002 2.2.1']]

[2.2.0]
Title = 'Release 2.2.0.'
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
                "Title": "Release 0.0.0.",
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
                "Title": "Release 0.0.1.",
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
                "Title": "Release 0.0.2.",
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
                "Title": "Release 0.1.0.",
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
                "Title": "Release 0.1.1.",
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
                "Title": "Release 0.1.2.",
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
                "Title": "Release 0.2.0.",
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
                "Title": "Release 0.2.1.",
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
                "Title": "Release 0.2.2.",
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
                "Title": "Release 1.0.0.",
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
                "Title": "Release 1.0.1.",
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
                "Title": "Release 1.0.2.",
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
                "Title": "Release 1.1.0.",
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
                "Title": "Release 1.1.1.",
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
                "Title": "Release 1.1.2.",
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
                "Title": "Release 1.2.0.",
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
                "Title": "Release 1.2.1.",
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
                "Title": "Release 1.2.2.",
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
                "Title": "Release 2.0.0.",
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
                "Title": "Release 2.0.1.",
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
                "Title": "Release 2.0.2.",
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
                "Title": "Release 2.1.0.",
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
                "Title": "Release 2.1.1.",
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
                "Title": "Release 2.1.2.",
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
                "Title": "Release 2.2.0.",
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
                "Title": "Release 2.2.1.",
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
                "Title": "Release 2.2.2.",
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
        assert t_releaseit.rel_notes == _TOML_CONTENTS_DEF_STRUCT
        assert t_releaseit.rel_list == [["0", "0", "0"]]
        assert t_releaseit.src_pth.exists()
        assert t_releaseit.success
        pass

    def test__init__existing(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXIST_CONTENTS)

        t_releaseit = releaseit.ReleaseIt(working_dir)

        assert t_releaseit.rel_notes == _TOML_CONTENTS_EXIST_STRUCT
        assert t_releaseit.rel_list == [["0", "0", "0"], ["0", "0", "1"]]
        assert t_releaseit.src_pth.exists()
        assert t_releaseit.success
        pass

    def test__init__extended(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaseit = releaseit.ReleaseIt(working_dir)

        assert t_releaseit.rel_notes == _TOML_CONTENTS_EXTENDED_STRUCT
        assert t_releaseit.rel_list == [
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
            "Title": "Creation of the project",
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
            "Title": "This is a new release.",
            "Version": "0.0.1",
        }
        with pytest.raises(StopIteration):
            assert next(elements)

    def test_add_release_note(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        release_note_100 = {
            "Description": [
                "Description line 1.",
                "Description line 2.",
            ],
            "FileChanges": [
                ["filename01.py", "Insert change description here."],
                ["filename02.txt", "Insert change description here."],
            ],
            "Title": "Release change 1.0.0",
            "Version": "1.0.0",
        }
        release_note_010 = {
            "Description": [
                "Description line 1.",
                "Description line 2.",
            ],
            "FileChanges": [
                ["filename01.py", "Insert change description here."],
                ["filename02.txt", "Insert change description here."],
            ],
            "Title": "Release change 0.1.0",
            "Version": "0.1.0",
        }
        release_note_001 = {
            "Description": [
                "Description line 1.",
                "Description line 2.",
            ],
            "FileChanges": [
                ["filename01.py", "Insert change description here."],
                ["filename02.txt", "Insert change description here."],
            ],
            "Title": "Release change 0.0.1",
            "Version": "0.0.1",
        }

        t_releaseit = releaseit.ReleaseIt(working_dir)
        t_releaseit.add_release_note(release_note_100)
        t_releaseit.add_release_note(release_note_010)
        t_releaseit.add_release_note(release_note_001)

        assert t_releaseit.rel_notes == {
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
                        "Title": "Creation of the project",
                        "Version": "0.0.0",
                    },
                    "1": {
                        "Description": [
                            "Description line 1.",
                            "Description line 2.",
                        ],
                        "FileChanges": [
                            ["filename01.py", "Insert change description here."],
                            ["filename02.txt", "Insert change description here."],
                        ],
                        "Title": "Release change 0.0.1",
                        "Version": "0.0.1",
                    },
                },
                "1": {
                    "0": {
                        "Description": [
                            "Description line 1.",
                            "Description line 2.",
                        ],
                        "FileChanges": [
                            ["filename01.py", "Insert change description here."],
                            ["filename02.txt", "Insert change description here."],
                        ],
                        "Title": "Release change 0.1.0",
                        "Version": "0.1.0",
                    },
                },
            },
            "1": {
                "0": {
                    "0": {
                        "Description": [
                            "Description line 1.",
                            "Description line 2.",
                        ],
                        "FileChanges": [
                            ["filename01.py", "Insert change description here."],
                            ["filename02.txt", "Insert change description here."],
                        ],
                        "Title": "Release change 1.0.0",
                        "Version": "1.0.0",
                    }
                }
            },
        }
        assert t_releaseit.rel_list == [
            ["0", "0", "0"],
            ["0", "0", "1"],
            ["0", "1", "0"],
            ["1", "0", "0"],
        ]
        assert t_releaseit.rel_cntr == 4
        pass

    def test_get_release_note_by_title(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaseit = releaseit.ReleaseIt(working_dir)

        assert t_releaseit.get_release_note_by_title("Release 1.1.1.") == {
            "Title": "Release 1.1.1.",
            "Description": [
                "Description line 1 of release 1.1.1",
                "Description line 2 of release 1.1.1",
            ],
            "Version": "1.1.1",
            "FileChanges": [
                ["File001.py", "File001 1.1.1"],
                ["File002.txt", "File002 1.1.1"],
            ],
        }
        assert t_releaseit.get_release_note_by_title("Release 9.9.9.") is None

    def test_get_release_note_by_version(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaseit = releaseit.ReleaseIt(working_dir)

        assert t_releaseit.get_release_note_by_version("1.1.1") == {
            "Title": "Release 1.1.1.",
            "Description": [
                "Description line 1 of release 1.1.1",
                "Description line 2 of release 1.1.1",
            ],
            "Version": "1.1.1",
            "FileChanges": [
                ["File001.py", "File001 1.1.1"],
                ["File002.txt", "File002 1.1.1"],
            ],
        }
        assert t_releaseit.get_release_note_by_title("9.9.9") is None

    def test_get_release_titles(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXIST_CONTENTS)

        t_releaseit = releaseit.ReleaseIt(working_dir)

        assert t_releaseit.get_release_titles() == [
            "Creation of the project",
            "This is a new release.",
        ]
        assert t_releaseit.success
        pass

    def test_has_title(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaseit = releaseit.ReleaseIt(working_dir)

        assert t_releaseit.has_title("Release 1.1.1.")
        assert not t_releaseit.has_title("Release 9.9.9.")
        pass

    def test_check_release_note(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        t_releaseit = releaseit.ReleaseIt(working_dir)
        release_note = {
            "Description": [
                "Description line 1.",
                "Description line 2.",
            ],
            "FileChanges": [
                ["filename01.py", "Insert change description here."],
                ["filename02.txt", "Insert change description here."],
            ],
            "Title": "Release change 9.9.9",
            "Version": "9.9.9",
        }

        assert t_releaseit._check_release_note(release_note)

        r_n = copy.deepcopy(release_note)
        del r_n["Description"]
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["Description"] = "abc"
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["Description"] = []
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["Description"] = ["abc", 123]
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        del r_n["FileChanges"]
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["FileChanges"] = "abc"
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["FileChanges"] = [[123, "def"], ["ghi", "jkl"]]
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["FileChanges"] = [["abc", "def"], ["ghi", 456]]
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        del r_n["Title"]
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["Title"] = "Creation of the project"
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        del r_n["Version"]
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["Version"] = "a.9.9"
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["Version"] = "9.q.9"
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["Version"] = "9.9.q"
        assert not t_releaseit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["Version"] = "0.0.0"
        assert not t_releaseit._check_release_note(r_n)

        pass

    def test_validate_release_notes(self, setup_env):
        working_dir = setup_env
        t_releaseit = releaseit.ReleaseIt(working_dir)
        release_note = {
            "0": {
                "0": {
                    "1": {
                        "FileChanges": [
                            ["filename01.py", "Insert change description here."],
                            ["filename02.txt", "Insert change description here."],
                        ],
                        "Description": [
                            "Changes for 0.0.1 are listed here.",
                            "Add as many description lines as you like.",
                        ],
                        "Title": "Release 0.0.1",
                        "Version": "0.0.1",
                    },
                    "2": {
                        "FileChanges": [
                            ["README.rst", "Update with latest changes."],
                            ["releaseit.py", "Update with latest changes."],
                        ],
                        "Description": [
                            "Changes for 0.0.2 are listed here.",
                            "Add as many description lines as you like.",
                        ],
                        "Title": "Release 0.0.2",
                        "Version": "0.0.2",
                    },
                }
            },
            "1": {
                "1": {
                    "1": {
                        "FileChanges": [
                            ["filename01.py", "Insert change description here."],
                            ["filename02.txt", "Insert change description here."],
                        ],
                        "Description": [
                            "Changes for 1.1.1 are listed here.",
                            "Add as many description lines as you like.",
                        ],
                        "Title": "Release 1.1.1",
                        "Version": "1.1.1",
                    },
                    "3": {
                        "FileChanges": [
                            ["README.rst", "Update with latest changes."],
                            ["releaseit.py", "Update with latest changes."],
                        ],
                        "Description": [
                            "Changes for 1.1.3 are listed here.",
                            "Add as many description lines as you like.",
                        ],
                        "Title": "Release 1.1.3",
                        "Version": "1.1.3",
                    },
                }
            },
        }

        assert t_releaseit._validate_release_notes(release_note)

        r_n = copy.deepcopy(release_note)
        r_n["a"] = r_n["0"]
        del r_n["0"]
        assert not t_releaseit._validate_release_notes(r_n)

        r_n = copy.deepcopy(release_note)
        r_n[0] = r_n["0"].copy()
        del r_n["0"]
        assert not t_releaseit._validate_release_notes(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["1"]["a"] = r_n["1"]["1"]
        del r_n["1"]["1"]
        assert not t_releaseit._validate_release_notes(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["1"][1] = r_n["1"]["1"]
        del r_n["1"]["1"]
        assert not t_releaseit._validate_release_notes(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["1"]["1"]["a"] = r_n["1"]["1"]["1"]
        del r_n["1"]["1"]["1"]
        assert not t_releaseit._validate_release_notes(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["1"]["1"][1] = r_n["1"]["1"]["1"]
        del r_n["1"]["1"]["1"]
        assert not t_releaseit._validate_release_notes(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["0"]["0"]["0"] = r_n["0"]["0"]["1"]
        del r_n["0"]["0"]["1"]
        assert not t_releaseit._validate_release_notes(r_n)

        r_n = copy.deepcopy(release_note)
        del r_n["0"]["0"]["1"]["Description"]
        assert not t_releaseit._validate_release_notes(r_n)

        pass

    def test_do_example(self):
        assert releaseit.do_examples()
        pass


del b_tls
