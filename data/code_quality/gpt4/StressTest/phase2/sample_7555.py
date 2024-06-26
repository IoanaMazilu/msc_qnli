clean_time_premise = 1
clean_time_hypothesis = 6

# the hypothesis refers to the time Jim needs to clean the house, also mentioned in the premise
if clean_time_hypothesis <= clean_time_premise:
    # check if the time in the hypothesis contradicts the estimate of more than 'clean_time_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the cleaning time
    # any cleaning time greater than 'clean_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
