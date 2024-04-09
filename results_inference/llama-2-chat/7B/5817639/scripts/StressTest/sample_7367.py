rate_premise = 7
rate_hypothesis = 3

# the premise gives the rate of walking in miles per hour, and the hypothesis gives a different rate
if rate_hypothesis <= rate_premise:
    # check if the hypothesis rate contradicts the premise rate
    label = "contradiction"
else:
    # the hypothesis rate does not contradict the premise rate, so we can infer entailment
    label = "entailment"

print(label)
