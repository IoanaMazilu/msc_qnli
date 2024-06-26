driving_rate_premise = 100
driving_rate_hypothesis = 100

# the hypothesis refers to the driving rate of Molly and Max mentioned in the premise
if driving_rate_hypothesis >= driving_rate_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
