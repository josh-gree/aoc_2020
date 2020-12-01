import pytest

from textwrap import dedent

from .day_1 import sol_part_1, sol_part_2


@pytest.fixture
def input_file(tmp_path):
    file = tmp_path / "input"
    s = """
    1721
    979
    366
    299
    675
    1456
    """
    file.write_text(dedent(s).strip())
    return file


def test_part_1(input_file):

    with open(input_file) as f:
        inp = f.read()

    assert sol_part_1(inp) == 514579


def test_part_2(input_file):

    with open(input_file) as f:
        inp = f.read()

    assert sol_part_2(inp) == 241861950
