
import math 
amount=0.0


principal=int(input("Enter principal\n"))

rate = 0.05
print("Year amount on deposit")
for year in range (1,11):
  amount=principal* pow(1+rate,year)
  print("%4d% 20.2f\n"%( year ,amount))	
	

