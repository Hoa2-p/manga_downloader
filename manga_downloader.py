import requests
from bs4 import BeautifulSoup
import os
import re
import logging
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import time

"""
Manga Downloader

A tool to download manga images from nhxxxai.net by entering URLs via the console.
IMPORTANT: This tool is designed exclusively for nhxxxai.net and will not work with other websites.
Note: Adjust URL pattern in is_valid_url() if using a different site.

Dependencies: requests, beautifulsoup4, selenium, webdriver-manager
"""

# Thiết lập logging để theo dõi quá trình
logging.basicConfig(level=logging.DEBUG)

# Headers để tải ảnh bằng requests
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'vi',
    'Referer': 'https://nhentai.net/language/english/?page=424',
}

def create_directory(directory):
    """Tạo thư mục nếu chưa tồn tại"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_page_count(url, driver):
    """Lấy số lượng trang của bộ truyện bằng Selenium"""
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.tag-container, body'))
        )
        html = driver.page_source
        with open('debug.html', 'w', encoding='utf-8') as f:
            f.write(html)
        soup = BeautifulSoup(html, 'html.parser')

        page_container = soup.find('div', class_='tag-container', string=re.compile(r'Pages:', re.I))
        if page_container:
            page_tag = page_container.find('span', class_='name')
            if page_tag and page_tag.text.isdigit():
                logging.info(f"Tìm thấy số trang trong HTML: {page_tag.text}")
                return int(page_tag.text)

        script_tags = soup.find_all('script')
        for script in script_tags:
            if script.string and 'window._gallery' in script.string:
                try:
                    json_match = re.search(r'JSON\.parse\("(.+?)"\)', script.string, re.DOTALL)
                    if json_match:
                        json_str = json_match.group(1)
                        json_str = bytes(json_str, 'utf-8').decode('unicode_escape')
                        gallery_data = json.loads(json_str)
                        if 'num_pages' in gallery_data:
                            logging.info(f"Tìm thấy số trang trong JSON: {gallery_data['num_pages']}")
                            return int(gallery_data['num_pages'])
                except json.JSONDecodeError as e:
                    logging.error(f"Lỗi phân tích JSON: {e}")
                    continue

        logging.error("Không tìm thấy số trang trong HTML hoặc JSON!")
        return None
    except Exception as e:
        logging.error(f"Lỗi khi lấy số trang: {e}")
        return None

def get_image_url(page_url, driver):
    """Lấy URL ảnh từ trang chi tiết bằng Selenium"""
    try:
        driver.get(page_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#image-container, body'))
        )
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        img_container = soup.find('section', id='image-container')
        if img_container:
            img_tag = img_container.find('img')
            if img_tag and img_tag.get('src'):
                return img_tag['src']
        logging.warning(f"Không tìm thấy URL ảnh tại {page_url}")
        return None
    except Exception as e:
        logging.error(f"Lỗi khi lấy URL ảnh từ {page_url}: {e}")
        return None

def download_image(args):
    """Tải một ảnh duy nhất"""
    i, url, folder_name, session = args
    if not url:
        logging.warning(f"Bỏ qua trang {i} do không lấy được URL ảnh")
        return
    try:
        response = session.get(url, headers=HEADERS, stream=True, timeout=20)
        response.raise_for_status()
        file_extension = url.split('.')[-1].split('?')[0]
        file_name = os.path.join(folder_name, f"page_{i:03d}.{file_extension}")
        with open(file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=32768):  # Tăng chunk size lên 32KB
                f.write(chunk)
        logging.info(f"Đã tải {file_name}")
    except requests.RequestException as e:
        logging.error(f"Lỗi khi tải {url}: {e}")

def download_images(image_urls, folder_name):
    """Tải các ảnh bằng đa luồng"""
    start_time = time.time()  # Đo thời gian bắt đầu
    create_directory(folder_name)
    session = requests.Session()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_image, [(i + 1, url, folder_name, session) for i, url in enumerate(image_urls)])
    session.close()
    end_time = time.time()  # Đo thời gian kết thúc
    logging.info(f"Hoàn tất tải tất cả ảnh trong {folder_name}. Thời gian: {end_time - start_time:.2f} giây")

def is_valid_url(url):
    """Kiểm tra URL có đúng định dạng nhxxxai.net không"""
    pattern = r'^https://nhentai\.net/g/\d+/?$'
    if not re.match(pattern, url):
        print("Lỗi: Chỉ hỗ trợ URL từ nhxxxai.net (dạng https://nhxxxai.net/g/<ID>/). Vui lòng thử lại.")
        return False
    return True

def main():
    print("Welcome to Manga Downloader!")
    print("IMPORTANT: This tool only supports downloading from nhxxxai.net (e.g., https://nhxxxai.net/g/123456/).")
    print("Enter a valid nhentai.net URL or press Enter to exit.")

    # Cấu hình Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(f"user-agent={HEADERS['User-Agent']}")

    # Khởi tạo driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        while True:
            print("\nNhập URL truyện (ví dụ: https://nhxxxai.net/g/123456/) hoặc nhấn Enter để thoát:")
            url = input().strip()
            
            if not url:
                print("Đã thoát chương trình.")
                break

            if not is_valid_url(url):
                continue

            if not url.endswith('/'):
                url += '/'

            gallery_id = re.search(r'g/(\d+)/', url).group(1)
            folder_name = f"nhentai_{gallery_id}"
            logging.info(f"Đang xử lý truyện: {url}")

            driver.get("https://nhentai.net")
            # driver.add_cookie({'name': 'sessionid', 'value': 'your_sessionid'})
            # driver.add_cookie({'name': 'csrftoken', 'value': 'your_csrftoken'})

            logging.info("Đang lấy số trang...")
            page_count = get_page_count(url, driver)
            if not page_count:
                logging.error("Không lấy được số trang! Bỏ qua truyện này.")
                continue
            logging.info(f"Bộ truyện có {page_count} trang.")

            image_urls = []
            for page in range(1, page_count + 1):
                page_url = f"{url}{page}/"
                logging.info(f"Đang lấy URL ảnh từ trang {page}...")
                img_url = get_image_url(page_url, driver)
                image_urls.append(img_url)

            if not any(image_urls):
                logging.error("Không lấy được URL ảnh nào! Bỏ qua truyện này.")
                continue
            logging.info(f"Tìm thấy {sum(1 for url in image_urls if url)} ảnh hợp lệ. Bắt đầu tải...")
            download_images(image_urls, folder_name)

    finally:
        driver.quit()
        logging.info("Hoàn tất tất cả truyện!")

if __name__ == "__main__":
    main()