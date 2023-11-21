class Phone:

    def make_call(self):
        print("Making a phone call")
    def play_game(self):
        print("Playing game")

    def set_color(self,color):
        self.color = color
    def set_cost(self,cost):
        self.cost = cost

    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost


    

dev = Phone()
# dev.make_call()
# dev.play_game()
dev.set_color("Blue")
dev.set_cost("13k")
print("color of phone is " , dev.show_color())
print("cost of phone is ",dev.show_cost())