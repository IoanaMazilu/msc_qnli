average_raise_premise = 2
average_raise_hypothesis = 7

# the hypothesis refers to the points Jerry wants to raise his average by, mentioned in the premise
if average_raise_premise >= average_raise_hypothesis:
    # check if the estimate of 'average_raise_hypothesis' contradicts the number of points Jerry wants to raise his average by in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
