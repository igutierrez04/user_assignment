class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == False:
            print(f"Welcome {self.first_name} you are now a member!")
            self.is_rewards_member = True
            self.gold_card_points += 200
            print(f"Here is your sign up bonus of {self.gold_card_points}")
            return False
        else:
            print(f"{self.first_name} is already a member")
            return True

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            print(f"You've spent {amount} of points.")
            self.gold_card_points -= amount
        elif self.gold_card_points < amount:
            print("Insuficient amount of points.")
        return self.gold_card_points




ivan = User("Ivan", "Gutierrez", "gutierrezI@email.com", 29)
ivan.enroll()
ivan.spend_points(200)
print(ivan.gold_card_points)
ivan.spend_points(10)
ivan.display_info()