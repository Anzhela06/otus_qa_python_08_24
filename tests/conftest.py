import pytest

@pytest.fixture(scope="session")
def create_db():
    print("\n Start DB")

    yield

    print("\n End DB")

@pytest.fixture(scope="session")
def create_api(create_db):
    print("\n Start API")

    yield

    print("\n End API")


@pytest.fixture(scope="module")
def send_screenshot():
    yield

    print("\n Screenshot is sent")
