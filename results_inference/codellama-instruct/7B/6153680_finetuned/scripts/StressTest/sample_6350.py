investment_premise = 90000
investment_hypothesis = 90000

# the hypothesis mentions a specific investment amount, which is also mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
