cleaning_time_premise = 7
cleaning_time_hypothesis = 4

# the hypothesis talks about the cleaning time, referenced also in the premise
if cleaning_time_hypothesis >= cleaning_time_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'cleaning_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the cleaning time
    # any cleaning time less than 'cleaning_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
