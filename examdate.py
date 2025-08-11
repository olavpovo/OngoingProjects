from datetime import date,timedelta

left=int(input("Exercises left:"))

dayChoice=input("Today or tomorrow? (answer -> '2' or 'tm'): ")

if dayChoice == "2":
	measure=date.today()
elif dayChoice == "tm":
	measure=date.today()+timedelta(days=1)

early=date(2024,12,12)
exam=date(2024,12,14)

daysLeft=exam-measure
complete=early-measure


	


print(f"\nDays until exam (Dec 14th): {daysLeft.days} days",f"Days to goal: {complete.days} days",f"\nDaily pace required: {left/complete.days:.02f}", sep="\n")
