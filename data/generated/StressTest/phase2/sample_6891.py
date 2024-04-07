# Premise: Smita Was Making A Cube With Dimensions 5 * 5 * 5 Using 1 * 1 * 1 Cubes.
# Hypothesis: Smita Was Making A Cube With Dimensions more than 3 * 5 * 5 Using 1 * 1 * 1 Cubes.
# Golden Label: entailment

cube_dimensions_premise = 5
cube_dimensions_hypothesis = 3

# the hypothesis refers to the dimension of the cube mentioned in the premise
if cube_dimensions_premise <= cube_dimensions_hypothesis:
    # check if the 'cube_dimensions_hypothesis' contradicts the dimension of the cube in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
