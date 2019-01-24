# Import packages
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


# Get data from csv and put dates into a list
sheet = pd.read_csv('Climbing 100x - 2018.csv')
climbing_dates = [] 
for date in sheet['Date'].tolist():
    climbing_dates.append(datetime.strptime(date, '%Y-%m-%d'))

# Make 2018_days list with all dates of 2018

date1 = '1-1-2018'
date2 = '12-31-2018'
year_dates = pd.date_range(date1, date2).tolist()

# Make list of cumulative climb count
climb_count = []
total = 0
for date in year_dates:
    if date in climbing_dates:
        total +=1
        climb_count.append(total)
    else:
        climb_count.append(total)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
         ]


# Graph cumulative climb count
plt.plot(year_dates, climb_count, label = 'My Progress')
plt.plot([year_dates[0], year_dates[-1]], [0, 100], 
         label = 'Climbing Rate to Realize Goal', color = 'red')

plt.axvline(datetime.strptime('2018-04-28', '%Y-%m-%d'), dashes=[1,1], 
            label = '4/28/18-5/8/18 Korea Trip', color ='green')
plt.axvline(datetime.strptime('2018-05-8', '%Y-%m-%d'), dashes=[1,1],
            color = 'green')
plt.axvline(datetime.strptime('2018-09-7', '%Y-%m-%d'), dashes=[1,1],
            label = '9/7/18-9/18/18 Denmark Trip', color = 'purple')
plt.axvline(datetime.strptime('2018-09-16', '%Y-%m-%d'), dashes=[1,1],
            color = 'purple')
plt.xlabel('Date')
plt.ylabel('Times Climbing')
plt.title('Climbing 100x in 2018')
plt.legend()
plt.show()
