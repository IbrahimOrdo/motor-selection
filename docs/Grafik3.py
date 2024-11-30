import matplotlib.pyplot as plt

class User:
    def __init__(self, name, income, expenses, age, driving_experience):
        self.name = name
        self.income = income
        self.expenses = expenses
        self.age = age
        self.driving_experience = driving_experience

    def get_income(self):
        return self.income

    def get_expenses(self):
        return self.expenses

    def get_age(self):
        return self.age

    def get_driving_experience(self):
        return self.driving_experience

class FinancialChart:
    def __init__(self, users):
        self.users = users

    def plot_income_vs_expenses(self):
        names = [user.name for user in self.users]
        incomes = [user.get_income() for user in self.users]
        expenses = [user.get_expenses() for user in self.users]

        plt.bar(names, incomes, color='blue', alpha=0.6, label='Income')
        plt.bar(names, expenses, color='red', alpha=0.6, label='Expenses')
        plt.title('Monthly Income vs Expenses')
        plt.xlabel('Users')
        plt.ylabel('Amount (USD)')
        plt.legend()
        plt.show()

    def plot_age_vs_experience(self):
        names = [user.name for user in self.users]
        ages = [user.get_age() for user in self.users]
        experiences = [user.get_driving_experience() for user in self.users]

        plt.plot(names, ages, marker='o', color='green', label='Age')
        plt.plot(names, experiences, marker='x', color='orange', label='Driving Experience')
        plt.title('Age vs Driving Experience')
        plt.xlabel('Users')
        plt.ylabel('Years')
        plt.legend()
        plt.show()

# Example Usage
users = [
    User('User 1', 3000, 2500, 25, 5),
    User('User 2', 4000, 3000, 30, 10),
    User('User 3', 3500, 2800, 28, 6),
    User('User 4', 5000, 4500, 35, 12),
    User('User 5', 4500, 4000, 40, 15)
]

chart = FinancialChart(users)
chart.plot_income_vs_expenses()  # Monthly Income vs Expenses (Bar Chart)
chart.plot_age_vs_experience()  # Age vs Driving Experience (Line Chart)
