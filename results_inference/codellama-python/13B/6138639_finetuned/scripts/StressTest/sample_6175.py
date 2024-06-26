commute_time_difference_premise = 55
commute_time_difference_hypothesis = 15

# the hypothesis talks about the difference in commute time by walking and riding the train, referenced also in the premise
if commute_time_difference_hypothesis >= commute_time_difference_premise:
    # check if the hypothesis value contradicts the estimate of less than 'commute_time_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference in commute time
    # any difference in commute time less than 'commute_time_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
