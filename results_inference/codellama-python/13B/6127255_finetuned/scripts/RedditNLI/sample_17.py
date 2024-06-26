points_premise = 500
percentage_premise = 8.01
date_premise = 10
day_premise = 'Tuesday'

date_hypothesis = 11
day_hypothesis = 'Wednesday'

# the hypothesis and premise mention the points and percentage rallied in SENSEX, Tata motors up and the date and day of the trading call
# the hypothesis contradicts the premise in all these aspects
if date_premise!= date_hypothesis or day_premise!= day_hypothesis:
    label = "contradiction"
elif points_premise > 0 or percentage_premise > 0:
    label = "contradiction"
else:
    label = "neutral"

print(label)
