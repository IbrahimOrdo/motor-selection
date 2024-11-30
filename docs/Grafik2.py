import matplotlib.pyplot as plt

class User:
    def __init__(self, name, weekly_travel_distance):
        self.name = name
        self.weekly_travel_distance = weekly_travel_distance

    def get_travel_distance(self):
        return self.weekly_travel_distance

class TravelChart:
    def __init__(self, users):
        self.users = users

    def plot(self):
        names = [user.name for user in self.users]
        travel_distances = [user.get_travel_distance() for user in self.users]
        
        plt.bar(names, travel_distances, color='green')
        plt.title('Weekly Travel Distance')
        plt.xlabel('Users')
        plt.ylabel('Travel Distance (km)')
        plt.show()

# Example usage:
users = [
    User('User 1', 50.5),
    User('User 2', 35.0),
    User('User 3', 60.0),
    User('User 4', 40.0),
    User('User 5', 55.0)
]

chart = TravelChart(users)
chart.plot()
