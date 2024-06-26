investment_premise = 20000
investment_hypothesis = 20000
months_premise = 6
months_hypothesis = 7

# the hypothesis refers to the same investment and time period mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the investment amount in the hypothesis contradicts the investment amount reported in the premise
    label = "contradiction"
elif months_hypothesis <= months_premise:
    # check if the time period in the hypothesis contradicts the time period reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
