# teamMember02.py

# File Name: teamMember02.py
# Student Name: Richie James
# email: james2c4@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 4/20/2025
# Course #/Section: IS 4010-001
# Semester/Year:Spring 2025
# Brief Description of the assignment: THis assignment takes a csv file and presents interesting data about it

# Brief Description of what this module does: this module shows the top 5 states by population along with the count
# Citations: https://chatgpt.com/g/g-cKXjWStaE-python/c/68013c85-48ec-8012-b7c8-a765bd3ad91a

from collections import defaultdict

class teamMember02:
    def print_something_interesting(self, data):
        print("===========================")
        print("Richie James (Team member02)")
        print("Count of First Names Starting with 'A' by State")

        # Initialize dictionary to count 'A' names per state
        a_name_counts = defaultdict(int)

        # Loop through data and count names starting with 'A'
        for person in data:
            try:
                state = person['state']
                first_name = person['first_name']

                if first_name.lower().startswith('a'):
                    a_name_counts[state] += 1
            except KeyError as e:
                print(f"Skipping record due to missing key: {e}")
            except Exception as e:
                print(f"Skipping record due to unexpected error: {e}")

        # Sort results alphabetically by state for consistency
        for state in sorted(a_name_counts):
            count = a_name_counts[state]
            print(f"{state}: {count} name(s) starting with 'A'")

        print("===========================")
