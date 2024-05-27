import pytest
from selenium import webdriver
from config import URL


@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.get(URL)
    yield firefox
    firefox.quit()
