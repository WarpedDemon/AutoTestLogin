from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

loginData = {
    "Username" : "levele1@yahoo.com",
    "Password" : "12345"
}

browser = webdriver.Firefox()
browser.get("https://login.yahoo.com")

try:
    usernameInput = browser.find_element_by_id("login-username")
    usernameInput.send_keys(loginData["Username"])

    print("Entered user name")

    submitButton = browser.find_element_by_id("login-signin")
    submitButton.click()

    print("Hit submit on the form 1")

    WebDriverWait(browser, 3).until(
      expected_conditions.text_to_be_present_in_element(
        (By.ID, 'login-signin'),
        'Sign in'
      )
    )

    #PasswordInput
    passwordInput = browser.find_element_by_id("login-passwd")
    passwordInput.send_keys(loginData["Password"])

    #Second Submit submitButton
    loginButton = browser.find_element_by_id("login-signin")
    loginButton.click()

    WebDriverWait(browser, 10).until(
        (By.ID, 'recaptcha-anchor-label'),
        "I'm not a robot"
    )
    browser.find_element_by_id("recaptcha-checkbox-checkmark").click()

except Exception as e:
    print("Error: " + str(e))
