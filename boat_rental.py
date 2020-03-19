import datetime

class BoatShop:

    def __init__(self, stock = 0):
        #our constructor class that initializes boat rental shop

        self.stock = stock

    def display_stock(self):
        #display number of boats currently available 
        print("We have currently {} bikes available to rent".format(self.stock))
        return self.stock

    def rent_boat_by_hour(self, n):

        if n <= 0:
            print("Number of boats should be positive")
            return None

        elif n>self.stock:
            print("Sorry we have only {} boats left to rent.".format(self.stock))
        else:
            now = datetime.datetime.now()
            print("Congratulations! You've rented  {} boat(s) on hourly today at {} hours.".format(n, now.hour))
            print("You'll be charged 50$ an hour for a single boat")
            print("We hope that you enjoy our service")

            self.stock -= n
            return now

    def rent_boat_by_days(self, n):
        if n<=0:
            print("Number of boats should be positive")
            return None
        elif n>self.stock:
            print("Sorry we have only {} boats left to rent.".format(self.stock))
        else:
            now = datetime.datetime.now()
            print("Congratulations! You've rented  {} boat(s) on daily basis today at {} hours.".format(n, now.hour))
            print("You'll be charged 999$ per day for a single boat")
            print("We hope that you enjoy our service")

            self.stock -= n
            return now

    def rent_boat_by_weeks(self, n):
        if n<=0:
            print("Number of boats should be positive")
            return None
        elif n>self.stock:
            print("Sorry we have only {} boats left to rent.".format(self.stock))
        else:
            now = datetime.datetime.now()
            print("Congratulations! You've rented  {} boat(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("You'll be charged 5000$ per week for a single boat")
            print("We hope that you enjoy our service")

            self.stock -= n
            return now


    def return_boat(self, request):
        rental_time, rental_method, num_of_boats = request
        bill = 0

        if rental_time and rental_method and num_of_boats:
            self.stock += num_of_boats
            now = datetime.datetime.now()
            rental_period = now - rental_time

            #hourly bill calculation
            if rental_method==1:
                bill = round(rental_period.seconds/3600)*50*num_of_boats
            #daily
            if rental_method == 2:
                bill = round(rental_period.days)*999*num_of_boats
            #weekly
            if rental_method == 3:
                bill = round(rental_period.days/7)*4999*num_of_boats
            
            if (3<= num_of_boats <=5):
                print("Congratualtions! You're eligible for Family Rental Promotion of 30% Discount ")
                bill = bill*0.7

            print("Thanks for returning your boat. Hope you enjoyed our service!")
            print("That would be {}$.".format(bill))
            return bill
        else:
            print("Are you sure you rented a bike with us ?")
            return None
        

class Customer:

    def __init__(self):
        self.boats = 0
        self.rental_method = 0
        self.rental_time = 0
        self.bill =0

    def request_boat(self):
        boats = input("How many boats would you like to rent (2 person per boat): ")
        try:
            boats = int(boats)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        
        if boats<1:
            print("Invalid Input")
            return -1
        else:
            self.boats = boats

        return self.boats
    
    def return_boat(self):
        if self.rental_method and self.rental_time and self.boats:
            return self.rental_time, self.rental_method, self.boats
        else:
            return 0,0,0
    


        
        



    

        