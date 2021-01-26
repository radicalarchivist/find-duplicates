class Throbber():
    def __init__(self):
        self.throbber = ['[◉○○○○○○○○○]','[○◉○○○○○○○○]','[○○◉○○○○○○○]','[○○○◉○○○○○○]','[○○○○◉○○○○○]','[○○○○○◉○○○○]','[○○○○○○◉○○○]','[○○○○○○○◉○○]','[○○○○○○○○◉○]','[○○○○○○○○○◉]']
        self.throb_size = 12
        self.ticks = 0
        self.tick_max = 9
    
    def __str__(self):
        return self.throbber[self.ticks]
    
    def tick(self):
        if self.ticks == self.tick_max:
            self.ticks = 0
        else:
            self.ticks += 1
    
    def reset(self):
        self.ticks = 0