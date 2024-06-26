# define variables with representative names for the numerical entities in both inputs
angel_scores_premise = [less_than_7, 2, 3, 4]
angel_scores_hypothesis = [1, 2, 3, 4]

# extract all quantities as valid numbers (integers or floats)
less_than_7_premise = min(angel_scores_premise)
less_than_7_hypothesis = min(angel_scores_hypothesis)

# compare the variables
if less_than_7_premise <= less_than_7_hypothesis:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif any(score not in angel_scores_hypothesis for score in angel_scores_premise):
    # the premise value is not consistent with the hypothesis value
    label = "contradiction"
else:
    # the hypothesis value is consistent with the premise value
    label = "entailment"

print(label)
