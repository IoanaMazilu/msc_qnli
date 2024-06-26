quarters_premise = 100.0 + 783.0
quarters_borrowed = 271.0
quarters_now = quarters_premise - quarters_borrowed

# the hypothesis refers to the number of quarters Sara has now
if quarters_now!= quarters_premise:
    # check if the number of quarters in the hypothesis contradicts the number of quarters in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
