# Selenium-Pytest Automation Framework

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.x-green.svg)
![Pytest](https://img.shields.io/badge/pytest-CI/CD-orange.svg)

## 📌 Project Overview
A robust, data-driven automation framework designed for high-signal UI validation. This project utilizes **Pytest** for test orchestration and **Selenium WebDriver** for cross-browser automation, integrated with **GitHub Actions** for continuous testing.

### Key Features:
* **CI/CD Integration:** Automated smoke tests on every push via GitHub Actions.
* **Data-Driven Testing:** Parametrized test execution using external CSV/JSON data.
* **Deterministic Setup:** Decoupled driver management using `webdriver-manager` for stability.
* **Rich Reporting:** Auto-generated HTML reports with detailed failure logs.

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.10 or higher
* Google Chrome Browser

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone [https://github.com/YOUR_USERNAME/selenium_basics.git](https://github.com/YOUR_USERNAME/selenium_basics.git)
cd selenium_basics
pip install -r requirements.txt