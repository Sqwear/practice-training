from datetime import datetime, timedelta

def date_in_future(days):
    if not isinstance(days, int):
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    future_date = datetime.now() + timedelta(days=days)
    return future_date.strftime('%d-%m-%Y %H:%M:%S')

print(date_in_future([])) # Текущая дата
print(date_in_future(2)) # Текущая дата + 2 дня

