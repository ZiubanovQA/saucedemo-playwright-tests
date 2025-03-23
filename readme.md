# 🧪 Autotests for SauceDemo Web App

UI automation project using **Playwright** and **Pytest** to test core functionality of the [SauceDemo](https://www.saucedemo.com/) web app.

---

## 🚀 Stack

- ✅ Python 3.13
- ✅ Playwright
- ✅ Pytest
- ✅ GitHub Actions (CI)
- ✅ Smoke + Regression test coverage

---

## 📂 Project Structure

```
saucedemo/
├── conftest.py
├── requirements.txt
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
```

## 💻 How to run tests locally

```bash
pip install -r requirements.txt
pytest tests/ -v -s

## 📸 Screenshots

Some tests save screenshots after key actions —  
for example: order success or failed login attempts.

These screenshots are useful for:
- ✅ Visual verification
- ✅ Debugging failed tests
- ✅ CI test artifacts (optional)

---

## 👨‍💻 Author

**Ivan (ZiubanovQA)** — QA Engineer  
GitHub: [@ZiubanovQA](https://github.com/ZiubanovQA)
