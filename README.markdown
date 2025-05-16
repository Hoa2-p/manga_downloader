# Manga Downloader

A Python tool to download manga images from nhxxxai.net by entering URLs via the console.

**Note**: This tool is designed exclusively for nhxxxai.net and will not work with other websites.

## Features

- Download manga images from nhxxxai.net using Selenium and Requests.
- User-friendly: Input manga URLs directly in the console.
- Automatically creates a folder for each manga based on its ID.
- Supports multiple manga downloads in one session.

## Prerequisites

- **Python 3.7+**: Download from [python.org](https://python.org).
- **Google Chrome**: Required for Selenium. Download from [google.com/chrome](https://www.google.com/chrome).
- **Git** (optional): To clone the repository. Download from [git-scm.com](https://git-scm.com).

## Installation

1. **Clone or download the repository**:

   ```bash
   git clone https://github.com/Hoa2-p/manga_downloader.git
   cd manga_downloader
   ```

   Or download the ZIP from GitHub and extract to a folder.

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   This installs `requests`, `beautifulsoup4`, `selenium`, and `webdriver-manager`.

3. **Verify Chrome**:

   - Ensure Google Chrome is installed and up-to-date.
   - The tool will automatically download the compatible ChromeDriver.

## Usage

1. **Run the tool**:

   ```bash
   python manga_downloader.py
   ```

2. **Enter manga URL**:

   - When prompted, enter the manga URL (e.g., `https://nhxxxai.net/g/123456/`).
   - **Important**: Only URLs from nhxxxai.net are supported (format: `https://nhxxxai.net/g/<ID>/`).
   - Press Enter to download the manga.
   - Enter another URL to download more, or press Enter again to exit.

3. **Check downloaded images**:

   - Images are saved in the `nhxxxai_<ID>` folder (e.g., `nhxxxai_123456`) in the project directory.
   - Files are named `page_001.jpg`, `page_002.jpg`, etc.

## Executable Version (.exe)

For users without Python installed, a standalone executable version is available.

1. **Download the .exe**:
   - Go to the [Releases](https://github.com/Hoa2-p/manga_downloader/releases) page on GitHub.
   - Download the latest `manga_downloader.zip` file.
   - Extract the ZIP to a folder (e.g., `C:\MangaDownloader`).

2. **Run the .exe**:
   - Double-click `manga_downloader.exe`.
   - Follow the console prompts to enter nhxxxai.net URLs (e.g., `https://nhxxxai.net/g/123456/`).
   - Press Enter to download, or press Enter again to exit.

3. **Requirements**:
   - **Google Chrome**: Must be installed and up-to-date.
   - **Windows**: Compatible with Windows 7 or later.
   - **Note**: The .exe is large (~200MB) due to bundled Python and dependencies.

4. **Check downloaded images**:
   - Images are saved in the `nhxxxai_<ID>` folder in the same directory as the .exe.

## Troubleshooting

- **"Không tìm thấy số trang" error**:
  - Check `debug.html` in the project folder to inspect the HTML response.
  - The site may require login. Add cookies in `manga_downloader.py` (for Python version) or contact the developer for .exe version:
    ```python
    driver.add_cookie({'name': 'sessionid', 'value': 'your_sessionid'})
    driver.add_cookie({'name': 'csrftoken', 'value': 'your_csrftoken'})
    ```
    - Get cookies from Chrome (F12 > Application > Cookies) after logging into nhxxxai.net.
  - Try running without headless mode (Python version) by commenting out:
    ```python
    chrome_options.add_argument("--headless")
    ```
- **Download fails**:
  - Ensure a stable internet connection.
  - Use a VPN if the site blocks your IP.
- **Dependencies issues** (Python version):
  - Update dependencies:
    ```bash
    pip install --upgrade -r requirements.txt
    ```

## Contributing

- Fork the repository.
- Create a new branch (`git checkout -b feature/your-feature`).
- Commit changes (`git commit -m "Add your feature"`).
- Push to the branch (`git push origin feature/your-feature`).
- Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

- This tool is for educational purposes only.
- Respect the terms of service of nhxxxai.net and use responsibly.

---

## Hướng dẫn bằng tiếng Việt

# Trình Tải Manga

Một công cụ Python để tải hình ảnh manga từ nhxxxai.net bằng cách nhập URL qua console.

**Lưu ý**: Công cụ này chỉ được thiết kế cho nhxxxai.net và sẽ không hoạt động với các trang web khác.

## Tính năng

- Tải hình ảnh manga từ nhxxxai.net bằng Selenium và Requests.
- Thân thiện với người dùng: Nhập URL manga trực tiếp qua console.
- Tự động tạo thư mục cho mỗi manga dựa trên ID của nó.
- Hỗ trợ tải nhiều manga trong một phiên.

## Yêu cầu

- **Python 3.7+**: Tải từ [python.org](https://python.org).
- **Google Chrome**: Cần cho Selenium. Tải từ [google.com/chrome](https://www.google.com/chrome).
- **Git** (tùy chọn): Để clone repository. Tải từ [git-scm.com](https://git-scm.com).

## Cài đặt

1. **Clone hoặc tải repository**:

   ```bash
   git clone https://github.com/Hoa2-p/manga_downloader.git
   cd manga_downloader
   ```

   Hoặc tải ZIP từ GitHub và giải nén vào một thư mục.

2. **Cài đặt các thư viện phụ thuộc**:

   ```bash
   pip install -r requirements.txt
   ```

   Lệnh này cài đặt `requests`, `beautifulsoup4`, `selenium`, và `webdriver-manager`.

3. **Kiểm tra Chrome**:

   - Đảm bảo Google Chrome đã được cài đặt và cập nhật.
   - Công cụ sẽ tự động tải ChromeDriver tương thích.

## Cách sử dụng

1. **Chạy công cụ**:

   ```bash
   python manga_downloader.py
   ```

2. **Nhập URL manga**:

   - Khi được yêu cầu, nhập URL manga (ví dụ: `https://nhxxxai.net/g/123456/`).
   - **Quan trọng**: Chỉ hỗ trợ URL từ nhxxxai.net (định dạng: `https://nhxxxai.net/g/<ID>/`).
   - Nhấn Enter để tải manga.
   - Nhập URL khác để tải thêm, hoặc nhấn Enter lần nữa để thoát.

3. **Kiểm tra hình ảnh đã tải**:

   - Hình ảnh được lưu trong thư mục `nhxxxai_<ID>` (ví dụ: `nhxxxai_123456`) trong thư mục dự án.
   - Các file được đặt tên là `page_001.jpg`, `page_002.jpg`, v.v.

## Phiên bản thực thi (.exe)

Dành cho người dùng không cài Python, có sẵn phiên bản thực thi độc lập.

1. **Tải .exe**:
   - Truy cập trang [Releases](https://github.com/Hoa2-p/manga_downloader/releases) trên GitHub.
   - Tải file `manga_downloader.zip` mới nhất.
   - Giải nén ZIP vào một thư mục (ví dụ: `C:\MangaDownloader`).

2. **Chạy .exe**:
   - Nhấp đúp vào `manga_downloader.exe`.
   - Làm theo hướng dẫn trên console để nhập URL nhxxxai.net (ví dụ: `https://nhxxxai.net/g/123456/`).
   - Nhấn Enter để tải, hoặc nhấn Enter lần nữa để thoát.

3. **Yêu cầu**:
   - **Google Chrome**: Phải được cài đặt và cập nhật.
   - **Windows**: Tương thích với Windows 7 trở lên.
   - **Lưu ý**: File .exe có kích thước lớn (~200MB) do chứa Python và các thư viện.

4. **Kiểm tra hình ảnh đã tải**:
   - Hình ảnh được lưu trong thư mục `nhxxxai_<ID>` trong cùng thư mục với file .exe.

## Khắc phục sự cố

- **Lỗi "Không tìm thấy số trang"**:
  - Kiểm tra file `debug.html` trong thư mục dự án để xem phản hồi HTML.
  - Trang web có thể yêu cầu đăng nhập. Thêm cookie trong `manga_downloader.py` (cho phiên bản Python) hoặc liên hệ nhà phát triển cho phiên bản .exe:
    ```python
    driver.add_cookie({'name': 'sessionid', 'value': 'your_sessionid'})
    driver.add_cookie({'name': 'csrftoken', 'value': 'your_csrftoken'})
    ```
    - Lấy cookie từ Chrome (F12 > Application > Cookies) sau khi đăng nhập vào nhxxxai.net.
  - Thử chạy không dùng chế độ headless (phiên bản Python) bằng cách bỏ comment:
    ```python
    chrome_options.add_argument("--headless")
    ```
- **Tải thất bại**:
  - Đảm bảo kết nối internet ổn định.
  - Sử dụng VPN nếu trang web chặn IP của bạn.
- **Vấn đề thư viện phụ thuộc** (phiên bản Python):
  - Cập nhật thư viện:
    ```bash
    pip install --upgrade -r requirements.txt
    ```

## Đóng góp

- Fork repository.
- Tạo branch mới (`git checkout -b feature/your-feature`).
- Commit thay đổi (`git commit -m "Add your feature"`).
- Đẩy lên branch (`git push origin feature/your-feature`).
- Mở Pull Request.

## Giấy phép

Dự án này được cấp phép theo Giấy phép MIT. Xem file [LICENSE](LICENSE) để biết chi tiết.

## Tuyên bố miễn trừ trách nhiệm

- Công cụ này chỉ dùng cho mục đích giáo dục.
- Tôn trọng điều khoản dịch vụ của nhxxxai.net và sử dụng một cách có trách nhiệm.
