participants_premise = 3
participants_hypothesis = 2

# the hypothesis refers to the number of participants in a race, mentioned also in the premise
if participants_premise <= participants_hypothesis:
    # check if the number of participants in the hypothesis contradicts the number of participants reported in the premise
    label = "contradiction"
else:
    # if the number of participants in the hypothesis does not contradict the premise's number of participants, we can infer entailment
    label = "entailment"

print(label)
