average_increase_premise = 2
average_increase_hypothesis = 5

# the hypothesis talks about the increase in average points Jerry wants to, referenced also in the premise
if average_increase_hypothesis < average_increase_premise:
    # check if the hypothesis value contradicts the estimate of 'average_increase_premise' points
    label = "contradiction"
elif average_increase_hypothesis > average_increase_premise:
    # the premise gives only an estimate for the increase in average points
    # any increase in average points greater than 'average_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
