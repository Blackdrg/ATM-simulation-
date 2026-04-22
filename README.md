# ATM Simulation

## Overview
Advanced Python-based ATM simulation system with two implementations:

### main.py (Basic ATM)
- Simple console-based ATM.
- Features: Balance display, deposit, withdraw, transaction history.
- No persistence or authentication.

### modified.py (Advanced ATM)
- Full-featured ATM with **user authentication**, **data persistence (JSON)**, **daily withdrawal limits (₹20,000)**.
- **Key Features**:
  - User accounts (ID + PIN)
  - Persistent balance & transactions across sessions (`atm_data.json`)
  - Timestamped transaction history
  - Daily withdrawal tracking & limits
  - Create new user accounts

## Quick Start
1. **Activate virtual environment**:
   ```
   .venv\Scripts\activate
   ```
2. **Run Basic ATM**:
   ```
   python main.py
   ```
3. **Run Advanced ATM**:
   ```
   python modified.py
   ```
   - First run: Create account (User ID + PIN)
   - Login with credentials
   - Use menu: Deposit/Withdraw/Balance/Transactions/Logout

## Features Breakdown

| Feature | main.py | modified.py |
|---------|---------|-------------|
| Authentication | ❌ | ✅ (PIN) |
| Persistence | ❌ | ✅ (JSON) |
| Daily Limit | ❌ | ✅ (₹20k) |
| Transaction History | ✅ (In-memory) | ✅ (Persistent, timestamped) |
| Multi-User | ❌ | ✅ |

## File Structure
```
ATM/
├── .venv/              # Python virtual environment (gitignored)
├── main.py             # Basic ATM
├── modified.py         # Advanced ATM
├── atm_data.json       # User data (created on first use, gitignored)
├── README.md           # This file
├── .gitignore          # Ignores venv, pyc, data
└── TODO.md             # Git setup log
```

## Usage Examples (Advanced)
```
# Create user: ID=123 PIN=0000
# Login: 123 / 0000
# Deposit ₹1000 → Balance: ₹1000
# Withdraw ₹500 → Balance: ₹500
# History shows timestamped txns
# Daily limit prevents >₹20k/day withdrawal
```

## Tech Stack
- **Python 3.x**
- **JSON** for persistence
- **datetime** for timestamps

## GitHub
Synced to: https://github.com/Blackdrg/ATM-simulation-.git

**Run locally or contribute!** 🚀
