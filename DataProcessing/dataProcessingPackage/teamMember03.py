# File Name: teamMember03.py
# Student Name: Caitlin Hutchins
# email: hutchicu@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 4/20/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This assignment takes a csv file and presents interesting data about it

# Brief Description of what this module does: This module shows the top 5 cities by population along with the count
# Citations: ChatGPT


# teamMember03.py

class teamMember03:
    def print_something_interesting(self, data):
        print("===========================")
        print("Caitlin Hutchins (Team member03)")
        print("TOP 5 CITIES BY POPULATION")

        # Count occurrences of each city
        city_counts = {}
        for person in data:
            city = person['city']
            if city in city_counts:
                city_counts[city] += 1
            else:
                city_counts[city] = 1

        # Sort cities by count
        sorted_cities = sorted(city_counts.items(), key=lambda x: x[1], reverse=True)

        # Take top 5 cities
        top_5_cities = sorted_cities[:5]

        # Display results
        for i, (city, count) in enumerate(top_5_cities, 1):
            print(f"{i}. {city}: {count} people")

        print("===========================")

         