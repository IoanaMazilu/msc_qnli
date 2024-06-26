investment_premise = 20000
investment_hypothesis = 20000
investment_time_premise = 6
investment_time_hypothesis = 7

# the hypothesis refers to the amount and time of investment mentioned in the premise
if investment_premise!= investment_hypothesis:
    # check if the amount of investment in the hypothesis contradicts the amount of investment in the premise
    label = "contradiction"
elif investment_time_premise >= investment_time_hypothesis:
    # check if the time of investment in the hypothesis contradicts the time of investment in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
