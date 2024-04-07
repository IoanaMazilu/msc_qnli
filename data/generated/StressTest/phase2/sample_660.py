# Premise: Rosy is 40% more efficient than Mary.
# Hypothesis: Rosy is more than 30% more efficient than Mary.
# Golden Label: entailment

efficiency_premise = 40
efficiency_hypothesis = 30

# the hypothesis refers to the efficiency difference between Rosy and Mary mentioned in the premise
if efficiency_premise <= efficiency_hypothesis:
    # check if the hypothesis' estimate contradicts the efficiency difference in the premise
    label = "contradiction"
else:
    # if the hypothesis' estimate doesn't contradict the premise's one, we can infer entailment
    label = "entailment"

print(label)

