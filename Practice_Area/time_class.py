class Time:

    def __init__(self, hr, min):
        self.hr = hr
        self.min = min
        self.tot_hr = hr
        self.tot_min = min

    def addTime(self, hr1=0, min1=0):
        self.tot_hr = self.hr + hr1
        self.tot_min = self.min + min1
        if self.tot_min > 60:
            h, m = divmod(self.tot_min, 60)
            self.tot_hr += h
            self.tot_min = m

        return self.tot_hr, self.tot_min

    def displaytime(self):
        print("Total Time is - {} hr, {} min".format(self.tot_hr, self.tot_min))


obj1 = Time(2, 40)
obj1.addTime(6, 45)
obj1.displaytime()
