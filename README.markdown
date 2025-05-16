# Manga Downloader

A Python tool to download manga images from nh***ai.net by entering URLs via the console.

## Features

- Download manga images from nh***ai.net using Selenium and Requests.
- User-friendly: Input manga URLs directly in the console.
- Automatically creates a folder for each manga based on its ID.
- Supports multiple manga downloads in one session.

## Prerequisites

- **Python 3.7+**: Download from python.org.
- **Google Chrome**: Required for Selenium. Download from google.com/chrome.
- **Git** (optional): To clone the repository. Download from git-scm.com.

## Installation

1. **Clone or download the repository**:

   ```bash
   git clone https://github.com/<username>/manga_downloader.git
   cd manga_downloader
   ```

   Or download the ZIP from GitHub and extract to a folder.

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   This installs requests, beautifulsoup4, selenium, and webdriver-manager.

3. **Verify Chrome**:

   - Ensure Google Chrome is installed and up-to-date.
   - The tool will automatically download the compatible ChromeDriver.

## Usage

1. **Run the tool**:

   ```bash
   python manga_downloader.py
   ```

2. **Enter manga URL**:

   - When prompted, enter the manga URL (e.g., https://nh****ai.net/g/123456/).
   - Press Enter to download the manga.
   - Enter another URL to download more, or press Enter again to exit.

3. **Check downloaded images**:

   - Images are saved in the nh***ai\_&lt;ID&gt;" folder (e.g., "nh***ai_123456") in the project directory.
   - Files are named page_001.jpg, page_002.jpg, etc.

## Troubleshooting

- **"Không tìm thấy số trang" error**:
  - Check debug.html in the project folder to inspect the HTML response.
  - The site may require login. Add cookies in manga_downloader.py:

    ```python
    driver.add_cookie({'name': 'sessionid', 'value': 'your_sessionid'})
    driver.add_cookie({'name': 'csrftoken', 'value': 'your_csrftoken'})
    ```
    - Get cookies from Chrome (F12 &gt; Application &gt; Cookies) after logging into nhentai.net.
  - Try running without headless mode by commenting out:

    ```python
    chrome_options.add_argument("--headless")
    ```
- **Download fails**:
  - Ensure a stable internet connection.
  - Use a VPN if the site blocks your IP.
- **Dependencies issues**:
  - Update dependencies:

    ```bash
    pip install --upgrade -r requirements.txt
    ```

## Contributing

- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature).
- Commit changes (git commit -m "Add your feature").
- Push to the branch (git push origin feature/your-feature).
- Open a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer

- This tool is for educational purposes only.
- Respect the terms of service of nhentai.net and use responsibly.
