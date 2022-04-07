import pytest


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def miltiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def diveideEvenlly(a,b):
    return a//b

def mudolo(a,b):
    return a%b

def sqrt(a):
   return a **0.5

'''---------------TESTS---------------'''
def test_add():
    assert 10 == add(5, 5)

def test_add2():
    assert 15 == add(5,5)

def test_subtract():
    assert 10 == subtract(12,2)

def test_subtract2():
    assert 10 == subtract(10,2)

def test_miltiply():
    assert 10 == miltiply(5,2)

def test_miltiply2():
    assert 10 == miltiply(5,5)

def test_divide():
    assert 10 == divide(20,2)

def test_divide2():
    assert 10 == divide(10,2)

def test_diveideEvenlly():
    assert 2 == diveideEvenlly(5,2)

def test_diveideEvenlly2():
    assert 2.50 == diveideEvenlly(5,3)

def test_mudolo():
    assert 1 == mudolo(10,3)

def test_mudolo2():
    assert 2 == mudolo(10,3)

def test_sqrt():
    assert 2 == sqrt(a=4)

def test_sqrt2():
    assert 16 == sqrt(a=2)
