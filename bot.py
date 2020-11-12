from selenium import webdriver
from config import keys
import time


def main(k):
    # Open site
    driver = webdriver.Chrome('./chromedriver')
    driver.get(k['product_url'])

    # Click "Account"
    # driver.find_element_by_xpath('//*[@id="hf-account-flyout"]').click()

    # Click "Sign In"
    # driver.find_element_by_xpath(
    #     '//*[@id="vh-account-menu-root"]/div[2]/div/a[1]').click()
    # time.sleep(1)
    # Type "Email"
    # driver.find_element_by_xpath('//*[@id="email"]').send_keys(k['email'])

    # Type "Password"
    # driver.find_element_by_xpath(
    #     '//*[@id="password"]').send_keys(k['password'])

    # Click "Sign In"
    # driver.find_element_by_xpath('//*[@id="sign-in-form"]/button[1]').click()

    # Click "Add to cart"
    driver.find_element_by_xpath(
        '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button').click()
    time.sleep(2)
    # Click "Checkout"
    driver.find_element_by_xpath(
        '//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[2]/div/button[1]').click()

    # Click "Continue"
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button').click()

    # Click "Continue" 2nd time
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/button').click()

    # Enter:
    # CVV Number
    driver.find_element_by_xpath('//*[@id="cvv-confirm"]').send_keys(k["CVV"])

    # Click "Review Order"
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button').click()

    # Click "Place Order"
    driver.find_element_by_xpath('')


if __name__ == '__main__':
    main(keys)
