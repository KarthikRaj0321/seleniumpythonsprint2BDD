from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@given(u'I open the application url in the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.asianpaints.com/")


@given(u'I search colour catalogue in search')
def step_impl(context):
    context.driver.find_element(By.NAME, "q").send_keys("colour catalogue")


@when(u'I click search')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"headerSearch\"]/div[1]/form/div/button/span").click()


@when(u'I see colour catalogue')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/section/div/div/div[2]/div/div/div["
                                           "2]/div/div/a/div").click()

@then(u'I can see various colours')
def step_impl(context):
   context.driver.quit()


@given(u'I hover the mouse on paints and colours tab')
def step_impl(context):
    element_to_hover_over = context.driver.find_element(By.XPATH, "//span[@class='iconTextLinks__text "
                                                               "visible-in-Desktop'][normalize-space()='PAINTS & "
                                                               "COLOURS']")
    actions = ActionChains(context.driver)
    actions.move_to_element(element_to_hover_over).perform()


@when(u'I click the interior textures')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[normalize-space()='Interior Textures']").click()


@then(u'I should see interior textures')
def step_impl(context):
    context.driver.quit()


@when(u'I click the Exterior textures')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[normalze-space()='Exterior Textures']").click()


@then(u'I can see various filters')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                 "//section[@class='color-palettes-main-wrapper']//li[1]//a[1]//span[1]").is_displayed()


@given(u'I hover the mouse on the paints and colours tab')
def step_impl(context):
    element_to_hover_over = context.driver.find_element(By.XPATH, "//span[@class='iconTextLinks__text "
                                                                  "visible-in-Desktop'][normalize-space()='PAINTS & "
                                                                  "COLOURS']")
    actions = ActionChains(context.driver)
    actions.move_to_element(element_to_hover_over).perform()


@when(u'I click the exterior paints')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[normalize-space()='Exterior Paints']").click()


@then(u'I can see various paints')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//img[@title='Exterior Wall Paints - Asian Paints']").is_displayed()


@when(u'I click the metal paints')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@class='track_third_level'][normalize-space()='Metal Paints']").click()


@then(u'I can see various metal paints')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@href='https://www.asianpaints.com/products/wood-and-metals"
                                           "/metal-enamels/apcolite-premium-gloss-enamel.html']").is_displayed()