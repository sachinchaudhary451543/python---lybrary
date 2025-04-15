from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "securekey"

# Load accounts from JSON
ACCOUNTS_FILE = "accounts.json"
def load_accounts():
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save accounts to JSON
def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as file:
        json.dump(accounts, file, indent=4)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Create Account
@app.route("/register", methods=["GET", "POST"])
def register():
    accounts = load_accounts()
    if request.method == "POST":
        acc_no = request.form["account_number"]
        name = request.form["name"]
        balance = int(request.form["balance"])

        if acc_no in accounts:
            flash("❌ Account already exists! Try logging in.", "danger")
            return redirect(url_for("register"))

        if balance < 10000:
            flash("❌ Minimum balance ₹10,000 required!", "danger")
            return redirect(url_for("register"))

        accounts[acc_no] = {
            "name": name,
            "balance": balance,
            "transactions": []
        }
        save_accounts(accounts)
        flash("✅ Account created successfully!", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    accounts = load_accounts()
    if request.method == "POST":
        acc_no = request.form["account_number"]
        if acc_no in accounts:
            session["account_number"] = acc_no
            return redirect(url_for("dashboard"))
        else:
            flash("❌ Account not found!", "danger")

    return render_template("login.html")

# Dashboard
@app.route("/dashboard")
def dashboard():
    if "account_number" not in session:
        return redirect(url_for("login"))

    accounts = load_accounts()
    acc_no = session["account_number"]
    account = accounts[acc_no]
    
    return render_template("dashboard.html", account=account, acc_no=acc_no)

# Debit Money
@app.route("/debit", methods=["POST"])
def debit():
    if "account_number" not in session:
        return redirect(url_for("login"))

    acc_no = session["account_number"]
    accounts = load_accounts()
    amount = int(request.form["amount"])

    if amount > accounts[acc_no]["balance"]:
        flash("❌ Insufficient balance!", "danger")
    else:
        accounts[acc_no]["balance"] -= amount
        transaction = f"Debited ₹{amount} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        accounts[acc_no]["transactions"].append(transaction)
        save_accounts(accounts)
        flash(f"✅ ₹{amount} debited successfully!", "success")

    return redirect(url_for("dashboard"))

# Credit Money
@app.route("/credit", methods=["POST"])
def credit():
    if "account_number" not in session:
        return redirect(url_for("login"))

    acc_no = session["account_number"]
    accounts = load_accounts()
    amount = int(request.form["amount"])

    accounts[acc_no]["balance"] += amount
    transaction = f"Credited ₹{amount} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    accounts[acc_no]["transactions"].append(transaction)
    save_accounts(accounts)
    flash(f"✅ ₹{amount} credited successfully!", "success")

    return redirect(url_for("dashboard"))

# Logout
@app.route("/logout")
def logout():
    session.pop("account_number", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
