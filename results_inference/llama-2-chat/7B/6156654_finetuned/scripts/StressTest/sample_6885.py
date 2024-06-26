notes_premise = 85
notes_hypothesis = 55

# the hypothesis refers to the number of currency notes, which is also mentioned in the premise
if notes_hypothesis <= notes_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
