# EDU-SAFE

## Overview

EDU-SAFE is a user-friendly website blocker application designed to help manage online activities by restricting access to specific websites or categories of websites. It is ideal for personal productivity, parental control, and maintaining a focused work environment. The application operates by blocking access to specified URLs, ensuring a safe and productive browsing experience.

## Features

- **URL Blocking:** Restrict access to specific websites by blocking their URLs.
- **Content Filtering:** Prevent access to websites based on predefined categories.
- **Access Scheduling:** Set schedules for when specific websites can be accessed.
- **Whitelist and Blacklist:** Customize your browsing experience by allowing or blocking specific websites.
- **Usage Reports:** Monitor and review browsing patterns through detailed usage reports.

## Installation and Setup

### Prerequisites

- Python 3.12.0
- Tkinter
- PIL (Python Imaging Library)

### Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/EDU-SAFE.git
    cd EDU-SAFE
    ```

2. **Install the Required Libraries:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Run the Application:**
    ```bash
    python main.py
    ```

2. **Login Screen:**
    - Enter your username, email, and password.
    - Click the "Login" button to proceed to the website blocker interface.

3. **Website Blocker Interface:**
    - **Enter Websites:** Type the websites you want to block or unblock, separated by commas.
    - **Block Button:** Click to block the entered websites.
    - **Unblock Button:** Click to unblock the entered websites.
    - **Show Blocked Websites:** Click to display a list of currently blocked websites.

### Platform-Specific Paths

The application automatically detects the operating system and sets the path to the `hosts` file accordingly:

- **Windows:** `C:\Windows\System32\drivers\etc\hosts`
- **macOS:** `/private/etc/hosts`
- **Linux:** `/etc/hosts`

## Code Structure

- **`main.py`:** Entry point for the application. Contains the main logic for the login window and website blocker interface.
- **`user_details/`:** Directory where user details are saved.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## Acknowledgements

- Tkinter for GUI
- PIL for image processing

## Contact

For any inquiries or issues, please contact [my email](mailto:djeevanmourya@gmail.com).
