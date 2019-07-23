#!/usr/bin/python

from allantools import noise
import pytest # NOQA
import sys
sys.path.append("..")


def test_noise():

    N = 500
    w = noise.white(num_points=N)
    b = noise.brown(num_points=N)
    v = noise.violet(num_points=N)
    p = noise.pink(num_points=N)

    # Check that length of sample is as expected
    assert len(w) == N
    assert len(b) == N
    assert len(v) == N
    assert len(p) == N


if __name__ == "__main__":
    test_noise()
