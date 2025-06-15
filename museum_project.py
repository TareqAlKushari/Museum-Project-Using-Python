# Define a class to represent a museum section
class Section:
    # Define a class attribute to store the total number of visitors
    total_visitors = 0

    # Define an initializer method to set the name and the number of visitors for each section
    def __init__(self, name):
        self.name = name
        self.visitors = 0

    # Define a method to increment the number of visitors for each section and the total number of visitors
    def enter(self):
        self.visitors += 1
        Section.total_visitors += 1

    # Define a method to display the number of visitors for each section
    def show_stats(self):
        print(f"Number of visitors in {self.name} section: {self.visitors}")

# Define a class to represent a museum
class Museum:
    # Define an initializer method to create three sections for the museum
    def __init__(self):
        self.historical = Section("historical")
        self.artistic = Section("artistic")
        self.islamic = Section("islamic")

    # Define a method to display the total number of visitors and the number of visitors for each section
    def show_stats(self):
        # Print the total number of visitors
        print(f"Total number of visitors: {Section.total_visitors}")
        # Print the number of visitors for each section
        self.historical.show_stats()
        self.artistic.show_stats()
        self.islamic.show_stats()

# Test the program
museum = Museum()
museum.historical.enter()
museum.artistic.enter()
museum.islamic.enter()
museum.islamic.enter()
museum.artistic.enter()
museum.show_stats()
