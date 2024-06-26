points_premise = 500
percentage_premise = 8.01
date_premise = 10

date_hypothesis = 11

# the hypothesis and premise mention the points and percentage of rally of SENSEX, and the date of the Nifty future stock trading call
if points_premise < 0 or percentage_premise < 0:
    # check if the points or percentage in the premise contradicts the assumption of rally
    label = "contradiction"
elif date_premise!= date_hypothesis:
    # check if the date in the hypothesis contradicts the date in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the points and percentage of rally
    # the date in the hypothesis is consistent with the premise, but the direction of the rally cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
