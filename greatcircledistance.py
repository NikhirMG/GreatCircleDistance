#"If it works it works ¯\_(ツ)_/¯ " - N J.Manilal
from math import sin, cos, asin, sqrt, radians 

def AskUser():
    while True:
        response = input("\nWould you like to compute another?(yes/no): ")
        if response == "yes":
            Begin()
        else:
            break

def Calculation(latitude_1, latitude_2, longitude_1, longitude_2):
    
    #Convert values from degrees to radians.
    longitude_1 = radians(longitude_1)
    longitude_2 = radians(longitude_2)
    latitude_1 = radians(latitude_1)
    latitude_2 = radians(latitude_2)

    #Haversine formula
    longitude = longitude_2 - longitude_1
    latitude = latitude_2 - latitude_1
    a = sin(latitude / 2)**2 + cos(latitude_1) * cos(latitude_2) * sin(longitude / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    #Radius of earth in kilometers
    radius_km = 6371
      
    #Calculate the result
    result = c * radius_km

    print("\nApproximate Distance: ", round(result,2), "KM")

def Begin():
    latitude_1 = float(input("\n\tPlease enter Latitude value of location 1:\n\t"))
    longitude_1 = float(input("\n\tPlease enter Longitude value of location 1:\n\t"))   
    latitude_2 = float(input("\n\tPlease enter Latitude value of location 2:\n\t"))
    longitude_2 = float(input("\n\tPlease enter Longitude value of location 2:\n\t"))
    Calculation(latitude_1, latitude_2, longitude_1, longitude_2)

#Beginning 
print("Welcome Human |ʘ‿ʘ)╯,")
print("\nThis Program allows you to compute the great circle distance between two points on the earth's surface")
print("\n\nPlease use the Decimal degree format of your coordinates(i.e. 42.3601) ")  
Begin()
AskUser()
