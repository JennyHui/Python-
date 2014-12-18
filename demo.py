from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
dr=webdriver.Firefox()
action = ActionChains(dr)
dr.get("http://www.jd.com")
jd_tx=dr.find_element_by_css_selector("div.item.fore3 > span > h3 > a:nth-child(3)")
action.move_to_element(jd_tx).perform()

time.sleep(2)
js="""document.getElementsByClassName("fore2")[6].getElementsByTagName("a")[2].click()"""
dr.execute_script(js)
time.sleep(2)
print dr.title
time.sleep(5)
dr.quit()

