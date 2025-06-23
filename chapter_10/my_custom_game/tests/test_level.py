# tests/test_level.py
from core.level import Level

def test_platform_count():
    lvl = Level('assets/level1.json')
    assert len(lvl.platforms) == 10