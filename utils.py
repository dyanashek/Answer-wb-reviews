import datetime

def validate_date(current_date):
    try:
        datetime.datetime.strptime(current_date, "%d.%m.%Y")

        return True
    except:
        return False