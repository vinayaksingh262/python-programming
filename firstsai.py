class BankAccount:
    def _init_(self):
        self.balance = 0
        self.transactions = []
        self.commit_points = []
        self.output = []

    def read_balance(self):
        self.output.append(str(self.balance))

    def credit(self, amount):
        self.balance += amount
        self.transactions.append(amount)

    def debit(self, amount):
        self.balance -= amount
        self.transactions.append(-amount)

    def abort(self, abort_index):
        if 0 < abort_index <= len(self.transactions):
            committed = len(self.commit_points) > 0
            if not committed:
                self.balance -= self.transactions[abort_index - 1]
                self.transactions[abort_index - 1] = 0

    def rollback(self, rollback_index):
        if 0 < rollback_index <= len(self.commit_points):
            # Restore balance to the commit point
            self.balance = self.commit_points[rollback_index - 1]
            # Remove all commit points after the rollback point
            self.commit_points = self.commit_points[:rollback_index]
            # Clear all transactions after rollback
            self.transactions.clear()

    def commit(self):
        # Save the current balance as a commit point
        self.commit_points.append(self.balance)
        # Clear the current transactions
        self.transactions.clear()

    def process_operations(self, operations):
        for operation in operations:
            parts = operation.split()
            command = parts[0]

            try:
                if command == "read":
                    self.read_balance()
                elif command == "credit":
                    self.credit(int(parts[1]))
                elif command == "debit":
                    self.debit(int(parts[1]))
                elif command == "abort":
                    self.abort(int(parts[1]))
                elif command == "rollback":
                    self.rollback(int(parts[1]))
                elif command == "commit":
                    self.commit()
                else:
                    raise ValueError(f"Unknown operation: {command}")
            except (IndexError, ValueError) as e:
                self.output.append(f"Error: {e}")

        return "\n".join(self.output)


if __name__ == "_main_":
    try:
        balance = int(input().strip())
        n = int(input().strip())
        operations = [input().strip() for _ in range(n)]
        bank_account = BankAccount()
        bank_account.balance = balance
        result = bank_account.process_operations(operations)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
