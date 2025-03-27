# 🧪 Autotests & Load Testing for SauceDemo Web App

Automated testing project using **Playwright** for UI tests and **K6** for load testing.  
Includes CI integration with **GitHub Actions** and cloud metrics via **Grafana**.

---

## 🧰 Stack

- ✅ Python 3.13
- ✅ Playwright + Pytest
- ✅ K6 (Load testing)
- ✅ GitHub Actions (CI)
- ✅ Grafana Cloud (Metrics)
- ✅ Smoke + Regression test coverage

---

## 📁 Project Structure

```
saucedemo/
├── .github/workflows/
│   ├── playwright-tests.yml         # CI for UI tests
│   └── k6-load-test.yml             # CI for load testing
├── load_tests_k6/
│   └── login_load_test.js           # K6 scenario for login page
├── pages/                           # Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   └── cart_page.py
├── tests/
│   ├── cart/
│   │   ├── test_add_to_cart.py
│   │   └── test_remove_from_cart.py
│   ├── login_form/
│   │   ├── test_login_with_valid_data.py
│   │   └── test_login_with_invalid_data.py
│   └── order/
│       ├── test_order_with_valid_data.py
│       └── test_order_with_empty_first_name.py
├── test_result_screenshots/         # Screenshots for verification
├── config.py
├── conftest.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to run tests locally

```bash
pip install -r requirements.txt
pytest tests/ -v -s
```

---

## 📸 Screenshots

Some tests save screenshots after key actions —  
for example: order success or failed login attempts.

These screenshots are useful for:

- ✅ Visual verification
- ✅ Debugging failed tests
- ✅ CI test artifacts (optional)

---

## ☁️ Load Testing with K6 + Grafana

Load tests are written using **K6**, executed through **GitHub Actions**,  
and results are automatically uploaded to **Grafana Cloud**.

No local setup required for metrics — just push, and observe the metrics.

---

## 👨‍💻 Author

**Ivan (ZiubanovQA)** — QA Engineer  
GitHub: [@ZiubanovQA](https://github.com/ZiubanovQA)
