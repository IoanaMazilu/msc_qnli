notes_carried_premise = 30
notes_carried_hypothesis = 20

# the hypothesis refers to the number of notes carried by Donald mentioned in the premise
if notes_carried_hypothesis != notes_carried_premise:
    # check if the number of notes in the hypothesis contradicts the number of notes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
