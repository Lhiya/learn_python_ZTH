#composition
class Building():
    room = []
    name = None

    def create_room(self, room):
        self.room.append(room)

    def remove_room(self, room):
        self.room.remove(room)

    def rooms(self):
        print(f"Ruangan dalam bangunan {self.name} : {self.room}")


class Room():
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return self.name

b1 = Building()
b1.name="ITEC"
b1.rooms()

r1 = Room("Instagram", "Biru")
r2 = Room("Whatsapp", "Hijau")

b1.create_room(r1)
b1.create_room(r2)
b1.rooms()

b1.remove_room(r2)
b1.rooms()
        
