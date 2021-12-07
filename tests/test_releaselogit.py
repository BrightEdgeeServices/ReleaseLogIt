"""Testing releaseit__init__()"""

import copy
from pathlib import Path
import pytest
from beetools.beearchiver import Archiver
import releaselogit


_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem


_TOML_CONTENTS_DEF_STRUCT = {
    "0": {
        "0": {
            "0": {
                "Description": [
                    "List all the changes to the project here.",
                    "Changes listed here will be in the release notes under the above heading.",
                ],
                "Title": "Creation of the project",
            },
        }
    }
}
_TOML_CONTENTS_EXIST_CONTENTS = """\
[0.0.0]
Title = "Creation of the project"
Description = [ "List all the changes to the project here.", "Changes listed here will be in the release notes under the above heading.",]

[0.0.1]
Title = "This is a new release."
Description = [ "Changes for 0.0.1 are listed here.", "Add as many description lines as you like.",]
"""
_TOML_CONTENTS_EXIST_STRUCT = {
    "0": {
        "0": {
            "0": {
                "Description": [
                    "List all the changes to the project here.",
                    "Changes listed here will be in the release notes under the above heading.",
                ],
                "Title": "Creation of the project",
            },
            "1": {
                "Description": [
                    "Changes for 0.0.1 are listed here.",
                    "Add as many description lines as you like.",
                ],
                "Title": "This is a new release.",
            },
        }
    }
}
_TOML_CONTENTS_EXTENDED_CONTENTS = """[0.0.0]
Title = 'Release 0.0.0.'
Description = ['Description line 1 of release 0.0.0',
               'Description line 2 of release 0.0.0']

[0.0.1]
Title = 'Release 0.0.1.'
Description = ['Description line 1 of release 0.0.1',
               'Description line 2 of release 0.0.1']

[0.0.2]
Title = 'Release 0.0.2.'
Description = ['Description line 1 of release 0.0.2',
               'Description line 2 of release 0.0.2']

[0.1.0]
Title = 'Release 0.1.0.'
Description = ['Description line 1 of release 0.1.0',
               'Description line 2 of release 0.1.0']

[0.1.1]
Title = 'Release 0.1.1.'
Description = ['Description line 1 of release 0.1.1',
               'Description line 2 of release 0.1.1']

[0.1.2]
Title = 'Release 0.1.2.'
Description = ['Description line 1 of release 0.1.2',
               'Description line 2 of release 0.1.2']

[0.2.0]
Title = 'Release 0.2.0.'
Description = ['Description line 1 of release 0.2.0',
               'Description line 2 of release 0.2.0']

[0.2.1]
Title = 'Release 0.2.1.'
Description = ['Description line 1 of release 0.2.1',
               'Description line 2 of release 0.2.1']

[0.2.2]
Title = 'Release 0.2.2.'
Description = ['Description line 1 of release 0.2.2',
               'Description line 2 of release 0.2.2']

[1.0.0]
Title = 'Release 1.0.0.'
Description = ['Description line 1 of release 1.0.0',
               'Description line 2 of release 1.0.0']

[1.0.1]
Title = 'Release 1.0.1.'
Description = ['Description line 1 of release 1.0.1',
               'Description line 2 of release 1.0.1']

[1.0.2]
Title = 'Release 1.0.2.'
Description = ['Description line 1 of release 1.0.2',
               'Description line 2 of release 1.0.2']

[1.1.0]
Title = 'Release 1.1.0.'
Description = ['Description line 1 of release 1.1.0',
               'Description line 2 of release 1.1.0']

[1.1.1]
Title = 'Release 1.1.1.'
Description = ['Description line 1 of release 1.1.1',
               'Description line 2 of release 1.1.1']

[1.1.2]
Title = 'Release 1.1.2.'
Description = ['Description line 1 of release 1.1.2',
               'Description line 2 of release 1.1.2']

[1.2.0]
Title = 'Release 1.2.0.'
Description = ['Description line 1 of release 1.2.0',
               'Description line 2 of release 1.2.0']

[1.2.1]
Title = 'Release 1.2.1.'
Description = ['Description line 1 of release 1.2.1',
               'Description line 2 of release 1.2.1']

[1.2.2]
Title = 'Release 1.2.2.'
Description = ['Description line 1 of release 1.2.2',
               'Description line 2 of release 1.2.2']

[2.0.0]
Title = 'Release 2.0.0.'
Description = ['Description line 1 of release 2.0.0',
               'Description line 2 of release 2.0.0']

[2.0.1]
Title = 'Release 2.0.1.'
Description = ['Description line 1 of release 2.0.1',
               'Description line 2 of release 2.0.1']

[2.0.2]
Title = 'Release 2.0.2.'
Description = ['Description line 1 of release 2.0.2',
               'Description line 2 of release 2.0.2']

[2.1.0]
Title = 'Release 2.1.0.'
Description = ['Description line 1 of release 2.1.0',
               'Description line 2 of release 2.1.0']

[2.1.1]
Title = 'Release 2.1.1.'
Description = ['Description line 1 of release 2.1.1',
               'Description line 2 of release 2.1.1']

[2.1.2]
Title = 'Release 2.1.2.'
Description = ['Description line 1 of release 2.1.2',
               'Description line 2 of release 2.1.2']

[2.2.2]
Title = 'Release 2.2.2.'
Description = ['Description line 1 of release 2.2.2',
               'Description line 2 of release 2.2.2']

[2.2.1]
Title = 'Release 2.2.1.'
Description = ['Description line 1 of release 2.2.1',
               'Description line 2 of release 2.2.1']

[2.2.0]
Title = 'Release 2.2.0.'
Description = ['Description line 1 of release 2.2.0',
               'Description line 2 of release 2.2.0']
"""
_TOML_CONTENTS_EXTENDED_STRUCT = {
    "0": {
        "0": {
            "0": {
                "Description": [
                    "Description line 1 of release 0.0.0",
                    "Description line 2 of release 0.0.0",
                ],
                "Title": "Release 0.0.0.",
            },
            "1": {
                "Description": [
                    "Description line 1 of release 0.0.1",
                    "Description line 2 of release 0.0.1",
                ],
                "Title": "Release 0.0.1.",
            },
            "2": {
                "Description": [
                    "Description line 1 of release 0.0.2",
                    "Description line 2 of release 0.0.2",
                ],
                "Title": "Release 0.0.2.",
            },
        },
        "1": {
            "0": {
                "Description": [
                    "Description line 1 of release 0.1.0",
                    "Description line 2 of release 0.1.0",
                ],
                "Title": "Release 0.1.0.",
            },
            "1": {
                "Description": [
                    "Description line 1 of release 0.1.1",
                    "Description line 2 of release 0.1.1",
                ],
                "Title": "Release 0.1.1.",
            },
            "2": {
                "Description": [
                    "Description line 1 of release 0.1.2",
                    "Description line 2 of release 0.1.2",
                ],
                "Title": "Release 0.1.2.",
            },
        },
        "2": {
            "0": {
                "Description": [
                    "Description line 1 of release 0.2.0",
                    "Description line 2 of release 0.2.0",
                ],
                "Title": "Release 0.2.0.",
            },
            "1": {
                "Description": [
                    "Description line 1 of release 0.2.1",
                    "Description line 2 of release 0.2.1",
                ],
                "Title": "Release 0.2.1.",
            },
            "2": {
                "Description": [
                    "Description line 1 of release 0.2.2",
                    "Description line 2 of release 0.2.2",
                ],
                "Title": "Release 0.2.2.",
            },
        },
    },
    "1": {
        "0": {
            "0": {
                "Description": [
                    "Description line 1 of release 1.0.0",
                    "Description line 2 of release 1.0.0",
                ],
                "Title": "Release 1.0.0.",
            },
            "1": {
                "Description": [
                    "Description line 1 of release 1.0.1",
                    "Description line 2 of release 1.0.1",
                ],
                "Title": "Release 1.0.1.",
            },
            "2": {
                "Description": [
                    "Description line 1 of release 1.0.2",
                    "Description line 2 of release 1.0.2",
                ],
                "Title": "Release 1.0.2.",
            },
        },
        "1": {
            "0": {
                "Description": [
                    "Description line 1 of release 1.1.0",
                    "Description line 2 of release 1.1.0",
                ],
                "Title": "Release 1.1.0.",
            },
            "1": {
                "Description": [
                    "Description line 1 of release 1.1.1",
                    "Description line 2 of release 1.1.1",
                ],
                "Title": "Release 1.1.1.",
            },
            "2": {
                "Description": [
                    "Description line 1 of release 1.1.2",
                    "Description line 2 of release 1.1.2",
                ],
                "Title": "Release 1.1.2.",
            },
        },
        "2": {
            "0": {
                "Description": [
                    "Description line 1 of release 1.2.0",
                    "Description line 2 of release 1.2.0",
                ],
                "Title": "Release 1.2.0.",
            },
            "1": {
                "Description": [
                    "Description line 1 of release 1.2.1",
                    "Description line 2 of release 1.2.1",
                ],
                "Title": "Release 1.2.1.",
            },
            "2": {
                "Description": [
                    "Description line 1 of release 1.2.2",
                    "Description line 2 of release 1.2.2",
                ],
                "Title": "Release 1.2.2.",
            },
        },
    },
    "2": {
        "0": {
            "0": {
                "Description": [
                    "Description line 1 of release 2.0.0",
                    "Description line 2 of release 2.0.0",
                ],
                "Title": "Release 2.0.0.",
            },
            "1": {
                "Description": [
                    "Description line 1 of release 2.0.1",
                    "Description line 2 of release 2.0.1",
                ],
                "Title": "Release 2.0.1.",
            },
            "2": {
                "Description": [
                    "Description line 1 of release 2.0.2",
                    "Description line 2 of release 2.0.2",
                ],
                "Title": "Release 2.0.2.",
            },
        },
        "1": {
            "0": {
                "Description": [
                    "Description line 1 of release 2.1.0",
                    "Description line 2 of release 2.1.0",
                ],
                "Title": "Release 2.1.0.",
            },
            "1": {
                "Description": [
                    "Description line 1 of release 2.1.1",
                    "Description line 2 of release 2.1.1",
                ],
                "Title": "Release 2.1.1.",
            },
            "2": {
                "Description": [
                    "Description line 1 of release 2.1.2",
                    "Description line 2 of release 2.1.2",
                ],
                "Title": "Release 2.1.2.",
            },
        },
        "2": {
            "0": {
                "Description": [
                    "Description line 1 of release 2.2.0",
                    "Description line 2 of release 2.2.0",
                ],
                "Title": "Release 2.2.0.",
            },
            "1": {
                "Description": [
                    "Description line 1 of release 2.2.1",
                    "Description line 2 of release 2.2.1",
                ],
                "Title": "Release 2.2.1.",
            },
            "2": {
                "Description": [
                    "Description line 1 of release 2.2.2",
                    "Description line 2 of release 2.2.2",
                ],
                "Title": "Release 2.2.2.",
            },
        },
    },
}
b_tls = Archiver(_PROJ_DESC, _PROJ_PATH)


class TestReleaseLogIt:
    def test__init__default(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        t_releaselogit = releaselogit.ReleaseLogIt(
            working_dir, p_parent_log_name=_PROJ_NAME
        )
        assert t_releaselogit.rel_notes == _TOML_CONTENTS_DEF_STRUCT
        assert t_releaselogit.rel_list == [["0", "0", "0"]]
        assert t_releaselogit.src_pth.exists()
        assert t_releaselogit.success
        pass

    def test__init__existing(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXIST_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)

        assert t_releaselogit.rel_notes == _TOML_CONTENTS_EXIST_STRUCT
        assert t_releaselogit.rel_list == [["0", "0", "0"], ["0", "0", "1"]]
        assert t_releaselogit.src_pth.exists()
        assert t_releaselogit.success
        pass

    def test__init__extended(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)

        assert t_releaselogit.rel_notes == _TOML_CONTENTS_EXTENDED_STRUCT
        assert t_releaselogit.rel_list == [
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
        assert t_releaselogit.src_pth.exists()
        assert t_releaselogit.success
        pass

    def test__iter__(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXIST_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)

        assert isinstance(t_releaselogit, releaselogit.ReleaseLogIt)
        assert t_releaselogit.cur_pos == 0
        pass

    def test__next__(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXIST_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)
        elements = iter(t_releaselogit)

        assert next(elements) == {
            "Description": [
                "List all the changes to the project here.",
                "Changes listed here will be in the release notes under the above heading.",
            ],
            "Title": "Creation of the project",
        }
        assert next(elements) == {
            "Description": [
                "Changes for 0.0.1 are listed here.",
                "Add as many description lines as you like.",
            ],
            "Title": "This is a new release.",
        }
        with pytest.raises(StopIteration):
            assert next(elements)

    def test__repr__extended(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)

        assert repr(t_releaselogit) == 'ReleaseLogIt(0,"0.0.0")'
        pass

    def test__str__extended(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)

        assert str(t_releaselogit) == "0.0.0"
        pass

    def test_add_release_note(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        release_note_100 = {
            "1": {
                "0": {
                    "0": {
                        "Description": [
                            "Description line 1.",
                            "Description line 2.",
                        ],
                        "Title": "Release change 1.0.0",
                    }
                }
            }
        }

        release_note_010 = {
            "0": {
                "1": {
                    "0": {
                        "Description": [
                            "Description line 1.",
                            "Description line 2.",
                        ],
                        "Title": "Release change 0.1.0",
                    }
                }
            }
        }
        release_note_001 = {
            "0": {
                "0": {
                    "1": {
                        "Description": [
                            "Description line 1.",
                            "Description line 2.",
                        ],
                        "Title": "Release change 0.0.1",
                    }
                }
            }
        }
        release_note_000 = {
            "0": {
                "0": {
                    "0": {
                        "Description": [
                            "Description line 1.",
                            "Description line 2.",
                        ],
                        "Title": "Release change 0.0.0",
                    }
                }
            }
        }
        release_note_default = {
            "Description": [
                "Description line 1.",
                "Description line 2.",
            ],
            "Title": "Release change 0.0.0",
        }

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)
        assert t_releaselogit.add_release_note(release_note_100)
        assert t_releaselogit.add_release_note(release_note_010)
        assert t_releaselogit.add_release_note(release_note_001)
        assert not t_releaselogit.add_release_note(release_note_000)
        assert not t_releaselogit.add_release_note(release_note_default)

        assert t_releaselogit.rel_notes == {
            "0": {
                "0": {
                    "0": {
                        "Description": [
                            "List all the changes to the project here.",
                            "Changes listed here will be in the release notes under the above heading.",
                        ],
                        "Title": "Creation of the project",
                    },
                    "1": {
                        "Description": [
                            "Description line 1.",
                            "Description line 2.",
                        ],
                        "Title": "Release change 0.0.1",
                    },
                },
                "1": {
                    "0": {
                        "Description": [
                            "Description line 1.",
                            "Description line 2.",
                        ],
                        "Title": "Release change 0.1.0",
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
                        "Title": "Release change 1.0.0",
                    }
                }
            },
        }
        assert t_releaselogit.rel_list == [
            ["0", "0", "0"],
            ["0", "0", "1"],
            ["0", "1", "0"],
            ["1", "0", "0"],
        ]
        assert t_releaselogit.rel_cntr == 4
        pass

    def test_check_release_note(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)
        release_note = {
            "9": {
                "9": {
                    "9": {
                        "Description": [
                            "Description line 1.",
                            "Description line 2.",
                        ],
                        "Title": "Release 9.9.9",
                    }
                }
            }
        }

        assert t_releaselogit._check_release_note(release_note)

        r_n = copy.deepcopy(release_note)
        del r_n["9"]["9"]["9"]["Description"]
        assert not t_releaselogit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["9"]["9"]["9"]["Description"] = "abc"
        assert not t_releaselogit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["9"]["9"]["9"]["Description"] = []
        assert not t_releaselogit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["9"]["9"]["9"]["Description"] = ["abc", 123]
        assert not t_releaselogit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        del r_n["9"]["9"]["9"]["Title"]
        assert not t_releaselogit._check_release_note(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["9"]["9"]["9"]["Title"] = "Creation of the project"
        assert not t_releaselogit._check_release_note(r_n)

        pass

    def test_do_example(self):
        assert releaselogit.do_examples()
        pass

    def test_get_release_note_by_title(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)

        assert t_releaselogit.get_release_note_by_title("Release 1.1.1.") == {
            "Title": "Release 1.1.1.",
            "Description": [
                "Description line 1 of release 1.1.1",
                "Description line 2 of release 1.1.1",
            ],
        }
        assert t_releaselogit.get_release_note_by_title("Release 9.9.9.") is None

    def test_get_release_note_by_version(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)

        assert t_releaselogit.get_release_note_by_version("1.1.1") == {
            "Title": "Release 1.1.1.",
            "Description": [
                "Description line 1 of release 1.1.1",
                "Description line 2 of release 1.1.1",
            ],
        }
        assert t_releaselogit.get_release_note_by_version("9.9.9") is None
        pass

    def test_get_release_titles(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXIST_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)

        assert t_releaselogit.get_release_titles() == [
            "Creation of the project",
            "This is a new release.",
        ]
        assert t_releaselogit.success
        pass

    def test_has_title(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)

        assert t_releaselogit.has_title("Release 1.1.1.")
        assert not t_releaselogit.has_title("Release 9.9.9.")
        pass

    def test_latest(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)

        assert t_releaselogit.latest() == {
            "Title": "Release 2.2.2.",
            "Description": [
                "Description line 1 of release 2.2.2",
                "Description line 2 of release 2.2.2",
            ],
        }
        pass

    def test_oldest(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXTENDED_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)

        assert t_releaselogit.oldest() == {
            "Title": "Release 0.0.0.",
            "Description": [
                "Description line 1 of release 0.0.0",
                "Description line 2 of release 0.0.0",
            ],
        }
        pass

    def test_validate_release_notes(self, setup_env):
        working_dir = setup_env
        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)
        release_note = {
            "0": {
                "0": {
                    "1": {
                        "Description": [
                            "Changes for 0.0.1 are listed here.",
                            "Add as many description lines as you like.",
                        ],
                        "Title": "Release 0.0.1",
                    },
                    "2": {
                        "Description": [
                            "Changes for 0.0.2 are listed here.",
                            "Add as many description lines as you like.",
                        ],
                        "Title": "Release 0.0.2",
                    },
                }
            },
            "1": {
                "1": {
                    "1": {
                        "Description": [
                            "Changes for 1.1.1 are listed here.",
                            "Add as many description lines as you like.",
                        ],
                        "Title": "Release 1.1.1",
                    },
                    "3": {
                        "Description": [
                            "Changes for 1.1.3 are listed here.",
                            "Add as many description lines as you like.",
                        ],
                        "Title": "Release 1.1.3",
                    },
                }
            },
        }

        assert t_releaselogit._validate_release_log(release_note)

        r_n = copy.deepcopy(release_note)
        r_n["a"] = r_n["0"]
        del r_n["0"]
        assert not t_releaselogit._validate_release_log(r_n)

        r_n = copy.deepcopy(release_note)
        r_n[0] = r_n["0"].copy()
        del r_n["0"]
        assert not t_releaselogit._validate_release_log(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["1"]["a"] = r_n["1"]["1"]
        del r_n["1"]["1"]
        assert not t_releaselogit._validate_release_log(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["1"][1] = r_n["1"]["1"]
        del r_n["1"]["1"]
        assert not t_releaselogit._validate_release_log(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["1"]["1"]["a"] = r_n["1"]["1"]["1"]
        del r_n["1"]["1"]["1"]
        assert not t_releaselogit._validate_release_log(r_n)

        r_n = copy.deepcopy(release_note)
        r_n["1"]["1"][1] = r_n["1"]["1"]["1"]
        del r_n["1"]["1"]["1"]
        assert not t_releaselogit._validate_release_log(r_n)

        r_n = copy.deepcopy(release_note)
        del r_n["0"]["0"]["1"]["Description"]
        assert not t_releaselogit._validate_release_log(r_n)

        pass

    def test_write_toml(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        (working_dir / "release.toml").write_text(_TOML_CONTENTS_EXIST_CONTENTS)

        t_releaselogit = releaselogit.ReleaseLogIt(working_dir)
        t_releaselogit.write_toml()

        assert t_releaselogit.src_pth.read_text() == _TOML_CONTENTS_EXIST_CONTENTS
        pass


del b_tls
