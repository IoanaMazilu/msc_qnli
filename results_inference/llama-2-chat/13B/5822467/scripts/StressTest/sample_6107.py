age_premise = 32
age_hypothesis = 35
stop_babysitting_premise = 12

# the hypothesis refers to the current age and the time when Jane stopped baby-sitting
if age_hypothesis > age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the premise value
    label = "contradiction"
elif stop_babysitting_hypothesis!= stop_babysitting_premise:
    # check if the time when Jane stopped baby-sitting in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
