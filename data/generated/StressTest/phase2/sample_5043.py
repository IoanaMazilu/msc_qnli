# Premise: Meg and Bob are among the 4 participants in a cycling race.
# Hypothesis: Meg and Bob are among the more than 2 participants in a cycling race.
# Golden Label: entailment

participants_premise = 4
participants_hypothesis = 2

# the hypothesis refers to the number of participants in a cycling race mentioned in the premise
if participants_premise <= participants_hypothesis:
    # check if the estimate of 'participants_hypothesis' contradicts the number of participants in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

