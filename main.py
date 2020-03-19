from boat_rental import BoatShop, Customer

def main():
    shop = BoatShop(100)
    customer = Customer()

    while True:
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request  boat(s) on hourly basis $50
        3. Request boat(s) on daily basis $999
        4. Request boat(s) on weekly basis $4999
        5. Return a bike
        6. Exit
        """)

        choice = input("Enter Choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Not a valid option")
            continue

        if choice==1:
            shop.display_stock()
        
        elif choice ==2:
            customer.rental_time = shop.rent_boat_by_hour(customer.request_boat())
            customer.rental_method = 1

        elif choice ==3:
            customer.rental_time = shop.rent_boat_by_days(customer.request_boat())
            customer.rental_method =2
        
        elif choice ==4:
            customer.rental_time = shop.rent_boat_by_weeks(customer.request_boat())
            customer.rental_method == 3
        
        elif choice ==5:
            customer.bill = shop.return_boat(customer.return_boat())
            customer.rental_method, customer.rental_time , customer.boats =0,0,0
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")
        
        print("Thank you for using our boat rental portal !")


if __name__ == "__main__":
    main()



