import logging


def func(x):
    return x + 1


def test_answer():
    logging.info("开始啦")
    assert func(2) == 4, f"实际结果是3"
