years_premise = 5
years_hypothesis = 8

# the hypothesis refers to the same situation as the premise, but estimates a different time until John will be twice as old as Frank
if years_hypothesis < years_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
