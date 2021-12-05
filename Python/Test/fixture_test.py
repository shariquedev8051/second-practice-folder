import pytest


# @pytest.fixture
# def setup():
#     print('Hello there user!')
#     yield
#     print("\nBye take care")


# No need to import fixture pytest will autometically find it in conftest
# def test_fixture_demo1(setup):
#     print('Hello from demo1!')

"""
# fixture will be applied to all the test cases
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo2(self):
        print('Hello from demo2!')

    def test_fixture_demo3(self):
        print('Hello from demo3!')

    def test_fixture_demo4(self):
        print('Hello from demo4!')
"""


"""
# To load the data using fixture
# We to pass it as argument when you are returning something in the return
@pytest.mark.usefixtures('load_data')
class Testexample2:

    def test_editProfile(self, load_data):
        print()
        for i in load_data:
            print(i)
"""


def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])
    print(crossBrowser[1])


