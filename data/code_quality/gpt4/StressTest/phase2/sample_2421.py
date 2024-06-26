notes_donald_premise = 30
notes_donald_hypothesis = 40

# the hypothesis refers to the number of notes Donald is carrying, which is also mentioned in the premise
if notes_donald_hypothesis <= notes_donald_premise:
    # check if the hypothesis value contradicts the exact number of notes 'notes_donald_premise'
    label = "contradiction"
elif notes_donald_hypothesis > notes_donald_premise:
    # check if the number of notes in the hypothesis contradicts the number of notes reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)