#!/usr/bin/env python

import sys
import random
import time


class Prisoner(object):

    def __init__(self):
        self.has_entered_room = False
        self.asserted_shennanigans_over = False

    def turn_on_light_bulb(self, room):
        room.light_bulb_is_on = True

    def turn_off_light_bulb(self, room):
        room.light_bulb_is_on = False

    def act_on_room(self, room):
        if room.light_bulb_is_on == False:
            #print("Включение лампочки")
            self.turn_on_light_bulb(room)
        else:
            print("Лампочка уже горит!(не считать)")

    def assert_shennanigans_over(self):
        self.asserted_shennanigans_over = True


class CountingPrisoner(Prisoner):

    def __init__(self):
        self.asserted_shennanigans_over = False
        self.count = 0

    def act_on_room(self, room):
        #print("Счетчик заходит!!!")
        if room.light_bulb_is_on == True:
            self.turn_off_light_bulb(room)
            self.count += 1

        if self.count == 9:
            self.assert_shennanigans_over()


class LivingRoom(object):

    def __init__(self):
        self.light_bulb_is_on = False


def main():
    living_room = LivingRoom()
    prisoners = [Prisoner() for i in range(10)]
    prisoners = prisoners + [CountingPrisoner()]

    # День старта
    days_since_shennanigans = 0
    while True:
        # рандомный заключенный входит в камепу
        prisoner = random.choice(prisoners)
        prisoner.act_on_room(living_room)
        days_since_shennanigans += 1
        if prisoner.asserted_shennanigans_over == True:
            break
    print("Прошло дней : " + str(days_since_shennanigans),
          "\nПрошло лет  : " + str(days_since_shennanigans / 356))
    sys.exit(0)


if __name__ == '__main__':
    main()
