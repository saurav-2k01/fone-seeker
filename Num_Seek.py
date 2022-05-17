import phonenumbers as pn
from phonenumbers import geocoder, carrier, timezone
import pandas as pd

class Num_Digger():
    def __init__(self, Dial_Code, Number):
        self.Dial_Code = Dial_Code
        self.Number = Number
        #self.Country_Code = Country_Code

    def Raw_Info(self):
        Raw_Data = {}
        Num = self.Number
        Country_Code = self.Country_Code()
        Phone_Number = pn.parse(Num, Country_Code)
        Valid = pn.is_valid_number(Phone_Number)
        Possibility = pn.is_possible_number(Phone_Number)
        Status = pn.is_valid_number_for_region(Phone_Number,Country_Code)
        Country = geocoder.country_name_for_number(Phone_Number,'en')
        Time_zone = timezone.time_zones_for_number(Phone_Number)
        Carrier = carrier.name_for_number(Phone_Number, "en")
        Int_format = pn.format_number(Phone_Number,pn.PhoneNumberFormat.INTERNATIONAL)
        Nat_format = pn.format_number(Phone_Number,pn.PhoneNumberFormat.NATIONAL)
        Raw_Data["Number"] = Num
        Raw_Data["Valid"] = Valid
        Raw_Data["Is_Possible"] = Possibility
        Raw_Data["Status"] = Status
        Raw_Data["Country"] = Country
        Raw_Data["Time Zone"] = Time_zone
        Raw_Data["Carrier"] = Carrier
        Raw_Data["International Format"] = Int_format
        Raw_Data["National Format"] = Nat_format
        return Raw_Data

    def Country_Code(self):
        Dial = self.Dial_Code
        df = pd.read_csv("country code.csv")
        index = df.index
        condition = df["Dial"] == Dial
        indices = index[condition]
        indx = indices.tolist()
        x = (df._get_value(indx[0], "ISO3166_1_Alpha_2"))
        return x

