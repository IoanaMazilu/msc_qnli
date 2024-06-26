cleaning_time_premise = 2
cleaning_time_hypothesis = 4

# the hypothesis talks about the time Bruce and Anne need to clean their house, a time also mentioned in the premise
if cleaning_time_hypothesis <= cleaning_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'cleaning_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time greater than 'cleaning_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
