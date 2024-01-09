from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import time
import pandas as pd

driver = webdriver.Chrome()

pixel = 0


def Hastag(keyword):
    global pixel

    url = 'https://pantip.com/search?q=' + keyword

    # Open the URL in the browser
    driver.get(url)
    time.sleep(3)

    for i in range(1000):
        driver.execute_script("window.scrollTo(0, {})".format(pixel))
        time.sleep(3)
        pixel = pixel + 10000
    
    page_html = driver.page_source

    data = soup(page_html, 'html.parser')
    pantext = data.findAll('div', {'class': 'pt-list-item__sr__content__inner'})
    
    # สร้างลิสต์เพื่อเก็บข้อมูล
    results = []
    for i, tw in enumerate(pantext):
        text = tw.text.strip()
        try:
            date_part = text.split('-')[0].strip()
            data_part = text.split('-')[1].strip()
            if data_part != "":
                result = {
                    'Number': i + 1,
                    'Text': data_part,
                    'Date': date_part
                }
                results.append(result)
                print(f'{i + 1}: {data_part} - {date_part}')
                print('------------------------')
        except IndexError:
            # จัดการข้อผิดพลาดเมื่อ index ไม่ถูกต้อง
            print(f"Skipping entry {i + 1} due to IndexError")
    
    return results

# เรียกใช้ฟังก์ชัน
data_results = Hastag('โควิด')

# สร้าง DataFrame จากลิสต์ของข้อมูล
df = pd.DataFrame(data_results)

# เขียนลงใน Excel
df.to_excel('scarpe.xlsx', index=False)

# ปิดเบราว์เซอร์
driver.quit()
