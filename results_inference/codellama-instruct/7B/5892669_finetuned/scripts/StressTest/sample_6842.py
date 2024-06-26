investment_premise = 20000
investment_hypothesis = 20000
investment_time_premise = 6
investment_time_hypothesis = 6

# the hypothesis refers to the amount and time of Rick's investment mentioned in the premise
if investment_premise!= investment_hypothesis:
    # check if the investment amount in the hypothesis contradicts the investment amount reported in the premise
    label = "contradiction"
elif investment_time_hypothesis <= investment_time_premise:
    # check if the investment time in the hypothesis contradicts the investment time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
