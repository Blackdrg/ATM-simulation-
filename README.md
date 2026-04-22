# 🚀 Fully Functional ATM Prototype

## Overview
**Production-ready console ATM simulator** with advanced features, colorful UI, persistence, and security.

**Key Features**:
- ✅ User authentication (4-digit PIN)
- ✅ Persistent data (JSON - `atm_data.json`)
- ✅ Daily withdrawal limit (₹20,000)
- ✅ Transaction history (timestamped)
- ✅ Multi-user support
- ✅ **NEW**: PIN change, user-to-user transfer
- ✅ Input validation & error handling
- ✅ Colorful console UI (colorama)
- ✅ Tests (pytest)

| Feature | Status |
|---------|--------|
| Auth/Persistence | ✅ Full |
| Limits/History | ✅ Full |
| Transfer/PIN Change | ✅ New |
| Tests/UI | ✅ Added |

## Quick Start
1. **Setup venv & deps**:
   ```
   .venv\Scripts\activate
   pip install -r requirements.txt  # colorama, pytest
   ```
2. **Run Prototype**:
   ```
   python modified.py
   ```
3. **Test**:
   ```
   pytest tests/
   ```

## Usage
```
🚀 Advanced ATM Prototype
=== MAIN MENU ===
1. Login     2. Create Account    3. Exit

[Create: ID=123 PIN=0000]
[Login → User MENU: Balance preview, Deposit/Withdraw/Transfer/PIN/History/Logout]
Daily limit enforced, data persists!
```

## File Structure
```
ATM/
├── modified.py         # Main prototype (use this!)
├── main.py            # Legacy basic (optional)
├── requirements.txt   # colorama pytest
├── run.py            # Launcher
├── tests/            # Unit tests
├── atm_data.json     # Data (auto-created)
├── README.md
└── .gitignore
```

## Tech Stack
- Python 3.x
- colorama (UI)
- JSON/datetime (data)
- pytest (tests)

## Next Steps (Optional)
- GUI (Tkinter/PyQt)
- SQLite DB
- GitHub PR

**Prototype complete! Run & contribute 🚀**
https://github.com/Blackdrg/ATM-simulation-.git
