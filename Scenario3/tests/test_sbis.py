import pytest
from pages.sbis_page import SbisPage


def test_successful_sbis_tensor(browser):
    sbis_page = SbisPage(browser)
    browser.get('https://sbis.ru/')

    sbis_page.search_plugin()

    file_size_mb, number = sbis_page.download_plugin()

    assert file_size_mb == number


