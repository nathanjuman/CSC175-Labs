class Flights:
    """ Flight class to represent airline flight information such as city of departure, destination city, and distance between departure and destination. """

    def __init__(self, departure, destination, distance):
        """ Create new flight information for departure, destination, and distance between the departure city and destination city. """
        self.__my_departure = departure
        self.__my_destination = destination
        self.__my_distance = distance

    def get_departure(self):
        """ Return the departure city of the current flight object. """
        return self.__my_departure
    
    def get_destination(self):
        """ Return the destination city of the current flight object. """
        return self.__my_destination
    
    def get_distance(self):
        """ Return the distance between the departure city and the destination city. """
        return self.__my_distance
    
    def traveltime(self, speed):
        """ This method returns the travel time between the departed city and the destination city using the speed of the aircraft and the distance between the two cities. """
        return self.__my_distance / speed
    
    def extend(self, flight):
        """ This method takes in a flight object and returns none if the parameter departure city does not match of the destination flight for the self object. If the two flights do match, a new flight object is created with the self's departure, the parameter's destination, and a distance equal to the self distance and parameter distance added together. """
        if flight.__my_departure != self.__my_destination:
            return None
        else:
            return Flights(self.__my_departure, flight.__my_destination, (self.__my_distance + flight.__my_distance))

    def __str__(self):
        """ Returns the current flight object information. """
        return f"Your flight is departing from {self.__my_departure} and will travel {self.__my_distance} miles to {self.__my_destination}."

def main():
    
    f1_departure = input("Where are you departing from? ")
    f1_destination = input("Where is the destination? ")
    f1_distance = float(input("How far is the journey (miles)? "))
    f1_speed = float(input("How fast is the airline moving on average (mph)? "))

    f1 = Flights(f1_departure, f1_destination, f1_distance)

    f2_departure = input("Where are you departing from? ")
    f2_destination = input("Where is the destination? ")
    f2_distance = float(input("How far is the journey (miles)? "))
    f2_speed = float(input("How fast is the airline moving on average (mph)? "))
    print("\n")


    f2 = Flights(f2_departure, f2_destination, f2_distance)

    f3 = f1.extend(f2)

    print(f"Departing from {f1.get_departure()}, traveling for {f1.get_distance()} miles, and landing in {f1.get_destination()}.\n")
    print(f"Departing from {f2.get_departure()}, traveling for {f2.get_distance()} miles, and landing in {f2.get_destination()}.\n")

    print(f"Flight from {f1.get_departure()} to {f1.get_destination()} will take approximately {f1.traveltime(f1_speed):.2f} hours.\n")
    print(f"Flight from {f2.get_departure()} to {f2.get_destination()} will take approximately {f2.traveltime(f1_speed):.2f} hours.\n")

    if f3 == None:
        print("The combined flight cannot be computed.\n")
    else:
        print(f"This extended flight departing from {f3.get_departure()}, will travel {f3.get_distance()} miles to {f3.get_destination()}. The flight will take approximately {f3.traveltime(f1_speed):.2f} hours.\n")
main()

'''
    Test Case 1:
    Flight One departs from Syracuse to Atlanta which is 963.2 miles.
    Flight Two departs from Atlanta to Miami which is 662.8 miles.

    Flight Three is the extension of the first and second flight.

    What is the information for the first two flights?

    The first two flights are traveling at a speed of 575 mph. What is the travel time for both?

    Compute the info for flight three.

    Test Case 2:
    Flight One departs from Syracuse to Boston which is 312.1 miles.
    Flight Two departs from Denver to Los Angeles which is 1016.5 miles.

    Flight Three is the extension of the first and second flight.

    What is the information for the first two flights?

    The first two flights are traveling at a speed of 575 mph. What is the travel time for both?

    Compute the info for flight three.
'''