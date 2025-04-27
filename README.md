# 💸 Expense Tracker App

A simple and beginner-friendly Python app to **track your expenses**, built with **CSV** for persistent storage and **Colorama** for a colorful CLI experience.

---

## 🚀 Features

- Add new expenses (with Date, Description, and Amount)
- View all stored expenses neatly in a table format
- Delete a specific expense by index
- Calculate the total of all expenses
- Clear all expenses at once
- Data is saved and loaded from a CSV file (`expenses.csv`)

---

## 🛠 Requirements

- Python 3.6+
- Colorama library

Install Colorama if you don't have it:
```bash
pip install colorama
```

---

## 📋 How to Use

1. Run the script:
```bash
python Expense Tracker.py
```

2. Choose an option from the menu:
    - `1` ➔ Add a new expense
    - `2` ➔ View all expenses
    - `3` ➔ Delete an expense
    - `4` ➔ View total expenses
    - `5` ➔ Clear all expenses
    - `6` ➔ Exit the app

3. Your data is saved automatically in a file named `expenses.csv`.

---

## 📂 File Structure

```
Expense Tracker/
│
├── expenses.csv       # CSV file where all expenses are stored
├── expense_tracker.py # Main Python script
└── README.md          # (This file)
```

---

## 🌟 Future Improvements (Ideas)

- Add an "Edit" expense option
- Validate real calendar dates (e.g., prevent Feb 30th)
- Monthly/yearly expense summaries
- Graphs and charts using `matplotlib`
- Export to Excel (`.xlsx`) format

---

## 🙌 Acknowledgment

Made with ❤️ using Python and Colorama.

---

