# 代码生成时间: 2025-11-01 04:15:31
import os
import random
import hashlib
import base64
from typing import Dict, Any

"""
Crypto Wallet - A simple cryptocurrency wallet simulator using Python and NumPy.
This program simulates basic functionalities of a cryptocurrency wallet including
creating a wallet, depositing, withdrawing, and checking balance.
"""

class CryptoWallet:
    """A class to simulate a cryptocurrency wallet."""

    def __init__(self, wallet_id: str):
        """Initialize a new wallet with a unique ID."""
        self.wallet_id = wallet_id
        self.balance = 0.0

    def deposit(self, amount: float) -> bool:
        """Deposit a specified amount to the wallet."""
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return False
        self.balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        """Withdraw a specified amount from the wallet."""
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return False
        if amount > self.balance:
            print("Error: Insufficient funds.")
            return False
        self.balance -= amount
        return True

    def check_balance(self) -> float:
        """Check the current balance of the wallet."""
        return self.balance

    def __repr__(self):
        """Return a string representation of the wallet."""
        return f"CryptoWallet(ID={self.wallet_id}, Balance={self.balance})"


# Example usage:
if __name__ == "__main__":
    # Creating a new wallet
    wallet = CryptoWallet("wallet_123")
    print(wallet)

    # Depositing funds
    success = wallet.deposit(1000)
    if success:
        print("Deposit successful!")
    else:
        print("Deposit failed.")

    # Checking balance
    balance = wallet.check_balance()
    print(f"Current balance: {balance}")

    # Withdrawing funds
    success = wallet.withdraw(500)
    if success:
        print("Withdrawal successful!")
    else:
        print("Withdrawal failed.")

    # Checking balance again
    balance = wallet.check_balance()
    print(f"Current balance after withdrawal: {balance}")