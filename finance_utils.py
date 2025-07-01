import json

def get_budget_advice(income, expense):
    if income == 0:
        return "Income must be greater than 0."
    saving = income - expense
    if saving > 0:
        return f"You're saving ₹{saving} per month. Consider investing in mutual funds or FDs."
    else:
        return "You're overspending. Try reducing lifestyle costs or increasing income sources."

def load_glossary():
    with open("glossary.json", "r") as f:
        return json.load(f)
