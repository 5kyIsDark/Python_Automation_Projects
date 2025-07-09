# 🌐 Website Availability Checker

This Python script checks if a list of websites are online or offline by sending HTTP GET requests. It’s a simple and effective tool for quickly testing website availability.

---

## ✅ Features

- Reads a list of URLs from a `.txt` file
- Checks if each website is online (`status code 200`)
- Displays result for each site:
  - ✅ Online
  - ⚠️ Responded with error code
  - ❌ Unreachable or offline
- Fast, clean, and fully automated

---

## 💻 How to Use

1. Install Python (3.6 or later recommended)
2. Install the `requests` library if not already installed:

   ```bash
   pip install requests
   ```

3. Create a text file (e.g. `sites.txt`) and list one URL per line:

   ```
   https://www.google.com
   https://github.com
   https://thissitedoesnotexist.example
   ```

4. Run the script:

   ```bash
   python website_checker.py
   ```

5. When prompted, enter the path to your `.txt` file.

---

## 🧪 Example Output

```
✅ https://www.google.com is Online
✅ https://github.com is Online
❌ https://thissitedoesnotexist.example is Offline or Unreachable
```

---

## 📦 Requirements

- Python 3.x
- `requests` library (`pip install requests`)

---

## 📁 Project Structure

```
website_checker.py
sites.txt
```

---

## 🧠 Tip

You can use this tool for:
- Monitoring your own websites
- Bulk status checks during OSINT
- Troubleshooting network issues

---

## 🛡️ License

This project is open-source and free to use.
