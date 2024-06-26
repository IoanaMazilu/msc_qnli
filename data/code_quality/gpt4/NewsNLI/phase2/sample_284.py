spent_premise = 1000000
spent_hypothesis = 1000000

# the hypothesis mentions a sum that has been spent, which is also mentioned in the premise
if spent_hypothesis != spent_premise:
    # check if the amount spent in the hypothesis contradicts the amount spent reported in the premise
    label = "contradiction"
else:
    # if the amount spent in the hypothesis does not contradict the amount spent in the premise, we can infer entailment
    label = "entailment"

print(label)
