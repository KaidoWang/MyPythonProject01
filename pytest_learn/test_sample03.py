import pytest
import logging

"""
打标签
使用pytest的mark能力，我们可以给case打tag，然后按tag来运行不同的case。比如最基础的，区分P0与P1 case。
"""


def my_heart_status():
    return "stopped"


def my_heartbeat():
    return -1


@pytest.mark.p0
def test_my_heart_status():
    logging.info("即将检查我的心脏")
    assert my_heart_status() == "running"


@pytest.mark.p1
def test_my_heartbeat():
    logging.info("即将检查我的心脏")
    assert 50 < my_heartbeat() < 100
