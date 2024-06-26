start_premise = 2
start_hypothesis = 3

# the hypothesis refers to the starting point of the route mentioned in the premise
if start_hypothesis <= start_premise:
    # check if the starting point in the hypothesis contradicts the starting point mentioned in the premise
    label = "contradiction"
else:
    # if the starting point in the hypothesis does not contradict the starting point in the premise, we can infer entailment
    label = "entailment"

print(label)
