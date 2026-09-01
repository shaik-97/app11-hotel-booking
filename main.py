# hotel booking app
import logging
import pandas as pd

logging.basicConfig(
    filename="app11.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s:%(lineno)d: %(message)s",
)
log = logging.getLogger(__name__)

class User:
    pass

class Customer(User):
    pass
    # def __init__(self, name):
    #     self.name = name
    #     self.loyalty_points = 0

    # def add_loyalty_points(self, points):
    #     self.loyalty_points += points
    #     log.debug("Added %s loyalty points to user %s", points, self.name)

class Hotel:
    def __init__(self, hotel_id=None,is_availability_24x7=False):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].iloc[0] if not df[df["id"] == self.hotel_id].empty else None
        self.hotel_city = df.loc[df["id"] == self.hotel_id, "city"].values[0] if not df[df["id"] == self.hotel_id].empty else None
        self.price = df.loc[df["id"] == self.hotel_id, "pernightprice"].values[0] if not df[df["id"] == self.hotel_id].empty else None
        self.is_availability_24x7 = is_availability_24x7

    def get_all_hotels(self):
        log.debug("Fetching all hotels from CSV")
        return pd.read_csv("hotels.csv")

    def view_hotels(self,):
        log.debug("Viewing hotels; 24X7 availability filter=%s", self.is_availability_24x7)
        hotels_list = self.get_all_hotels()
        if self.is_availability_24x7:
            print(" Please find list of below hotels which are available 24X7 ")
            hotels_avail_24x7 = hotels_list[
                (hotels_list["24X7"] == 'yes') | (hotels_list["24X7"] == 'YES') | (hotels_list["24X7"] == 'Yes')]
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n',hotels_avail_24x7,'\n')

    def updated_hotel_list(self,):
        log.debug("Updating hotel id=%s availability to no", self.hotel_id)
        df = pd.read_csv("hotels.csv")
        df.loc[df["id"] == self.hotel_id, "availability"] = "no"
        df.to_csv("hotels.csv", index=False) # False bcz we don't want index column to be added in csv file 
        print(f'updated list of hotels :-\n {df.to_string(index=False)}')
        return

    def book_hotel(self,):
        log.debug("Attempting to book hotel id=%s", self.hotel_id)
        if self.is_hotel_id_available(self.hotel_id):
            log.debug(f"Hotel booked successfully! -> details : \n hotel_id-->{self.hotel_id} \n hotel_name-->{self.name} \n hotel_city-->{self.hotel_city} \n hotel_price-->{self.price}")
            self.updated_hotel_list()
            log.info("Hotel id=%s booked successfully", self.hotel_id)
            return True
        log.warning("Hotel id=%s booking unsuccessful or unavailable", self.hotel_id)
        print("Hotel booking unsuccessful")

    def is_hotel_id_available(self, h_id) -> bool:
        log.debug(f'Checking availability for hotel id={h_id}')
        hotel_ids = df[df["availability"] == "yes"]["id"].tolist()
        log.debug(f'hotel_ids->{hotel_ids} and id -> {h_id}')
        
        if h_id in hotel_ids:
            log.debug("Hotel id=%s is available", h_id)
            return True
        log.debug("Hotel id=%s is not available", h_id)
        return False

    def make_all_hotels_available(self):
        log.debug("Making all hotels available")
        df = pd.read_csv("hotels.csv")
        df["availability"] = "yes"
        df.to_csv("hotels.csv", index=False)
        print("All hotels are now available for booking.")

class ReserveTickets:
    def __init__(self, hotel):
        self.hotel = hotel

    def generate_tickets(self):
        pass

class Payment:
    def __init__(self, amount):
        self.amount = amount
    def do_process(self):
        log.debug("Processing payment of amount %s", self.amount)
        print(f"Payment of amount {self.amount} processed successfully.")
        return True    
        
    def payment_receipt(self):
        log.debug("please find the payment receipt for the amount %s", self.amount)
        return True

class CreditCardPayment(Payment):
    def __init__(self,amount, number,exp,cvv,holder_name):
        super().__init__(amount)
        self.number = number
        self.exp = exp
        self.cvv = cvv
        self.holder_name = holder_name

    def validate_Card(self):
        card_data = {
            "number": self.number,
            "exp": self.exp,
            "cvv": self.cvv,
            "holder_name": self.holder_name
        }
        if card_data in df_card:
            log.debug("Credit card validated successfully for holder_name=%s", self.holder_name)
            print("Credit card validated successfully")
            return True
        log.debug("Credit card validation failed for holder_name=%s", self.holder_name)
        return False

        
class Welcome:
    def welcome_user(self):
        print("--- Welcome to Agoda Hotel Booking ---\n\n")

df = pd.read_csv("hotels.csv",dtype={"id": str,"availability": str, "24X7": str})
df_card = pd.read_csv("cards.csv").to_dict(orient='records')  # Convert to list of dictionaries for easier comparison
print(df_card,'\n')

def main():
    welcome = Welcome()
    welcome.welcome_user()

    print(df.to_string(index=False),'\n\n')
    hotel_booking_id = input(" Enter hotel id for booking:")
    hotel = Hotel(hotel_booking_id,is_availability_24x7=True)
    hotel.make_all_hotels_available()  # Reset availability for testing purposes
    hotel.view_hotels()
    creditcard = CreditCardPayment(amount=8889, number=1234, exp="12/26", cvv=111, holder_name="DESH")
    if creditcard.validate_Card():
        creditcard.do_process()
        creditcard.payment_receipt()
        if hotel.book_hotel():
            print(f"Hotel booking successful for id={hotel_booking_id}")
            log.debug("Hotel booking successful for id=%s", hotel_booking_id)
            ticket = ReserveTickets(hotel)
            ticket.generate_tickets()
        else:
            log.debug("Hotel booking unsuccessful for id=%s", hotel_booking_id)
    else:
        print("Credit card validation failed. Cannot proceed with booking.")


if __name__ == "__main__":
    main()
