participants_premise = 4
participants_hypothesis = 1

# both the premise and hypothesis talk about the number of participants in a cycling race
if participants_premise <= participants_hypothesis:
    # check if the number of participants in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the number of participants in the premise is more than the one in the hypothesis,
    # we can infer entailment as the premise explicitly states the number of participants
    label = "entailment"

print(label)
