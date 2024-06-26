average_raise_premise = 2
average_raise_hypothesis = 7

# the hypothesis refers to the points Jerry needs to raise his average, also mentioned in the premise
if average_raise_premise >= average_raise_hypothesis:
    # check if the estimate of 'average_raise_premise' contradicts the points Jerry needs to raise his average in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
