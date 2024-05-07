# CS458 Project 3

## Introduction
This repository contains a Next.js project that is hosted on Vercel at [cs458.gahmed.app](https://cs458.gahmed.app) or run locally. It also includes Selenium tests located in the `tests` directory.

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

## Running the Tests
The Selenium tests for this project are located in the `tests` directory. These tests are designed to run against the Vercel hosted app but can be modified to run locally.

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
If you are running the app locally and wish to run the Selenium tests against it, replace the URL in the test scripts from `cs458.gahmed.app` to your local server's URL, typically `http://localhost:3000`
