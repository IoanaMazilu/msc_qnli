# the hypothesis refers to the time it takes for Mary to complete a task alone
if hypothesis_days <= premise_days:
    # check if the estimate of 'hypothesis_days' contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
