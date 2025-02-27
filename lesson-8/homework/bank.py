import json


class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
        }


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        return account_number

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.to_dict()
        else:
            return "Account not found."

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            self.save_to_file()
            return account.balance
        else:
            return "Account not found."

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount <= account.balance:
                account.balance -= amount
                self.save_to_file()
                return account.balance
            else:
                return "Insufficient funds."
        else:
            return "Account not found."

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            accounts_data = {
                acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()
            }
            json.dump(accounts_data, file)

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                accounts_data = json.load(file)
                for acc_num, acc_data in accounts_data.items():
                    self.accounts[int(acc_num)] = Account(**acc_data)
        except FileNotFoundError:
            pass
