# Robot Introduction (ACP starter, DSCM2L3). Python 3 standard library only.
# Run it in Google Colab (one cell) or as robot_introduction.py. It runs now; do TODO 1 to TODO 4 in order.
# Lines marked (given) are done for you.


class Robot:
    maker = "Bright Bots"                    # (given) A: class variable, the same for every robot

    def __init__(self, name, model, battery):
        # TODO 1: store name, model and battery on self. A battery below 0
        #   becomes 0 and a battery above 100 becomes 100.
        #   Check: after TODO 4, Jerry (made with 120) shows "Battery: 100%".
        self.name, self.model, self.battery = "?", "?", 0  # (given) placeholder: replace this line

    def introduce(self):
        # TODO 2: return "Hi, I am <name>, a <model> robot made by <maker>.
        #   Battery: <battery>%" using self for every value.
        #   Check: "Hi, I am Tom, a T-100 robot made by Bright Bots. Battery: 40%"
        return "(introduce not written yet)"  # (given) placeholder: replace this line

    def charge(self, amount):
        # TODO 3: if amount is 0 or less, return "Charge amount must be
        #   positive." and change nothing. Otherwise add it to the battery, cap it at 100 and
        #   return "<name> charged to <battery>%".
        #   Check: "Tom charged to 90%", then "Tom charged to 100%", then the positive-amount message.
        return "(charge not written yet)"  # (given) placeholder: replace this line


# TODO 4: create tom (name "Tom", model "T-100", battery 40) and
#   jerry (name "Jerry", model "J-200", battery 120).
#   Check: two introductions print, and Jerry's battery shows 100%.
tom = jerry = Robot("?", "?", 0)  # (given) placeholder: replace this line
print(tom.introduce())                                         # (given) B
print(jerry.introduce())
print(tom.charge(50))                                          # (given) C: normal charge
print(tom.charge(30))                                          # (given)    edge: goes past 100
print(tom.charge(-5))                                          # (given)    edge: bad amount
