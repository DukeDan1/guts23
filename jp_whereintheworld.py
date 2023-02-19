from FlightRadar24.api import FlightRadar24API
import json
fr_api = FlightRadar24API()

def get_all_flights():
    try:
        flights = fr_api.get_flights()
    except json.decoder.JSONDecodeError as err:
        print("Invalid flight ID")
        return {'success': False, 'error':err}
    except:
        return {'success': False, 'error':"Something went wrong"}
    return {'success': True, 'flights':flights}


def get_flight(flights, id):
    for flight in flights:
        if flight.id == id:
            return {'success': True, 'flight':flight}
        elif flight.registration == id:
            return {'success': True, 'flight':flight}
        elif flight.number == id:
            return {'success': True, 'flight':flight}
        
    
    return {'success': False, 'error':"Flight not found"}

def output(flight):
    print("Current location:")
    print(" -->  Latitude:", flight.latitude)
    print(" -->  Longitude:", flight.longitude, end='\n\n')
    
    try:
        origin = fr_api.get_airport(flight.origin_airport_iata)
        destination = fr_api.get_airport(flight.destination_airport_iata)

        print("Origin airport:")
        print(" -->  Name:", origin['name'])
        print(" -->  Country:", origin['position']['country']['name'])
        print(" -->  IATA:", origin['code']['iata'], end='\n\n')

        print("Destination airport:")
        print(" -->  Name:", destination['name'])
        print(" -->  Country:", destination['position']['country']['name'])
        print(" -->  IATA:", destination['code']['iata'])
    except:
        print("Unable to get airport information")



def main():
    allFlights = get_all_flights()
    
    if not allFlights['success']: 
        print(allFlights['error'])
    else:
        print("If you can't think of a flight to search for, perhaps you could try one of these: ", end='')
        printedFlights, i = 0, -1
        if len(allFlights['flights']) < 5: return print("Not enough flights found")
        while printedFlights < 5:
            if allFlights['flights'][i].registration != "N/A":
                print(allFlights['flights'][i].registration, end=' ')
                printedFlights += 1
            i -= 1
            
        print()   
        id = input("Enter a flight ID or aircraft registration: ")
        flight = get_flight(allFlights['flights'], id)
        
        if not flight['success']: 
            print(flight['error'])
        else: 
            output(flight['flight'])

main()