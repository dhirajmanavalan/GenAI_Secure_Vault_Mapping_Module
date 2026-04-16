
---

# 🕵️ Secret Agent Project

## 📌 Overview

The **Secret Agent Project** is designed to securely map command aliases to actual executable commands. It ensures validation, error handling, logging, and automated test reporting integrated with Google Sheets.

This project demonstrates:

* Secure command resolution
* Structured testing using `pytest`
* Automated reporting pipeline to Google Sheets
* Logging and audit tracking

---

## 📁 Project Structure

```
secret-agent-project/
│
├── secret_agent_logic.py      # Core logic for alias-to-command mapping
├── audit.log                 # Logs for errors and audit tracking
│
├── tests/
│   └── test_vault.py         # Pytest test cases
│
├── utils/
│   └── update_sheet.py       # Script to upload test results to Google Sheets
│
├── reports/
│   └── report.json           # Generated pytest JSON report
│
├── requirements.txt          # Project dependencies
├── client_secret.json        # Google OAuth credentials
├── token.pkl                # Stored authentication token
│
└── README.md                # Project documentation
```

---

## ⚙️ Core Functionality

### 🔐 `map_secure_command(alias, mapping_dict)`

**Definition:**
Maps a given alias to its corresponding secure command using a dictionary.

**Handles:**

* `TypeError` → Invalid input types
* `KeyError` → Alias not found
* `ValueError` → Invalid mapping data

**Real-Time Example:**

```python
mapping = {
    "init": "initialize_system",
    "shut": "shutdown_system"
}

map_secure_command("init", mapping)
# Output: "initialize_system"
```

---

## 🧪 Testing Strategy

The project uses **pytest** to validate functionality.

### Test Coverage:

* ✅ Valid alias mapping
* ❌ Invalid alias (`KeyError`)
* ❌ Wrong input types (`TypeError`)
* ❌ Incorrect mapping values (`ValueError`)

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

### Key Libraries:

* `pytest`
* `pytest-json-report`
* `gspread`
* `google-auth-oauthlib`

---

## 🚀 Usage

### 1️⃣ Run Tests & Generate Report

```bash
pytest tests/test_vault.py --json-report --json-report-file=reports/report.json
```

👉 This generates a structured JSON report inside the `reports/` folder.

---

### 2️⃣ Upload Results to Google Sheets

```bash
python utils/update_sheet.py
```

### What Happens:

* Reads `report.json`
* Extracts test summary (pass/fail)
* Updates Google Sheet (`Test_Report`)

---

## 📊 Google Sheets Integration

### Setup Steps:

1. Enable Google Sheets API
2. Download `client_secret.json`
3. Run authentication (generates `token.pkl`)
4. Share your Google Sheet with service account email

---

## 📝 Logging & Audit

All errors and execution logs are stored in:

```
audit.log
```

This ensures traceability and debugging support.

---

## 🔄 End-to-End Flow

```
Alias Input
     ↓
map_secure_command()
     ↓
Validation & Error Handling
     ↓
Pytest Execution
     ↓
JSON Report Generated
     ↓
update_sheet.py
     ↓
Google Sheet Updated
```




---


