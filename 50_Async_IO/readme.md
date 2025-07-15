# Favicon Downloader (Async Wrapper with Requests)

This Python script attempts to download Google's favicon (`favicon.ico`) using asynchronous functions. It saves the favicon into three separate files: `google.ico`, `google2.ico`, and `google3.ico`.

> ⚠️ **Note**: Although the script uses `asyncio`, it does not perform real asynchronous I/O because it uses the `requests` library, which is blocking. See the note below for a better approach.

---

## 🧾 Description

The script defines three asynchronous functions:

- `func1()` downloads and saves `google.ico`
- `func2()` downloads and saves `google2.ico`
- `func3()` downloads and saves `google3.ico`

These functions are executed concurrently using `asyncio.gather()` in the `main()` coroutine.

### 🔧 How it Works

Each function:
1. Sends an HTTP GET request to `http://google.com/favicon.ico`
2. Saves the response content to a different file

The `main()` coroutine gathers all three tasks and prints their results (which are `None`, since the functions don’t return anything).

---

## 📦 Requirements

- Python 3.7+
- `requests` library

Install `requests` with:

```bash
pip install requests
