class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username 
        self.fans = 0   #Since all start with 0 fans best to keep without a parameter to enter
        self.simp = 0

    def follow(self, user):
        user.fans += 1
        self.simp += 1

user_1 = User("001", "Lino")

print(user_1) #note that this points at its memory location

user_2 = User("002", "Kek")
print(user_2.username) #Works as expected

user_1.follow(user_2)
print(user_1.fans)
print(user_1.simp)