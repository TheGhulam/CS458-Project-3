# CS458 Project 3

## Introduction
This repository contains a Next.js project that is hosted on Vercel at [cs458.gahmed.com](https://cs458.gahmed.com) or run locally. It also includes Selenium tests located in the `tests` directory.

Test User Credentials:
- Username: `test@gmail.com`
- Password: `1`

## Getting Started

### Prerequisites
Ensure you have `npm` installed on your system to run the project and manage dependencies.

### Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Install the dependencies:
   ```bash
    npm install
    ```

### Running the Project
To run the project locally, execute the following command:
```bash
npm run dev
```
This will start the Next.js development server. By default, the app will be available at http://localhost:3000.

## Testing
The Selenium tests for this project are located in the `tests` directory. These tests are designed to run against the Vercel hosted app but can be modified to run locally.

### WebDriver Setup
Before running the Selenium tests, you need to set up the appropriate WebDriver for your browser.

1. Download the WebDriver for your preferred browser:

- Chrome: ChromeDriver
- Firefox: GeckoDriver
- Safari: SafariDriver
- Edge: EdgeDriver

2. Add the path to the WebDriver executable to your system's PATH environment variable.

### Running the Tests

To run the tests:

1. Navigate to the tests directory:
    ```bash
    cd tests
    ```

2. Execute the test scripts using Python:
    ```bash
    python <test-script-name>.py
    ```

### Modifying Test Configuration
If you are running the app locally and wish to run the Selenium tests against it, replace the URL in the test scripts from `cs458.gahmed.com` to your local server's URL, typically `http://localhost:3000`

Additionally, make sure to update the WebDriver initialization in the test scripts to match your browser and WebDriver setup. For example, if using Chrome:
```python
driver = webdriver.Chrome()
```