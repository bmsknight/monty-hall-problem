import random


class Host:

    def __init__(self, door_count=3):
        assert door_count >= 3
        self._car_index = int(random.uniform(0, door_count))
        self.door_count = door_count

    def present_doors(self):
        return self.door_count

    def eliminate_others_and_present_one_door(self, contestant_selection):
        if contestant_selection == self._car_index:
            while True:
                alternative_door = int(random.uniform(0, self.door_count))
                if alternative_door != contestant_selection:
                    return alternative_door
        else:
            return self._car_index

    def reveal_if_winner(self,final_selection):
        if final_selection == self._car_index:
            return True
        else:
            return False
