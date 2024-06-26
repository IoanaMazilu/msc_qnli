rate_premise = 3.9
rate_hypothesis = 3.9

# the hypothesis and premise mention the unemployment rate
if rate_hypothesis!= rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
