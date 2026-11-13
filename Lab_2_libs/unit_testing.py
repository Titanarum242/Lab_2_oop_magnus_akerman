from pytest import raises
from space_3d import Translate

#print(Translate())

def test_valid_init():
    t1=Translate(1,2,4)
    assert t1(1,2,4)


def test_invalid_init():
    with raises(TypeError):
        Translate(1, 2, "3")
