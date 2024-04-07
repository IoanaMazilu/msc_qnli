# Premise: Meg and Bob are among the 8 participants in a cycling race.
# Hypothesis: Meg and Bob are among the more than 3 participants in a cycling race.
# Golden Label: entailment

participants_premise = 8
participants_hypothesis = 3

# the hypothesis talks about the number of participants in a cycling race, referenced also in the premise
if participants_premise <= participants_hypothesis:
    # check if the number of participants in the premise contradicts the estimate of more than 'participants_hypothesis'
    label = "contradiction"
elif participants_hypothesis > participants_premise:
    # check if the number of participants in the hypothesis contradicts the number of participants reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

