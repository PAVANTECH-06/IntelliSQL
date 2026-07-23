# 🤖 IntelliSQL

> AI-Powered Natural Language to SQL Query Assistant using Google Gemini and Streamlit.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite-green.svg)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange.svg)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## 📌 Overview

IntelliSQL is an AI-powered application that allows users to interact with a database using natural language.

Instead of writing SQL queries manually, users simply ask questions in English. Google Gemini converts the request into an optimized SQLite query, executes it, and displays the results in an interactive format.

The application also explains the generated SQL, provides visualizations, and allows users to download query results as CSV files.

---

## ✨ Features

- 🤖 Natural Language to SQL Conversion
- 🧠 Google Gemini AI Integration
- 🗄️ SQLite Database Support
- 📊 Interactive Data Visualization
- 📥 CSV Export
- 📝 SQL Query Explanation
- 📜 Query History
- 🌙 Dark & Light Theme
- ⚡ Fast and Responsive Streamlit Interface
- 🔒 Read-Only SQL Execution (SELECT Queries Only)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web Interface |
| Google Gemini | AI SQL Generation |
| SQLite | Database |
| Pandas | Data Processing |
| Plotly | Data Visualization |
| Python Dotenv | Environment Variables |

---

## 📂 Project Structure

```
IntelliSQL/
│
├── app.py
├── database.db
├── requirements.txt
├── README.md
├── .gitignore
├── .env
├── assets/
│   └── logo.png
└── .streamlit/
    └── config.toml
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/IntelliSQL.git
```

### 2. Navigate to the project

```bash
cd IntelliSQL
```

### 3. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

Command Prompt

```bash
venv\Scripts\activate
```

PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Configure Gemini API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your API key from:

https://aistudio.google.com/app/apikey

---

### 6. Run the Application

```bash
python -m streamlit run app.py
```

Open your browser:

```
http://localhost:8501
```

---

## 💬 Example Queries

Try asking:

- Show all customers
- List all orders
- Show customers from Hyderabad
- Display total sales by product
- Find customers who ordered Laptop
- Show orders greater than 5000
- Display customer names and cities

---

## 📊 Workflow

```
User Question
      │
      ▼
Google Gemini
      │
Natural Language → SQL
      │
      ▼
SQLite Database
      │
      ▼
Execute Query
      │
      ▼
Results + Charts + SQL Explanation
```

---

## 📸 Screenshots

Add screenshots here after deployment.

Example:

```
screenshots/
│
├── home.png
├── query.png
├── chart.png
└── about.png
```

---

## 🔒 Security

- Only SELECT queries are executed.
- UPDATE, DELETE, INSERT, DROP, and ALTER commands are blocked.
- API keys are stored securely using `.env`.
- Sensitive files are excluded using `.gitignore`.

---

## 📈 Future Enhancements

- PostgreSQL Support
- MySQL Support
- SQL Optimization Suggestions
- Voice Input
- User Authentication
- Saved Queries
- Dashboard Analytics
- AI Chat Mode
- Export to PDF
- Multi-Database Support

---

## 👨‍💻 Author

**P. V. Durga Malleswara Rao**

- 🎓 B.Tech – Computer Science & Engineering
- 💻 Software Engineer & AI Enthusiast
- ☁️ AWS Certified Cloud Practitioner

### GitHub

https://github.com/PAVANTECH-06

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and contribute.
