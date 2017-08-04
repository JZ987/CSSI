class SpaceShip:

    def __init__(self, color, can_shoot, speed):
        self.color = color
        self.can_shoot = can_shoot
        self.speed = speed

    def HowFast(self):
        return "This space ship can travel at {}".format(self.speed)

    def ChangeSpeed(self, new_speed):
        self.speed = str(new_speed) + " mph"

EbonHawk = SpaceShip("white", True, "speed of light")
Ghost = SpaceShip("white", True, "23878490 mph")

print(EbonHawk.HowFast())
EbonHawk.ChangeSpeed(23242143)
print(EbonHawk.HowFast())
