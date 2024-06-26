miles_walked_premise = 4
miles_walked_hypothesis = 8
time_walked = 1.25 # 1 hour and 15 minutes converted to hours

# the hypothesis refers to the distance and time of walking mentioned in the premise
if miles_walked_hypothesis <= miles_walked_premise:
    # check if the distance walked in the hypothesis contradicts the estimate of more than 'miles_walked_premise' in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance walked
    # any distance greater than 'miles_walked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
