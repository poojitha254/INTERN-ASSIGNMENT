STEP1:Install Dependencies
--->pip install -r requirements.txt
STEP2:Running the Tests
TASK1:API TESTING
---> pytest api_tests.py -v
TASK2:WEBSITE TESTING
--->pytest tests/ui_tests.py -v

PROJECT STRUCTURE
automation-assignment/
│── tests/
│   ├── api_tests.py   # API test cases
│   ├── ui_tests.py    # UI test cases
│── load_test.py       # Locust load test
│── requirements.txt   # Dependencies
│── README.md          # Instructions


Test Design Choices
-->API Tests → Validated success responses (200), response content (JSON keys/values), and error handling (missing/invalid parameters).

-->UI Tests → Focused on verifying page load, logo presence, heading visibility, and navigation links. Explicit waits (WebDriverWait) used for reliability.

-->Load Test → Simulates small user load (5–10 concurrent users) to stay within Reqres API daily limits (≤100 calls).











