class Statistics:
    def count_color(self, autos, color):
        cnt = 0

        for auto in autos:
            if auto.color == color:
                cnt += 1

        return cnt

    def avg_year(self, autos, make):
        s = 0
        cnt = 0

        for auto in autos:
            if auto.make == make:
                cnt += 1
                s += auto.year

        return s/cnt
