import pytest
import logging

"""
暂时不运行
如果某个用例暂时有问题，或者用例写好了，但是功能没写好，我们可以标记先跳过这个用例
更进一步，我们可以有条件得跳过某些case，比如我们先看看当前的环境，是否在ICU，如果在的话，就不管心跳了。
"""


def my_heart_status():
    return "stopped"


def my_heartbeat():
    return -1


@pytest.mark.p0
def test_my_heart_status():
    logging.info("即将检查我的心脏")
    assert my_heart_status() == "running"


@pytest.mark.skip(reason="对应功能未实现")
def test_my_heartbeat():
    logging.info("即将检查我的心脏")
    assert 50 < my_heartbeat() < 100
