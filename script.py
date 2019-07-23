import codecademylib
import numpy as np
from matplotlib import pyplot as plt


survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

#Calculate no of people who voted Ceballos in survey
total_ceballos = sum([1 for e in survey_responses if e == 'Ceballos'])
print("Voted Ceballos: "+str(total_ceballos))

total = float(len(survey_responses))
print("Total Number of Votes: "+str(total))

#Calcluate percentage who voted Ceballos in survey
percentage_ceballos = 100*total_ceballos/total
print("Percentage Who Voted Ceballos: "+str(percentage_ceballos)+str('%')) 

#Plot the binomial histogram
possible_surveys = np.random.binomial(total, 0.54, 10000) / total
plt.hist(possible_surveys, range=(0, 1), bins=20)
plt.show()

#Probability that ceballos would get less than 50% of the total vote
ceballos_loss_surveys = np.mean(possible_surveys<0.5) 
print(ceballos_loss_surveys)

#Generate a larger survey
large_survey_length = float(7000)
large_survey = np.random.binomial(large_survey_length, 0.54, 10000) / large_survey_length
plt.hist(large_survey, range=(0, 1), bins=20)
plt.show()

#New loss survey
ceballos_loss_new = np.mean(large_survey<0.5)
print(ceballos_loss_new) 