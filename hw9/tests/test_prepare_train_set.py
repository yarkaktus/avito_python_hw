import os

import pandas as pd
import pytest

from hw9.tests.data import hard_case
from hw9.tests.data import simple_case2
from hw9.tests.data import simple_case3
from hw9.utils import prepare_train_set

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def test_bad_path():
    with pytest.raises(FileNotFoundError):
        prepare_train_set("bad_path", 0, 0, 0)


def test_hard_case():
    logs_dir = os.path.join(BASE_DIR, "logs", "case1")
    df = pd.DataFrame(hard_case)
    assert df.to_dict() == prepare_train_set(logs_dir, 4, 2, 30).to_dict()


def test_simple_case2():
    logs_dir = os.path.join(BASE_DIR, "logs", "case2")
    df = pd.DataFrame(simple_case2)
    assert df.to_dict() == prepare_train_set(logs_dir, 2, 2, 30).to_dict()


def test_simple_case3():
    logs_dir = os.path.join(BASE_DIR, "logs", "case3")
    df = pd.DataFrame(simple_case3)
    assert df.to_dict() == prepare_train_set(logs_dir, 4, 0, 30).to_dict()


def test_empty_path():
    logs_dir = os.path.join(BASE_DIR, "logs", "empty_path")
    columns = ["site1", "time1", "site2", "time2", "site3", "time3", "site4", "time4", "user_id"]
    df = pd.DataFrame(columns=columns)
    assert df.to_dict() == prepare_train_set(logs_dir, 4, 2, 30).to_dict()
