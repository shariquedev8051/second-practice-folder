import pytest

# fixture it will be available for all test_cases
# @pytest.fixture
@pytest.fixture(scope="class") # To limit the fixture to the class only
def setup():
    print('It will run befor the test!')
    yield
    print('It will run after the test!')


# To load data from the fixture
@pytest.fixture()
def load_data():
    print('user data is being created!')
    return ['Mohammad','Sharique','shariquedev1.0@gmail.com']


"""
# To send data multiple times one data at time
@pytest.fixture(params=['Chrome','Firefox','IE'])
def crossBrowser(request):
    return request.param
"""

# To send multiple data at time
@pytest.fixture(params=[('sharique','Mohammad'),('Nargis','Bano'),])
def crossBrowser(request):
    return request.param # use param not params 