average_raise_premise = 2
average_raise_hypothesis = 5

# the hypothesis refers to the points Jerry wants to raise his average by, which is also mentioned in the premise
if average_raise_hypothesis!= average_raise_premise:
    # check if the desired points to raise the average in the hypothesis contradicts the desired points in the premise
    label = "contradiction"
else:
    # if the desired points to raise the average in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
