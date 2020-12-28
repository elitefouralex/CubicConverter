# ci = liters * 61.02
# liters = ci / 61.02

def youfuckedup():
	print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You done messed up A-A-RON!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

while True:
	ci_or_liter = input("""
Here we will be converting engine sizes to and from cubic inches and liters.
	
Which unit of measurement would you like to convert from? CI or L: """)
	
	if ci_or_liter in ("CI", "ci", "Cubic Inches", "cubic inches", "cubic inch", "Cubic Inch"):
		ci_amount = float(input("""
How many cubic inches would you like to convert?: """))
		ci_output = ci_amount / 61.02
		print(f"\n{ci_amount} equals {ci_output:.2f} liters.")
		break
		if ci_amount is not 
			continue
	elif ci_or_liter in ("L", "l", "Liters", "Litres", "Liter","Litre", "liters", "litres", "liter", "litre"):
		L_amount = float(input("""
How many liters would you like to convert to cubic inches?: """))
		L_output = L_amount * 61.02
		#L_output with the colon dot 2 F rounds output of f string variable to 2 decimal places
		print(f"\n{L_amount} is equal to {L_output:.2f}")
		break	
	else:
		youfuckedup()
print("\nThanks for using my code!")


