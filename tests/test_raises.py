# test_raises.py

import pytest

def test_raises():
    with pytest.raises(TypeError) as e:
        connect('localhost', '6379')
    exec_msg = e.value.args[0]
    assert exec_msg == 'port type must be int'