# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
data[10]

np.shape(data)

new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((data,new_record), axis = 0)

np.shape(census)

age = census[:,0]
print(age)

max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age, dtype=np.float64)
age_std = np.std(age, dtype=np.float64)
print(max_age)
print(min_age)
print(round(age_mean,2))
print(round(age_std,2))

race_0 = census[census[:,2]==0]
print(race_0)

race_1 = census[census[:,2]==1]
print(race_1)

race_2 = census[census[:,2]==2]
print(race_2)

race_3 = census[census[:,2]==3]
print(race_3)

race_4 = census[census[:,2]==4]
print(race_4)


len_0 = len(race_0)
print(len_0)

len_1 = len(race_1)
print(len_1)

len_2 = len(race_2)
print(len_2)

len_3 = len(race_3)
print(len_3)

len_4 = len(race_4)
print(len_4)

minority_race = np.min(np.array([len_0,len_1,len_2,len_3,len_3,len_4]))
print(minority_race)

senior_citizens = census[census[:,0]>60]
print(senior_citizens)

working_hours_sum = sum(senior_citizens[:,6])
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = (working_hours_sum/senior_citizens_len)
print(round(avg_working_hours,2))


high = census[census[:,1]>10]
print(high)

low = census[census[:,1]<=10]
print(low)

avg_pay_high = np.mean(high[:,7])
print(round(avg_pay_high,2))

avg_pay_low = np.mean(low[:,7])
print(round(avg_pay_low,2))


np.array_equal(avg_pay_high, avg_pay_low)



