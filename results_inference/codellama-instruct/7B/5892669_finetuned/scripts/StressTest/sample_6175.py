commute_difference_premise = 55
commute_difference_hypothesis = 15

# the hypothesis talks about the difference in commuting times by walking and by train, referenced also in the premise
if commute_difference_hypothesis >= commute_difference_premise:
    # check if the hypothesis value contradicts the estimate of less than 'commute_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference in commuting times
    # any difference less than 'commute_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
