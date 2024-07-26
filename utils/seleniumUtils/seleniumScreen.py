from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import ImageGrab

# 创建WebDriver对象，指定使用Chrome浏览器。
driver = webdriver.Edge()

# 打开网页
driver.get('http://mall.gqhsps.com/#/login')

# 最大化浏览器窗口
driver.maximize_window()

# 输入账号密码
username_element = driver.find_element(By.NAME, 'username')
username_element.send_keys('admin')

userpassword_element = driver.find_element(By.NAME, 'password')
userpassword_element.send_keys('Hs69606259.')
userpassword_element.send_keys(Keys.RETURN)

sleep(5)
driver.get('http://mall.gqhsps.com/#/financial/summaryOfFinancialStatements')

sleep(5)
# 滚动到页面底部，确保页面加载完全
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

sleep(2)
# 截取当前窗口的屏幕截图
full_screen_screenshot = ImageGrab.grab()
# 获取浏览器窗口的位置
window_position = driver.get_window_position()
# 获取浏览器窗口的大小
window_size = driver.get_window_size()
# 截取浏览器窗口内的部分屏幕截图
browser_view_screenshot = full_screen_screenshot.crop((
    window_position['x'],  # left
    window_position['y'],  # top
    window_position['x'] + window_size['width'],  # right
    window_position['y'] + window_size['height']  # bottom
))
# 保存截图
browser_view_screenshot.save('browser_screenshot.png')


driver.quit()
