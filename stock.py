class Stock:
    def __init__(self, code, name, date, open, high, close, low, volume, p_change, dict):
        self.code = code
        self.name = name
        self.date = date
        self.open = open
        self.high = high
        self.close = close
        self.low = low
        self.volume = volume
        self.p_change = p_change
        self.c_name = dict[code]
