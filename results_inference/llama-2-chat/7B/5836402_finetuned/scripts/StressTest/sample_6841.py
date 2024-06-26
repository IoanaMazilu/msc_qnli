investment_premise = 20000
investment_hypothesis = 20000
duration_premise = 7
duration_hypothesis = 6

# the hypothesis refers to the same investment amount and duration mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the investment amount in the hypothesis contradicts the investment amount reported in the premise
    label = "contradiction"
elif duration_hypothesis!= duration_premise:
    # check if the duration in the hypothesis contradicts the duration reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
