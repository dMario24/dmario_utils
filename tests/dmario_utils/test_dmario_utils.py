import sys
import dmario_utils


def test_ping():
    sys.argv = ['foo', '10']
    dmario_utils.ping()

