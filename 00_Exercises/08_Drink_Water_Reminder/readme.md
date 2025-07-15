# 💧 Hydration Reminder

A simple Python script that reminds you to drink water at regular intervals to help you stay hydrated and healthy. The reminder uses system notifications and sound alerts to notify the user.

## 📋 Features

- Displays a desktop notification every hour (currently set to every 10 seconds for testing).
- Plays a system sound along with the notification.
- Uses the `plyer` library for cross-platform notification support.
- Uses the `winsound` module (Windows-only) for audio alerts.

## 🔧 Requirements

- Python 3.x
- Windows OS (due to `winsound` dependency)
- Python packages:
  - `plyer`

## 📦 Installation

1. **Clone the repository or download the script:**

   ```bash
   git clone https://github.com/yourusername/hydration-reminder.git
   cd hydration-reminder
