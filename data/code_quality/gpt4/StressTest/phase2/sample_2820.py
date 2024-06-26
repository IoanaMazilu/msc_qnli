participants_premise = 6
participants_hypothesis = 3

# the hypothesis refers to the number of participants in a cycling race mentioned in the premise
if participants_premise <= participants_hypothesis:
    # check if the number of participants in the hypothesis contradicts the number of participants reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
