cube_dimensions_premise = 3 * 5 * 5
cube_dimensions_hypothesis = 5 * 5 * 5
cube_units_premise = 1 * 1 * 1
cube_units_hypothesis = 1 * 1 * 1

# the hypothesis talks about the dimensions of a cube and the units used, both mentioned in the premise
if cube_dimensions_hypothesis == cube_dimensions_premise:
    # the hypothesis and premise have the same value, so there is no contradiction or entailment
    label = "neutral"
elif cube_dimensions_hypothesis > cube_dimensions_premise:
    # the hypothesis dimension is greater than the premise dimension, so there is entailment
    label = "entailment"
else:
    # the hypothesis dimension is less than or equal to the premise dimension, so there is contradiction
    label = "contradiction"

print(label)
