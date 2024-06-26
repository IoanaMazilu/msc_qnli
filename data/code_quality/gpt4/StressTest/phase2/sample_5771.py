notes_premise = 39
notes_hypothesis = 79

# the hypothesis refers to the number of notes Donald carries, also mentioned in the premise
if notes_premise != notes_hypothesis:
    # check if the number of notes in the hypothesis contradicts the number of notes mentioned in the premise
    label = "contradiction"
else:
    # if the number of notes in the hypothesis does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
