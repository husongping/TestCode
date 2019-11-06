from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://132.232.44.158:9999/shopxo/admin.php?s=/admin/logininfo.html")
name = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[1]/input')
name.send_keys('admin')
pswd = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[2]/input')
pswd.send_keys('shopxo')
delu = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')
delu.click()
time.sleep(3)


yhgl = driver.find_element_by_xpath('//*[@id="admin-offcanvas"]/div/ul/li[5]/a/span[2]')
yhgl.click()
time.sleep(1)
yhlb = driver.find_element_by_xpath('//*[@id="power-menu-126"]/li/a/span')
yhlb.click()

f = driver.find_element_by_xpath('//*[@id="ifcontent"]')
driver.switch_to_frame(f)


time.sleep(1)
xz = driver.find_element_by_xpath('/html/body/div[1]/div/div/a[1]')
xz.click()
a = 'husongping'
time.sleep(1)
yhm = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/input')
yhm.send_keys(a)

mm = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[13]/input')
mm.send_keys('123456')

bc = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[14]/button')
bc.click()
time.sleep(2)

nm = driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/ul/li[1]')
if a in nm.text:
    print("添加成功")
else:
    print("添加失败")
# driver.quit()
from selenium.webdriver.support.ui import WebDriverWait
