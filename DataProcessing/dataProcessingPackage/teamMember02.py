# teamMember02.py

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
