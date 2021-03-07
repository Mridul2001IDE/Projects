from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()
def siteLogin():
    driver.get("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=c8c52a1f-00a7-41f0-af5b-e6fc8ec893f1&&client-request-id=dd32a5e9-1468-442c-9e74-513c91defa26&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=30b1377d-f0fb-4878-9978-92258d7bffca&domain_hint=")
    driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]").send_keys("i19ma007@svnitsuratg.onmicrosoft.com")
    driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input").send_keys("I19ma@007")
    driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input").click()
    driver.find_element_by_xpath("/html/body/promote-desktop/div/div/div/div[1]/div[2]/div/a").click()

siteLogin()

HU201="/html/body/div[2]/div[2]/div[2]/div[1]/teams-grid/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[2]"
MA205DMS = "/html/body/div[2]/div[2]/div[2]/div[1]/teams-grid/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[3]"
EOA = "/html/body/div[2]/div[2]/div[2]/div[1]/teams-grid/div/div[2]/div[1]/div[1]/div/div[1]/div[3]/div[2]"
teams = [HU201,MA205DMS,EOA]

time.sleep(5)

for team in teams:
    driver.find_element_by_xpath(team).click()
    time.sleep(5)
    driver.back()
    time.sleep(2)


