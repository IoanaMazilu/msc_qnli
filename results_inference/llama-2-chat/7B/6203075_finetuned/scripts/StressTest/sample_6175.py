commute_time_premise = 55
commute_time_hypothesis = 15

# the hypothesis talks about the difference in commute times by walking and train, which is also mentioned in the premise
if commute_time_hypothesis >= commute_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'commute_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference in commute times
    # any difference less than 'commute_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
