money_premise = 248
money_hypothesis = 548

# the hypothesis refers to the amount of money in Marie's account mentioned in the premise
if money_premise >= money_hypothesis:
    # check if the amount of money in the premise contradicts the estimate of less than'money_hypothesis'
    label = "contradiction"
else:
    # if the premise amount does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
