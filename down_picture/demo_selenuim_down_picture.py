from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download():
    driver_path = "/Users/kaidongwang/Downloads/chromedriver_mac64/chromedriver"
    driver = webdriver.Chrome(driver_path)
    driver.get("https://meirentu.cc/pic/196937205210-1.html")


    element = driver.find_element(By.XPATH, value="//img[@alt='熊小诺']").screenshot("a.png")
    # 创建ActionChains对象
    actions = ActionChains(driver)

    # 在图片元素上右键单击
    actions.context_click(element).perform()

    # 等待弹出菜单出现
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "contextMenu")))

    # 选择"Save Link As"选项
    actions.click(driver.find_element_by_id("contextMenu")).perform()

    # 等待弹出菜单消失
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.ID, "contextMenu")))

    # 模拟按键回车确认保存选项
    actions.send_keys(webdriver.Keys.RETURN).perform()

    # 等待图片下载完成
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.TAG_NAME, "iframe")))

    # 获取图片的URL
    image_url = driver.current_url

    # 将图片保存到本地
    with open("uxiao_nuo.jpg", "wb") as file:
        file.write(driver.page_source)

        # 关闭驱动程序
    driver.quit()


if __name__ == '__main__':
    download()
