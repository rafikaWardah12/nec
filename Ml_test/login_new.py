from selenium import webdriver
import json

# Buka file cookies.json dan baca cookies
with open('cookie.json', 'r') as file:
    cookies = json.load(file)

# Inisialisasi webdriver Selenium
driver = webdriver.Chrome()
url = "https://nationaleyecenter.id/nlc-cms/"  # Ganti dengan URL yang ingin Anda scraping
driver.get(url)

# Setel cookie untuk setiap kunci dalam cookies
for cookie in cookies:
    driver.add_cookie(cookie)

# Refresh halaman agar cookie-nya diaplikasikan
driver.refresh()

# Sekarang Anda dapat melanjutkan dengan tindakan-tindakan yang memerlukan otentikasi,
# misalnya mengakses halaman yang terproteksi atau melakukan scraping yang memerlukan otentikasi.

# Contoh: Mengakses halaman setelah login
driver.get("https://nationaleyecenter.id/wp-admin/")

# Sekarang Anda dapat melakukan scraping atau tindakan lainnya yang diperlukan setelah login.
