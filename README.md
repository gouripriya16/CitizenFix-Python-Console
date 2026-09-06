# CitizenFix – Console / Terminal CLI Application 🏙️💻

**CitizenFix** is an interactive **Console / Terminal Application** built in Python with a **SQLite Database** (`database.py` & `citizenfix.db`).

---

## 🚀 How to Run in Console / Terminal

Open your PowerShell or Command Prompt terminal inside the project directory and run:

```powershell
python main.py
# OR
python run.py
# OR using virtual environment
.venv\Scripts\python.exe main.py
```

---

## 🎮 Interactive Console Menu

When you run the application in your console, you get an interactive menu:

```
=================================================================
 🏙️  CitizenFix – Civic Issue Intelligence System (Console CLI)
=================================================================
1. 👤 Citizen Portal (Report Issue / View Complaints)
2. 🛡️ Municipal Officer Gateway (Login / Manage Tickets)
3. 📊 View Analytics Summary
4. 🚪 Exit
```

### 👤 1. Citizen Portal
- **Report Issue**: Choose issue category (Pothole, Water Leak, Streetlight, Garbage), enter location, and write issue description.
- **View Complaints**: View all reported tickets formatted cleanly in console cards with status icons.

### 🛡️ 2. Municipal Officer Gateway
- **Login**: Authenticate with Officer Credentials (`officer@city.gov` / `Officer@123`).
- **Ticket Management**:
  - Filter complaints by status (**All**, **Pending**, **In Progress**, **Resolved**).
  - Update ticket status (Pending ➔ In Progress ➔ Resolved) and attach officer resolution notes.

### 📊 3. Analytics Summary
- Displays live metric counts (Total Logged, Pending, In Progress, Resolved).

---

## 📁 Project Structure

```
Civic Issue Intelligence/
├── main.py       # Main Console CLI Application (Interactive Terminal Loop)
├── database.py   # SQLite Database Manager (Tables: users, complaints)
├── run.py        # Launcher script
├── README.md     # Project Documentation
└── citizenfix.db # Persistent SQLite Database File
```
