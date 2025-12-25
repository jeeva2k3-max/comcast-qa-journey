# QA Automation Framework (Selenium + Python)

## Overview
This project is a modular, data-driven QA automation framework built using Python and Selenium.
It demonstrates real-world testing concepts such as reusable utilities, assertions, logging,
failure diagnostics, screenshots, and HTML reporting.

## Key Features
- Data-driven test execution
- Custom assertion framework
- Automatic screenshot capture on failures
- HTML test report generation
- Modular utility-based architecture
- Command-line execution

## Tech Stack
- Python 3
- Selenium WebDriver
- ChromeDriver
- HTML reporting

## Project Structure
- `tests/` – Test execution logic
- `utils/` – Browser, assertions, logging, screenshots, reporting
- `data/` – Test input data
- `reports/` – Generated HTML reports
- `screenshots/` – Failure evidence

## How to Run Tests
```bash
cd selenium_basics
python -m tests.test_data_driven
