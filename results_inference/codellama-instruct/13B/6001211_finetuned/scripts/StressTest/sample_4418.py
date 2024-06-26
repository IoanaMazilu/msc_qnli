average_raise_premise = 2
average_raise_hypothesis = 5

# the hypothesis refers to the points Jerry wants to raise his average by, mentioned in the premise
if average_raise_premise!= average_raise_hypothesis:
    # check if the points Jerry wants to raise his average by in the hypothesis contradicts the points mentioned in the premise
    label = "contradiction"
else:
    # if the points Jerry wants to raise his average by in the hypothesis does not contradict the points mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)
