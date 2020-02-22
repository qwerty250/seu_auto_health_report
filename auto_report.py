INFO = ['YOUR_ID', 'YOUR_PASSWORD']
from selenium import webdriver
import time
import tkinter.messagebox

browser = webdriver.Chrome('./webdriver/chromedriver')

try:
    browser.get('https://xgbxscwx.seu.edu.cn/')
    time.sleep(5)

    fields = browser.find_elements_by_class_name('auth_input')
    fields[0].send_keys(INFO[0])
    time.sleep(1)
    fields[1].send_keys(INFO[1])
    time.sleep(1)

    login_btn = browser.find_elements_by_class_name('auth_login_btn')
    login_btn[0].click()
    time.sleep(5)

    browser.get('https://xgbxscwx.seu.edu.cn/?#/ncp-daily-report')
    time.sleep(5)

    submit_btn = browser.find_element_by_class_name("el-button")
    submit_btn.click()

    tkinter.messagebox.showinfo("成功", "成功填报健康情况。")
    browser.quit()

except Exception as e:
    print(e)
    tkinter.messagebox.showerror("未能填报", "出现错误，未能自动填报。请手动操作。")
    browser.quit()