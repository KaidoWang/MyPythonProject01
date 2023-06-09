import logging

import pytest

"""
同一个用例不同的参数:
比如现在有一个查询的测试接口，我们要测试不同查询条件下接口是否符合预期。从最简单的开始：不同的page size：
可以看到，虽然我们只写了一个用例，但是利用pytest.mark.parametrize，我们实现了类似表驱动测试的效果。
"""


@pytest.mark.parametrize("args", [10, 20])
def test_query_page_size(args):
    logging.info(args)
