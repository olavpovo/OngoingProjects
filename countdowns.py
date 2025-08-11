from datetime import date,timedelta
today=date.today()
days=date(2024,12,23)-date.today()
christmas=date(2024,12,25)-date.today()
bday=date(2025,1,24)-today
vacation=today-date(2024,11,18)
print(f"Mom's return: {days.days} days")
nextVacay=(date(2024,11,18)+timedelta(days=180))-date.today()
print(f"Christmas: {christmas.days} days")
print(f"39th bday: {bday.days} days")
print(f"Time since last vacation: {vacation.days} days")
print(f"Time until next vacation: {nextVacay.days} days ")