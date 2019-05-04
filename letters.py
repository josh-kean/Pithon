import pi_dict
class numSelect:

    def piDigit(self, count):
        pi=pi_dict.pi
        self.count = count

        currentDigit = pi[count]
        if currentDigit == 0:
            return "images/zero.png"
        elif currentDigit == 1:
            return "images/one.png"
        elif currentDigit == 2:
            return "images/two.png"
        elif currentDigit == 3:
            return "images/three.png"
        elif currentDigit == 4:
            return "images/four.png"
        elif currentDigit == 5:
            return "images/five.png"
        elif currentDigit == 6:
            return "images/six.png"
        elif currentDigit == 7:
            return "images/seven.png"
        elif currentDigit == 8:
            return "images/eight.png"
        elif currentDigit == 9:
            return "images/nine.png"
