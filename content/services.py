from django.db import connection


def get_flight_with_city_and_data(city1, city2, data_depart):
    with connection.cursor() as cursor:
        cursor.execute("select flight.id, number_flight, model, company.name as company, arriv.name as arrival_city,"
                       " depart.name as departure_city, data_departure, time_departure, data_arrive, price from flight"
                       " JOIN airplane ON flight.airplane_id=airplane.id"
                       " JOIN company ON flight.company_id=company.id"
                       " JOIN city as depart ON departure_city_id=depart.id"
                       " JOIN city as arriv ON arrival_city_id=arriv.id"
                       " where depart.name = %s AND arriv.name = %s"
                       "AND flight.data_departure = %b", [city1, city2, data_depart])
        flights = cursor.fetchall()

    return flights


def get_flight_with_city(city1, city2):
    with connection.cursor() as cursor:
        cursor.execute("select flight.id, number_flight, model, company.name as company, arriv.name as arrival_city,"
                       " depart.name as departure_city, data_departure, time_departure, data_arrive, price from flight"
                       " JOIN airplane ON flight.airplane_id=airplane.id"
                       " JOIN company ON flight.company_id=company.id"
                       " JOIN city as depart ON departure_city_id=depart.id"
                       " JOIN city as arriv ON arrival_city_id=arriv.id"
                       " where depart.name = %s AND arriv.name = %s "
                       "order by data_departure ASC", [city1, city2])
        flights = cursor.fetchall()

    return flights


def get_airplane_flights(airplane):
    return airplane.flights.all()