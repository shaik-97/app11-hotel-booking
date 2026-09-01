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
    def __init__(self, name):
        self.name = name


class Hotel:
    def __init__(self, hotel_id=None):
        self.id = hotel_id

    @staticmethod
    def get_all_hotels():
        return pd.read_csv("hotels.csv")

    def view_hotels(self, is_availability_24x7=False):
        log.debug("Viewing hotels; 24X7 availability filter=%s", is_availability_24x7)
        hotels_list = self.get_all_hotels()

        if is_availability_24x7:
            filtered_hotels = hotels_list[
                (hotels_list["24X7"].str.lower() == "yes")
            ]
            print("\nPlease find the hotels available 24X7:")
            print(filtered_hotels)
            return

        print("\nAvailable hotels:")
        print(hotels_list)

    def updated_hotel_list(self, hotel_id):
        log.debug("Updating hotel id=%s availability to no", hotel_id)
        df = self.get_all_hotels()
        df.loc[df["id"] == hotel_id, "availability"] = "no"
        df.to_csv("hotels.csv", index=False)

    def fetch_hotel_details(self, hotel_id):
        log.debug("Fetching details for hotel id=%s", hotel_id)
        df = self.get_all_hotels()
        return df[df["id"] == hotel_id].iloc[0].to_dict()

    def is_hotel_id_available(self, hotel_id) -> bool:
        log.debug("Checking availability for hotel id=%s", hotel_id)
        hotels_list = self.get_all_hotels()
        available_ids = hotels_list[hotels_list["availability"].str.lower() == "yes"]["id"].tolist()

        if hotel_id in available_ids:
            log.debug("Hotel id=%s is available", hotel_id)
            return True

        log.debug("Hotel id=%s is not available", hotel_id)
        return False

    def book_hotel(self, hotel_id):
        log.debug("Attempting to book hotel id=%s", hotel_id)
        if self.is_hotel_id_available(hotel_id):
            hotel_details = self.fetch_hotel_details(hotel_id)
            print(f"\nHotel booked successfully! Details: {hotel_details}")
            self.updated_hotel_list(hotel_id)
            log.info("Hotel id=%s booked successfully", hotel_id)
            return True

        log.warning("Hotel id=%s booking unsuccessful or unavailable", hotel_id)
        print("\nHotel booking unsuccessful")
        return False


class Payment:
    def __init__(self, method):
        self.method = method.lower()

    def process(self):
        if self.method in {"cash", "online"}:
            print(f"Payment selected: {self.method}")
            return True

        print("Invalid payment method selected.")
        return False


class BookingApp:
    def __init__(self):
        self.hotel = Hotel()

    def welcome(self):
        print("--- Welcome to Agoda Hotel Booking ---")

    def run(self):
        self.welcome()
        self.hotel.view_hotels(is_availability_24x7=False)

        try:
            hotel_id = int(input("\nEnter hotel id for booking: "))
        except ValueError:
            print("Please enter a valid hotel id number.")
            return

        if not self.hotel.book_hotel(hotel_id):
            return

        payment_method = input("Choose payment method (cash/online): ").strip().lower()
        payment = Payment(payment_method)
        payment.process()


def main():
    app = BookingApp()
    app.run()


if __name__ == "__main__":
    main()
