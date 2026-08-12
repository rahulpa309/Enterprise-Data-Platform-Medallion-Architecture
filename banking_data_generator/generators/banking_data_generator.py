from pathlib import Path
from datetime import datetime, timedelta
import random
import uuid

import pandas as pd
from faker import Faker


class BankingDataGenerator:

    def __init__(self, output_directory="../output", seed=12345):
        self.fake = Faker("en_IN")
        self.fake.seed_instance(seed)
        random.seed(seed)

        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)

        self.branches = []
        self.employees = []
        self.customers = []
        self.accounts = []
        self.loans = []
        self.credit_cards = []
        self.beneficiaries = []
        self.transactions = []

    # ---------------------------------------------------------
    # Branches
    # ---------------------------------------------------------
    def generate_branches(self, count=25):

        for i in range(1, count + 1):
            self.branches.append({
                "branch_id": f"BR{i:04d}",
                "branch_name": f"Branch_{i:03d}",
                "city": self.fake.city(),
                "state": self.fake.state(),
                "ifsc_code": f"EBPB0{i:05d}",
                "branch_type": random.choice(
                    ["Urban", "Semi-Urban", "Rural"]
                ),
                "created_date": "2026-01-01"
            })

    # ---------------------------------------------------------
    # Employees
    # ---------------------------------------------------------
    def generate_employees(self, count=500):

        for i in range(1, count + 1):

            branch = random.choice(self.branches)

            self.employees.append({
                "employee_id": f"EMP{i:05d}",
                "employee_name": self.fake.name(),
                "branch_id": branch["branch_id"],
                "designation": random.choice([
                    "Manager",
                    "Assistant Manager",
                    "Officer",
                    "Clerk"
                ]),
                "joining_date": self.fake.date_between(
                    start_date="-10y",
                    end_date="-1y"
                ),
                "email": self.fake.email(),
                "phone": self.fake.phone_number()
            })

    # ---------------------------------------------------------
    # Customers
    # ---------------------------------------------------------
    def generate_customers(self, count=10000):

        for i in range(1, count + 1):

            dob = self.fake.date_of_birth(
                minimum_age=18,
                maximum_age=75
            )

            branch = random.choice(self.branches)

            self.customers.append({
                "customer_id": f"CUST{i:07d}",
                "customer_name": self.fake.name(),
                "date_of_birth": dob,
                "gender": random.choice(
                    ["Male", "Female", "Other"]
                ),
                "email": self.fake.email(),
                "phone": self.fake.phone_number(),
                "pan_number": f"{self.fake.random_uppercase_letter()}"
                             f"{self.fake.random_uppercase_letter()}"
                             f"{self.fake.random_number(digits=5)}"
                             f"{self.fake.random_uppercase_letter()}",
                "aadhaar_number": self.fake.numerify(
                    "############"
                ),
                "branch_id": branch["branch_id"],
                "customer_status": random.choice(
                    ["Active", "Active", "Active", "Inactive"]
                ),
                "created_date": self.fake.date_between(
                    start_date="-5y",
                    end_date="today"
                )
            })

    # ---------------------------------------------------------
    # Accounts
    # ---------------------------------------------------------
    def generate_accounts(self):

        account_id = 1

        for customer in self.customers:

            number_of_accounts = random.randint(1, 3)

            for _ in range(number_of_accounts):

                account_type = random.choices(
                    ["Savings", "Current", "Salary"],
                    weights=[70, 20, 10]
                )[0]

                self.accounts.append({
                    "account_id": f"ACC{account_id:09d}",
                    "customer_id": customer["customer_id"],
                    "branch_id": customer["branch_id"],
                    "account_type": account_type,
                    "account_number": str(
                        random.randint(10**10, 10**11 - 1)
                    ),
                    "opening_date": self.fake.date_between(
                        start_date="-5y",
                        end_date="today"
                    ),
                    "balance": round(
                        random.uniform(1000, 500000), 2
                    ),
                    "interest_rate": round(
                        random.uniform(2.5, 7.5), 2
                    ),
                    "currency": "INR",
                    "account_status": random.choice(
                        ["Active", "Active", "Active", "Dormant"]
                    )
                })

                account_id += 1

    # ---------------------------------------------------------
    # Loans
    # ---------------------------------------------------------
    def generate_loans(self):

        loan_id = 1

        eligible_customers = random.sample(
            self.customers,
            int(len(self.customers) * 0.25)
        )

        for customer in eligible_customers:

            loan_type = random.choices(
                ["Home", "Personal", "Vehicle"],
                weights=[40, 35, 25]
            )[0]

            self.loans.append({
                "loan_id": f"LOAN{loan_id:07d}",
                "customer_id": customer["customer_id"],
                "loan_type": loan_type,
                "loan_amount": random.randint(
                    100000, 5000000
                ),
                "interest_rate": round(
                    random.uniform(7, 14), 2
                ),
                "tenure_months": random.choice(
                    [12, 24, 36, 60, 120]
                ),
                "loan_status": random.choice(
                    ["Active", "Active", "Closed"]
                ),
                "loan_start_date": self.fake.date_between(
                    start_date="-5y",
                    end_date="today"
                )
            })

            loan_id += 1

    # ---------------------------------------------------------
    # Credit Cards
    # ---------------------------------------------------------
    def generate_credit_cards(self):

        card_id = 1

        eligible_customers = random.sample(
            self.customers,
            int(len(self.customers) * 0.35)
        )

        for customer in eligible_customers:

            self.credit_cards.append({
                "credit_card_id": f"CC{card_id:08d}",
                "customer_id": customer["customer_id"],
                "card_type": random.choice(
                    ["Classic", "Gold", "Platinum"]
                ),
                "credit_limit": random.choice(
                    [50000, 100000, 200000, 500000]
                ),
                "card_status": random.choice(
                    ["Active", "Active", "Blocked"]
                ),
                "issue_date": self.fake.date_between(
                    start_date="-4y",
                    end_date="today"
                )
            })

            card_id += 1

    # ---------------------------------------------------------
    # Beneficiaries
    # ---------------------------------------------------------
    def generate_beneficiaries(self):

        beneficiary_id = 1

        for account in self.accounts:

            number_of_beneficiaries = random.randint(1, 3)

            for _ in range(number_of_beneficiaries):

                self.beneficiaries.append({
                    "beneficiary_id": f"BEN{beneficiary_id:08d}",
                    "account_id": account["account_id"],
                    "beneficiary_name": self.fake.name(),
                    "beneficiary_account_number": str(
                        random.randint(10**10, 10**11 - 1)
                    ),
                    "ifsc_code": f"EBPB0{random.randint(1, 99999):05d}",
                    "relationship": random.choice([
                        "Self",
                        "Spouse",
                        "Parent",
                        "Sibling",
                        "Friend"
                    ]),
                    "created_date": self.fake.date_between(
                        start_date="-3y",
                        end_date="today"
                    )
                })

                beneficiary_id += 1

    # ---------------------------------------------------------
    # Transactions
    # ---------------------------------------------------------
    def generate_transactions(self, days=30):

        transaction_id = 1
        start_date = datetime(2026, 1, 1)

        for account in self.accounts:

            transaction_count = random.randint(5, 15)

            for _ in range(transaction_count):

                transaction_date = (
                    start_date +
                    timedelta(days=random.randint(0, days - 1))
                )

                transaction_type = random.choice([
                    "ATM",
                    "UPI",
                    "NET_BANKING",
                    "DEBIT_CARD",
                    "CREDIT_CARD"
                ])

                amount = round(
                    random.uniform(100, 100000), 2
                )

                debit_credit = random.choice(
                    ["Debit", "Credit"]
                )

                self.transactions.append({
                    "transaction_id": f"TXN{transaction_id:010d}",
                    "account_id": account["account_id"],
                    "customer_id": account["customer_id"],
                    "transaction_date": transaction_date.strftime(
                        "%Y-%m-%d"
                    ),
                    "transaction_type": transaction_type,
                    "debit_credit": debit_credit,
                    "amount": amount,
                    "currency": "INR",
                    "transaction_status": random.choice([
                        "SUCCESS",
                        "SUCCESS",
                        "SUCCESS",
                        "FAILED"
                    ])
                })

                transaction_id += 1

    # ---------------------------------------------------------
    # Write CSV files
    # ---------------------------------------------------------
    def save_data(self):

        datasets = {
            "branches": self.branches,
            "employees": self.employees,
            "customers": self.customers,
            "accounts": self.accounts,
            "loans": self.loans,
            "credit_cards": self.credit_cards,
            "beneficiaries": self.beneficiaries,
            "transactions": self.transactions
        }

        for name, data in datasets.items():

            file_path = self.output_directory / f"{name}.csv"

            pd.DataFrame(data).to_csv(
                file_path,
                index=False
            )

            print(
                f"Generated {name}.csv "
                f"({len(data):,} rows)"
            )

    # ---------------------------------------------------------
    # Run everything
    # ---------------------------------------------------------
    def run(self):

        print("\nStarting banking data generation...\n")

        self.generate_branches()
        self.generate_employees()
        self.generate_customers()
        self.generate_accounts()
        self.generate_loans()
        self.generate_credit_cards()
        self.generate_beneficiaries()
        self.generate_transactions()

        self.save_data()

        print("\nData generation completed successfully.")