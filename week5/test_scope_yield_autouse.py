import pytest

@pytest.fixture(scope="module")
def setup_module():
    print("\n[setup_module]")
    return {"status": "module"}

@pytest.fixture(scope="session")
def setup_session():
    print("\n[setup_session]")
    return {"status": "session"}

def test_one(setup_module, setup_session):
    assert setup_module["status"] == "module"
    assert setup_session["status"] == "session"

def test_two(setup_module, setup_session):
    assert setup_module["status"] == "module"
    assert setup_session["status"] == "session"