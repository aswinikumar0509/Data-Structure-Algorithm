# Design a Python class BankAccount that models a simple bank account with the following features:

# Attributes: account_number, account_holder, and balance (default 0)

# Methods:

# deposit(amount) — increases balance

# withdraw(amount) — decreases balance if sufficient funds

# get_balance() — returns current balance
# create a FastAPI endpoint to interact with the above class.

# Task:
# Implement a simple REST API that:

# Allows creating a new BankAccount

# Allows depositing, withdrawing, and checking the balance

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage (for demo only)
accounts: dict[str, "BankAccount"] = {}


class BankAccount:
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance


class CreateAccountRequest(BaseModel):
    account_number: str
    account_holder: str


class AmountRequest(BaseModel):
    amount: float


@app.post("/accounts")
def create_account(req: CreateAccountRequest):
    if req.account_number in accounts:
        raise HTTPException(status_code=400, detail="Account already exists")
    accounts[req.account_number] = BankAccount(req.account_number, req.account_holder)
    return {"message": "Account created", "account_number": req.account_number}


@app.post("/accounts/{account_number}/deposit")
def deposit(account_number: str, req: AmountRequest):
    acc = accounts.get(account_number)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    try:
        acc.deposit(req.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"account_number": account_number, "balance": acc.get_balance()}


@app.post("/accounts/{account_number}/withdraw")
def withdraw(account_number: str, req: AmountRequest):
    acc = accounts.get(account_number)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    try:
        acc.withdraw(req.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"account_number": account_number, "balance": acc.get_balance()}


@app.get("/accounts/{account_number}/balance")
def balance(account_number: str):
    acc = accounts.get(account_number)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"account_number": account_number, "balance": acc.get_balance()}
