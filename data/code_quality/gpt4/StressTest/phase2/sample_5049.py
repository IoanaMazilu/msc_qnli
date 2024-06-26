total_notes_premise = 80
total_notes_hypothesis = 40

# the hypothesis refers to the total number of currency notes Anitha had, which is also mentioned in the premise
if total_notes_premise <= total_notes_hypothesis:
    # check if the statement in the hypothesis contradicts the total number of notes in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
