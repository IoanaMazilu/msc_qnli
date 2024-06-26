rate_premise = 7.8
rate_hypothesis = 7.8

# the hypothesis and premise mention the same unemployment rate
if rate_hypothesis!= rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the unemployment rate in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
