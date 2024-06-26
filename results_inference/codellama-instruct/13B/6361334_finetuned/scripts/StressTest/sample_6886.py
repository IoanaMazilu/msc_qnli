notes_premise = 55
notes_hypothesis = 85

# the hypothesis refers to the total number of currency notes in all, mentioned in the premise
if notes_hypothesis <= notes_premise:
    # check if the estimate of 'notes_hypothesis' contradicts the number of currency notes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
