from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# ระบุพาธของ ChromeDriver
chrome_driver_path = "D:/webdriver/chromedriver.exe"

# เริ่มต้น WebDriver
driver = webdriver.Chrome()
# ขยายหน้าต่างเบราวเซอร์ให้เต็มหน้าจอ
driver.maximize_window()

# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")

# ค้นหาปุ่ม "เข้าสู่ระบบ" ตาม ID
login_button = driver.find_element(By.ID, "loginNavbar")

login_button.click()

time.sleep(2)
# กรอก ID number และ password
id_input = driver.find_element(By.ID, "LoginID_Card")
password_input = driver.find_element(By.ID, "LoginPassword")

id_input.send_keys("1700401342745")

time.sleep(1)

password_input.send_keys("0967305591")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย ID
login_button = driver.find_element(By.ID, "Login")

# คลิกปุ่ม "เข้าสู่ระบบ"
login_button.click()

# รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

# ค้นหาและคลิกที่เมนูแฮมเบอร์เกอร์ตาม ID
menu_button = driver.find_element(By.ID, "hamNavbar")
menu_button.click()

time.sleep(2)

# ค้นหาและคลิกที่ "โปรไฟล์"
profile_button = driver.find_element(By.XPATH, "//div[@aria-label='โปรไฟล์']")
profile_button.click()

time.sleep(2)

# ใช้ JavaScript เลื่อนหน้าเว็บลงเพื่อเปิดเส้นทางให้กับองค์ปิด
driver.execute_script("window.scrollTo(0, 2000);")

# ค้นหาและคลิกที่ปุ่ม "แก้ไขโปรไฟล์" ตาม ID
button_edit = driver.find_element(By.ID, "ProfileloadEdit")
button_edit.click()

# ค้นหา textbox ที่ชื่อว่า first name ตาม ID
first_name_input = driver.find_element(By.ID, "Profilefirst_name")

# ล้างข้อมูลใน textbox ที่ชื่อว่า first name
first_name_input.clear()

# กรอกข้อมูล "ต่อ" ใน textbox ที่ชื่อว่า first name
first_name_input.send_keys("ต่อ")

time.sleep(5)

# ค้นหาและคลิกที่ปุ่มบันทึกตาม ID
save_button = driver.find_element(By.ID, "Profilesubmit")
save_button.click()

# รอสักครู่เพื่อดูผลลัพธ์หรือปิดเบราวเซอร์
time.sleep(5)

# ปิดเบราวเซอร์
driver.quit()
