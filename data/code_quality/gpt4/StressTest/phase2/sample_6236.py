cleaning_time_premise = 3
cleaning_time_hypothesis = 3

# the hypothesis refers to the cleaning time at doubled speed, mentioned in the premise
if cleaning_time_hypothesis >= cleaning_time_premise:
    # check if the hypothesis value contradicts the estimate of 'cleaning_time_premise'
    label = "contradiction"
else:
    # the premise gives an exact time needed for cleaning at doubled speed
    # cleaning time less than 'cleaning_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
