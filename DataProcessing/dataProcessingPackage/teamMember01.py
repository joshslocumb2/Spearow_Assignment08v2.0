# File Name: teamMember01.py
# Student Name: Josh Slocumb
# email: slocumbjt@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 4/20/2025
# Course #/Section: IS 4010-001
# Semester/Year:Spring 2025
# Brief Description of the assignment: THis assignment takes a csv file and presents interesting data about it

# Brief Description of what this module does: this module shows the top 5 states by population along with the count
# Citations: Perplexity AI


class teamMember01:
    def print_something_interesting(self, data):
            print("===========================")
            print("Joshua Slocumb (Team member01)")
            print("TOP 5 STATES BY POPULATION")
           
        
            # Count occurrences of each state
            state_counts = {}
            for person in data:
                state = person['state']
                if state in state_counts:
                    state_counts[state] += 1
                else:
                    state_counts[state] = 1
        
            # Sort states by count
            sorted_states = sorted(state_counts.items(), key=lambda x: x[1], reverse=True)
        
            # Take top 5 states
            top_5_states = sorted_states[:5]
        
            # Display results
            for i, (state, count) in enumerate(top_5_states, 1):
                print(f"{i}. {state}: {count} people")
                
            print("===========================")


