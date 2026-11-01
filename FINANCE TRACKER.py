from datetime import datetime, timedelta
import winsound
import threading

class Finance:
    next_id=1
    def __init__(self,amount,type,category):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be an integer or a float.")
        if amount <= 0:
            raise ValueError("Amount is not valid.")

        if not isinstance(type, str):
            raise ValueError("Type must be an string.")
        if not isinstance(category, str):
            raise ValueError("Category must be an string.")
        if type.lower() != "income" and type.lower() != "expense":
            raise ValueError("The type should be either income or expense.")
        self.amount = amount
        self.type = type
        self.category = category
        self.time=datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

        self.transaction_id=f"TXN-{datetime.now().strftime("%y%m%d")}-{Finance.next_id:03d}"
        Finance.next_id += 1


salary=Finance(50000,"income","salary")
food=Finance(1000,"expense","food")

class Manager:
    def __init__(self):

       self.transactions = []

    def add_transaction(self,transaction):
         if isinstance(transaction, Finance):
             self.transactions.append(transaction)
         else:
            raise ValueError("This object is not valid.")
    def delete_transaction(self,transaction):
        if transaction in self.transactions:
            self.transactions.remove(transaction)
        else:
            raise ValueError("Transaction does not exist.")

    def calculate_income(self):
        income = 0
        for transaction in self.transactions:
            if transaction.type=="income":
                income+=transaction.amount
        return income
    def calculate_expense(self):

        expense = 0
        for transaction in self.transactions:
            if transaction.type=="expense":
                expense+=transaction.amount
        return expense

    def calculate_total(self):
        total_amount = 0


        for transaction in self.transactions:
             if transaction.type == "income":
                total_amount += transaction.amount
             if transaction.type == "expense":
                total_amount -= transaction.amount
        return total_amount
    def __str__(self):
        return f"The remaining balance is {self.calculate_total()}"

    def history(self):
        history = []

        for transaction in self.transactions:
            details=[transaction.amount,transaction.type,transaction.category,transaction.time,transaction.transaction_id]
            print(f"{details[0]} of {details[1]} was transacted in {details[2]} at {details[3]} ID={details[4]}")
            history.append(details)
        if not self.transactions:
            history=[]
            print( f"The transaction list is empty.")
        return history

class Reminder:
    def __init__(self,name,amount,due_date):

        self.name=name
        self.amount=amount
        self.due_date=due_date
        self.reminder_date=due_date-timedelta(days=7)
    def check_reminder(self):
        today=datetime.now().date()
        time_elapsed=self.due_date.date()-today
        if time_elapsed.days < 0:
            print(
            f"WOW OMG WE ARE DOOMED. HOW COULD YOU NOT MAKE A PAYMENT DUDE? THE PAYMENT WAS DUE ON LET'S SEE {abs(time_elapsed.days)} DAYS AGO.")
        elif time_elapsed.days == 0:


            print("YOUR PAYMENT IS DUE TODAY. MAKE THE PAYMENT RIGHT NOW! OR I WILL LOOP FOREVER.")
            self.play_alarm()

        elif today>=self.reminder_date.date():

            print(f"Alert!Your payment needs to be made in {time_elapsed.days} days.")


    def ring_alarm(self, stop_alarm):
        while not stop_alarm.is_set():
            winsound.Beep(1000, 500)

    def play_alarm(self):
        stop_alarm=threading.Event()
        worker=threading.Thread(target=self.ring_alarm, args=(stop_alarm,))
        worker.start()
        input("Press ENTER to stop the alarm...")
        stop_alarm.set()
        worker.join()




















manager = Manager()


transactions = len(manager.transactions)
manager.add_transaction(salary)
manager.add_transaction(food)
salary = Finance(50000, "income", "salary")
food = Finance(1000, "expense", "food")
transport = Finance(500, "expense", "transport")
netflix=Reminder("Netflix",300,datetime(2026,11,1))
subscription=Reminder("Subscription",300,datetime(2026,10,19))
rent=Reminder("Rent",300,datetime(2026,11,7))

print(manager.calculate_income())
print(manager.calculate_expense())
print(manager.calculate_total())
print(manager)
print(manager.history())
print(netflix.reminder_date)
netflix.check_reminder()

subscription.check_reminder()
rent.check_reminder()
rent.play_alarm()
subscription.play_alarm()
netflix.play_alarm()


