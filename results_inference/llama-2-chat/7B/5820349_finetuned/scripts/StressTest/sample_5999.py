min_lists_premise = 1/4
min_lists_hypothesis = 6/4

# the hypothesis refers to the minimum number of lists that a film must appear in, mentioned in the premise
if min_lists_hypothesis!= min_lists_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
