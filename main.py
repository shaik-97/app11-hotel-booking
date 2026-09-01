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

df = pd.read_csv("hotels.csv")
class Hotel:
    def __init__(self, hotel_id=None):
        self.id = hotel_id
        self.name = df[df["id"] == hotel_id]["name"]

    def get_all_hotels(self):
        log.debug("Fetching all hotels from CSV")
        return pd.read_csv("hotels.csv")

    def view_hotels(self, is_availability_24x7):
        log.debug("Viewing hotels; 24X7 availability filter=%s", is_availability_24x7)
        hotels_list = self.get_all_hotels()
        if is_availability_24x7:
            print(" Please find list of below hotels which are available 24X7 ")
            hotels_avail_24x7 = hotels_list[
                (hotels_list["24X7"] == 'yes') | (hotels_list["24X7"] == 'YES') | (hotels_list["24X7"] == 'Yes')]
            print(hotels_avail_24x7)
        print(hotels_list)

    def updated_hotel_list(self, hotel_id):
        log.debug("Updating hotel id=%s availability to no", hotel_id)
        df = pd.read_csv("hotels.csv")
        df.loc[df["id"] == hotel_id, "availability"] = "no"
        df.to_csv("hotels.csv", index=False) # False bcz we don't want index column to be added in csv file 
        #print(f'updated list of hotels :- {df}')

    def book_hotel(self, hotel_id):
        log.debug("Attempting to book hotel id=%s", hotel_id)
        if self.is_hotel_id_available(hotel_id):
            hotel_details = self.fetch_hotel_details(hotel_id)
            f"""
            Hotel booked successfully! -> details : {hotel_details}
            """
            self.updated_hotel_list(hotel_id)
            log.info("Hotel id=%s booked successfully", hotel_id)
            return
        log.warning("Hotel id=%s booking unsuccessful or unavailable", hotel_id)
        print("Hotel booking unsuccessful")

    def fetch_hotel_details(self, id):
        log.debug("Fetching details for hotel id=%s", id)
        df = pd.read_csv("hotels.csv")
        hotel_details = df[df["id"] == id].iloc[0].to_dict()
        return  hotel_details

    def is_hotel_id_available(self, h_id) -> bool:
        log.debug(f'Checking availability for hotel id={h_id}')
        hotels_list = pd.read_csv("hotels.csv")
        hotel_ids = hotels_list[hotels_list["availability"] == "yes"]["id"].tolist()
        log.debug(f'hotel_ids->{hotel_ids} and id -> {h_id}')
        
        if h_id in hotel_ids:
            log.debug("Hotel id=%s is available", h_id)
            return True
        log.debug("Hotel id=%s is not available", h_id)
        return False


class ReserveTickets:
    def generate_tickets(self):
        pass

class Payment:
    def cash_payment(self):
        pass
    def online_payment(self):
        pass
class Welcome:
    def welcome_user(self):
        print("--- Welcome to Agoda Hotel Booking ---")




def main():
    hotel = Hotel()
    hotel.view_hotels(is_availability_24x7=False)
    hotel_booking_id = int(input(" Enter hotel id for booking: "))
    hotel.book_hotel(hotel_booking_id)

if __name__ == "__main__":
    main()
