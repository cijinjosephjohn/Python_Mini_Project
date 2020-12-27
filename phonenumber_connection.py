import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

if __name__=="__main__":
    num=input("enter the phone Number : ")
    try:
        country = phonenumbers.parse(num,"CH")
        print(geocoder.description_for_number(country,"en"))
        service_num = phonenumbers.parse(num,"RO")
        ans=carrier.name_for_number(service_num,"en")
        if ans=='Idea' or ans=='Vodafone':
            print('VI')
        else:
            print(ans)
    except:
        print("Something Went Wrong")
