import pytest
from pages.sbis_page import SbisPage, TensorPage


def test_successful_sbis_tensor(browser):
    sbis_page = SbisPage(browser)
    browser.get('https://sbis.ru/')

    sbis_page.click_contacts()
    sbis_page.click_banner()

    tensor_page = TensorPage(browser)

    tensor_page.switch_to_window(1)

    text = tensor_page.get_banner_title_text()

    assert 'Сила в людях' in text

    tensor_page.click_banner_link()

    size1, size2, size3, size4 = tensor_page.size_image()
    assert size1 == size2 == size3 == size4









