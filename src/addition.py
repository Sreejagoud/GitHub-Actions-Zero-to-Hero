# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 7) == 5
    assert add(1, -1) == 0
    assert add(2, 2) == 4
