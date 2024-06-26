notes_premise = 42
notes_hypothesis = 52

# the hypothesis refers to the number of notes carried by Donald mentioned in the premise
if notes_premise >= notes_hypothesis:
    # check if the estimate of 'notes_hypothesis' contradicts the number of notes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
