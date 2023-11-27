from bank_account import BankAccount
from person import Person

person = Person("Nicholas", "Fontana")
person.say_hello()

account = BankAccount("001789", 1000)
print(account)

account.deposit(100)
print(account)
account.withdraw(400)
print(account)

account2 = BankAccount("1234", 500)
account2.deposit(500)
print(account2)