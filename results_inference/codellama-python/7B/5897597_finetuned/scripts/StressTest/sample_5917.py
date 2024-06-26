average_increase_premise = 7
average_increase_hypothesis = 2

# the hypothesis talks about the increase in average Jerry wants to achieve, referenced also in the premise
if average_increase_hypothesis >= average_increase_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_increase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the increase in average
    # any increase less than 'average_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
