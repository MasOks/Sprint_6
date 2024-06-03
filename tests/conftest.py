import pytest
from selenium import webdriver
from config import URL1


@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.get(URL1)
    yield firefox
    firefox.quit()
