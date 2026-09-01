import pandas as pd
hotels_list = pd.read_csv("hotels.csv")
#print(hotels_list)
#prints header
#print(hotels_list.columns.tolist())
hotels_avail_24X7 = hotels_list[
    (hotels_list["24X7"] == 'yes') | (hotels_list["24X7"] == 'YES') | (hotels_list["24X7"] == 'Yes')]["id"].tolist()
print(hotels_avail_24X7)

hotel_details = hotels_list[hotels_list["id"] == 2].iloc[0].to_dict()
print(type(hotel_details))

def is_hotel_id_available(id) -> bool:
    print(f'Checking availability for hotel id={id}')
    hotels_list = pd.read_csv("hotels.csv")
    hotel_ids = hotels_list[hotels_list["availability"] == "yes"]["id"].tolist()
    print(f'hotel_ids->{hotel_ids} and id -> {id}')
    if id in hotel_ids:
        print("Hotel id=%s is available", id)
        return True
    print("Hotel id=%s is not available", id)
    return False

print(is_hotel_id_available(4))