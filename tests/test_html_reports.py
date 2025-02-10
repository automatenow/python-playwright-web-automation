import re
import allure
import pytest
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("/")

    # Expect a title to contain 'automateNow'
    expect(page).to_have_title(re.compile("automateNow"))

def test_fail_test(page: Page):
    page.goto("/")

    # Expect a title wrong title
    expect(page).to_have_title(re.compile("123"))

@pytest.mark.skip(reason="This test is skipped on purpose")
def test_skip_test(page: Page):
    page.goto("/")

def test_form_input(page: Page):
    page.goto("/")

    page.get_by_text("Form Fields").click()
    page.get_by_test_id("name-input").type("Marco")
    # page.wait_for_timeout(2000)

def test_take_screenshot(page: Page):
    page.goto("/")

    # Take a screenshot
    my_screenshot = page.screenshot()

    # Attach screenshot to Allure Report
    allure.attach(
        my_screenshot,
        name="full-page",
        attachment_type=allure.attachment_type.PNG
    )