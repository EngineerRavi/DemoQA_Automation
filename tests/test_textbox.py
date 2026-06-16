from pages.textbox_page import TextBoxPage

def test_textbox_submission(setup):
    driver = setup
    driver.get("https://demoqa.com")

    assert "DEMOQA" in driver.page_source
# def test_textbox_form(setup):
#     driver = setup

#     driver.get("https://demoqa.com/text-box")

#     textbox = TextBoxPage(driver)

#     textbox.enter_username("Ravi")
#     textbox.enter_email("ravi@test.com")
#     textbox.enter_current_address("Delhi")
#     textbox.enter_permanent_address("India")
#     textbox.click_submit()

#     assert "Ravi" in driver.page_source