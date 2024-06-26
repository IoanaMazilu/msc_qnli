friend_count_premise = 6
combination_premise = 2
combination_hypothesis = 1

# the hypothesis refers to the number of combinations formed from John's friends mentioned in the premise
if combination_premise <= combination_hypothesis:
    # check if the hypothesis value contradicts the number of combinations in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimate do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
