# 🏋️ Gym & Fitness Center Management System

A comprehensive desktop application for managing gym operations, including member management, trainer management, attendance tracking, and payment processing.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Database Schema](#database-schema)
- [Module Documentation](#module-documentation)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Member Management
- Add new members with personal information
- Manage member profiles (name, age, gender, contact details, email)
- Assign membership plans (Monthly, Quarterly, Yearly)
- Track join dates and membership expiry dates
- Search and retrieve member information
- Update member details
- Delete member records

### Trainer Management
- Add and manage trainers
- Track trainer specialties (strength training, cardio, yoga, etc.)
- Maintain trainer contact information
- View all trainers in the system

### Attendance Tracking
- Mark member attendance with automatic timestamps
- Record attendance date and time
- View attendance history for each member
- Track member gym visits

### Payment Management
- Record member payments
- Support multiple payment methods (Cash, Card, UPI)
- Track payment amounts and dates
- Maintain payment history
- Add payment notes for reference

### Membership Plans
- Pre-configured plans: Monthly, Quarterly, Yearly
- Automatic expiry date calculation based on plan duration
- Flexible plan pricing

## 🏗️ Project Structure

```
gym_management_system/
├── gui.py                 # Main GUI application using CustomTkinter
├── models.py              # Database operations and business logic
├── database.py            # Database initialization and connection
├── gym.db                 # SQLite database file (created at runtime)
└── README.md              # This file
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

#### 📋 Members Tab
1. **Add Member**: Fill in the form with member details and click "➕ Add Member"
   - Name (required)
   - Age
   - Phone
   - Email
   - Membership Plan (dropdown)
   - Join Date (auto-filled with today's date)

2. **Show Members**: Click "📋 Show Members" to view all members in the system

#### 🏋 Trainers Tab
1. **Add Trainer**: Enter trainer information
   - Name
   - Specialty (e.g., Strength Training, Yoga, Cardio)
   - Phone

2. **Show Trainers**: Click "📋 Show Trainers" to view all trainers

#### 📆 Attendance Tab
1. **Mark Attendance**: Enter member ID and click "✔ Mark Now" to record attendance
   - Automatically records date and time
   - Requires valid member ID

2. **Show Records**: View attendance history for a specific member

#### 💳 Payments Tab
1. **Add Payment**: Record a payment transaction
   - Member ID
   - Amount
   - Payment Method (Cash, Card, or UPI)

2. **Show Payments**: View payment history for a member

### Navigation
- Use the sidebar buttons to switch between different sections
- Click "Exit" button to close the application

## 📸 Screenshots

### Main Landing Page
[Add your main application landing page screenshot here]

![Main Screen](/ss.png)



## 🎨 UI Features

- **Dark Theme**: Modern dark blue interface for comfortable viewing
- **Responsive Layout**: Sidebar navigation with main content area
- **Input Validation**: Error handling for invalid entries
- **Emoji Icons**: Intuitive visual indicators for different sections
- **Message Boxes**: User-friendly notifications for success and errors
- **Combo Boxes**: Dropdown selections for membership plans and payment methods

## ⚙️ Default Membership Plans

The system comes with three pre-configured membership plans:

| Plan Name | Duration | Price  |
|-----------|----------|--------|
| Monthly   | 1 month  | ₹1000  |
| Quarterly | 3 months | ₹2500  |
| Yearly    | 12 months| ₹8000  |

## 🐛 Error Handling

The application includes error handling for:
- Invalid member IDs
- Missing required fields
- Invalid date formats
- Database connection issues
- Invalid input types (age, amount must be numeric)

## 🔒 Data Persistence

All data is automatically saved to the SQLite database (`gym.db`). The database is created in the same directory as the application on first run.

## 🚀 Future Enhancements

Potential features for future versions:
- Export reports (PDF, Excel)
- Membership renewal reminders
- Monthly billing automation
- Performance analytics and charts
- Member search and filtering
- Trainer assignment to members
- Package management system
- User authentication and roles
- Backup and restore functionality
- Email notifications

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for bugs and feature requests.

## 📄 License

This project is open source and available under the MIT License.

---

**Author**: Ankit Kumar  

