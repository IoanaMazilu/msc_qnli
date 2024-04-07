# Premise: Adam sat with his friends in the Chinnaswamy stadium at Madurai to watch the 100 metres running race organized by the Asian athletics Association.
# Hypothesis: Adam sat with his friends in the Chinnaswamy stadium at Madurai to watch the less than 700 metres running race organized by the Asian athletics Association.
# Golden Label: entailment

race_length_premise = 100
race_length_hypothesis = 700

# the hypothesis refers to the length of the running race mentioned in the premise
if race_length_hypothesis < race_length_premise:
    # check if the hypothesis length contradicts the race length in the premise
    label = "contradiction"
elif race_length_hypothesis > race_length_premise:
    # the premise gives an exact length for the race
    # any race length less than 'race_length_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

