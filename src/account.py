class Account:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.profiles = []

    def generate_profile(self, account):
        self.username = self.first_name.lower() + self.last_name[0]
        self.password = "password"
        profile = (self.username, self.password)
        return profile
    
    def add_profile(self, profile):
        self.profiles.append(profile)

    def remove_profile(self, profile):
        self.profiles.remove(profile)

    def get_profiles(self, account):
        return self.profiles