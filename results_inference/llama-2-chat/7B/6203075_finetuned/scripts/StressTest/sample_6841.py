investment_premise = 20000
investment_hypothesis = 20000
duration_premise = 7
duration_hypothesis = 6

# the hypothesis talks about the investment amount and duration, which are also mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the investment amount in the hypothesis contradicts the investment amount in the premise
    label = "contradiction"
elif duration_hypothesis!= duration_premise:
    # check if the duration in the hypothesis contradicts the duration in the premise
    label = "contradiction"
else:
    # if the hypothesis values and durations do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
