import pytest
from pages.sbis_page import SbisPage


def test_successful_sbis_tensor(browser):
    sbis_page = SbisPage(browser)
    browser.get('https://sbis.ru/')

    sbis_page.click_contacts()
    region, city = sbis_page.verify_city()
    assert region == 'Костромская обл.' and city == 'Кострома'

    region, city, title, url = sbis_page.change_and_verify_new_region()

    assert region == 'Камчатский край' and city == 'Петропавловск-Камчатский' and 'Камчатский край' in title and '41-kamchatskij-kraj' in url








