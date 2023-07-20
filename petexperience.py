import pickle

class PetExperience:
    def __init__(self):
        self.experience_levels = [100, 300, 800, 1600, 3000]
        self.current_level = 1
        self.experience = 0
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update_ui()

    def feed(self):
        self.experience += 10
        if self.experience >= self.experience_levels[self.current_level - 1]:
            self.level_up()
        self.notify_observers()
        self.save_pet_data()

    def level_up(self):
        if self.current_level < len(self.experience_levels):
            self.current_level += 1
            print(f"Congratulations! Your pet leveled up to Level {self.current_level}!")
        self.notify_observers()  # Notify observers again to update UI after leveling up

    def save_pet_data(self):
        pet_data = {"current_level": self.current_level, "experience": self.experience}
        with open("pet_data.pkl", "wb") as file:
            pickle.dump(pet_data, file)