#Jonathan Leventhal
#CS21 Exam Practice

#tuition = $8000/semester
#tuition increases by 3%/year for 5 years
#display projected semester tuition for the next 5 years

#start of program
TUITION = 8000
yearly_tuition = TUITION*2
year = 0

for i in range(5):
	year+=1
	yearly_tuition = yearly_tuition + (yearly_tuition * .03)
	print('Year',year,'tuition is $',format(yearly_tuition,'.2f'))
	




