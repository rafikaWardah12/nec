from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chrome_driver_path = "E:\Fika\Machine_Learning\chromedriver-win64\chromedriver.exe"  # Ganti dengan lokasi ChromeDriver Anda

# chrome_driver_path = "E:/Fika/Machine_Learning/chromedriver-win64/chromedriver.exe"  # Ganti dengan lokasi ChromeDriver Anda
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")  # Maximize the browser window
# driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Edge()
url = "https://nationaleyecenter.id/nlc-cms/"  # Ganti dengan URL yang ingin Anda scraping
driver.get(url)

username = driver.find_element(By.ID, "user_login")
password = driver.find_element(By.ID, "user_pass")
username.send_keys("author-09")
password.send_keys("J0%x(y!i^UstHkNy&Y#tgL1I")

#Click Submit
submit = driver.find_element(By.ID, "wp-submit")
submit.click

#Click Semua Data
# all_post = driver.find_element(By.CLASS_NAME, "wp-first-item")
# all_post.click

def init_urls():
    start_urls = []
    url1 = "https://nationaleyecenter.id/wp-admin/edit.php?post_type=post&all_posts=1"
    url2 = "&paged="

    for page in range(1, 21):
        start_urls.append(url1 + url2 + str(page))
    return start_urls

start_urls = init_urls()
for start_url in start_urls:
    driver.get(start_url)
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "pagination-links")))
    kata_kunci = driver.find_element(By.CSS_SELECTOR, "td.rank_math_seo_details.column-rank_math_seo_details > span:nth-child(3) > span").text
    print(kata_kunci)

driver.get(start_url)
driver.close()

#post-14746 > td.rank_math_seo_details.column-rank_math_seo_details > span:nth-child(3) > span
#post-14288 > td.rank_math_seo_details.column-rank_math_seo_details > span:nth-child(3) > span
#post-14277 > td.rank_math_seo_details.column-rank_math_seo_details > span:nth-child(3) > span