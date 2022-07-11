class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def extract_data(cls, date_str):
        return tuple(map(int, date_str.split('-')))

    @staticmethod
    def validate(date_str):
        dd, mm, yy = Date.extract_data(date_str)
        if 1 <= dd <= 31 and 1 <= mm <= 12:
            return True
        return False


print(Date.extract_data('08-04-2003'))
print(Date.validate('17-06-2005'))
print(Date.validate('17-26-2005'))