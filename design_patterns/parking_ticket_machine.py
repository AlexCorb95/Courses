class ParkingTicketMachine:
    def __init__(self,price_per_hour):
        self.ticket_money = 0
        self.price_per_hour=price_per_hour



    def add_money(self, money):
        self.ticket_money = money

    def check_ticket(self, money):
        if money > 0:
            if money >= self.price_per_hour:
                return True
    def print_ticket(self):
        if self.check_ticket(self.ticket_money):
            print(f"Your ticket is valid for { self.ticket_money/self.price_per_hour} hours ")
        else:
            print(f"You need {self.price_per_hour-self.ticket_money} more for an hour")


ticket=ParkingTicketMachine(80)
ticket.add_money(90)
ticket.print_ticket()
