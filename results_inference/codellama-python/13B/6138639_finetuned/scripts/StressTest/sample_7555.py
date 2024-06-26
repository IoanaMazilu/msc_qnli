cleaning_time_premise = 1
cleaning_time_hypothesis = 6

# the hypothesis talks about the time Jim takes to clean the house, referenced also in the premise
if cleaning_time_hypothesis <= cleaning_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'cleaning_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the cleaning time
    # any cleaning time greater than 'cleaning_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
