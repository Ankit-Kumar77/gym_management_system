# 🏋️ Gym & Fitness Center Management System

A comprehensive desktop application for managing gym operations, including member management, trainer management, attendance tracking, and payment processing.

## 📸 Screenshot

### Main Landing Page
![Main Screen](/ss.png)

## ✨ Features

- **Member Management** - Add, update, and manage member profiles with membership plans
- **Trainer Management** - Register and manage trainers with their specialties
- **Attendance Tracking** - Record and view member gym visit history with timestamps
- **Payment Management** - Process and track member payments with multiple payment methods
- **Membership Plans** - Pre-configured plans (Monthly, Quarterly, Yearly) with auto-expiry calculation
- **Modern UI** - Dark theme interface with intuitive navigation and emoji-based visual indicators
- **Database Persistence** - All data automatically saved to SQLite database

## 🏗️ Project Structure

```
gym_management_system/
├── gui.py              # Main GUI application
├── models.py           # Business logic and data operations
├── database.py         # Database initialization and connection
├── gym.db              # SQLite database (created at runtime)
└── README.md           # Documentation
```

## 📦 Requirements

- Python 3.7+
- customtkinter >= 5.0
- sqlite3 (included with Python)

## 🚀 Installation

### Step 1: Clone or Download the Project
```bash
git clone <repository-url>
cd gym_management_system
```

### Step 2: Install Dependencies
```bash
pip install customtkinter
```

### Step 3: Run the Application
```bash
python gui.py
```

The application will automatically create the `gym.db` database file and initialize tables on first run.

## 💻 Usage

### Starting the Application
```bash
python gui.py
```

### Main Menu
The application provides a sidebar menu with the following options:

**📋 Members Tab** - Add member details and view all members  
**🏋 Trainers Tab** - Add trainers with specialties and contact info  
**📆 Attendance Tab** - Mark and view member attendance records  
**💳 Payments Tab** - Record and track member payments

## ⚙️ Default Membership Plans

| Plan Name | Duration | Price  |
|-----------|----------|--------|
| Monthly   | 1 month  | ₹1000  |
| Quarterly | 3 months | ₹2500  |
| Yearly    | 12 months| ₹8000  |

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for bugs and feature requests.

## 📄 License

This project is open source and available under the MIT License.

---

**Author**: Ankit Kumar  

