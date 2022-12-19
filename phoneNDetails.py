import phonenumbers
from phonenumbers import timezone,geocoder,carrier

mobnumr=input("Enter your mobile number with +__: ")
mobileN=phonenumbers.parse(mobnumr)
time=timezone.time_zones_for_number(mobileN)
carr=carrier.name_for_number(mobileN,"en")
reg=geocoder.description_for_number(mobileN,"en")
print(mobileN)
print(time)
print(carr)
print(reg)