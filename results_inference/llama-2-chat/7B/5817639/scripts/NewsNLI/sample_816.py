opposition_premise = 0.62
opposition_hypothesis = 0.63

# the hypothesis mentions a higher percentage of disapproval than the premise
if opposition_hypothesis!= opposition_premise:
    # check if the percentage of disapproval in the hypothesis contradicts the percentage of disapproval in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
