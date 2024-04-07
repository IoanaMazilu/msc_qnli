# Premise: Smita Was Making A Cube With Dimensions 5 * 5 * 5 Using 1 * 1 * 1 Cubes.
# Hypothesis: Smita Was Making A Cube With Dimensions more than 5 * 5 * 5 Using 1 * 1 * 1 Cubes.
# Golden Label: contradiction

cube_dimensions_premise = 5 * 5 * 5
cube_dimensions_hypothesis = 5 * 5 * 5

# the hypothesis refers to the dimensions of the cube Smita was making which is also mentioned in the premise
if cube_dimensions_hypothesis > cube_dimensions_premise:
    # check if the dimensions given in the hypothesis contradict the dimensions given in the premise
    label = "contradiction"
elif cube_dimensions_hypothesis == cube_dimensions_premise:
    # the premise gives exact dimensions for the cube
    # if the hypothesis gives the exact same dimensions, we can infer entailment
    label = "entailment"
else:
    # if the dimensions given in the hypothesis do not contradict the dimensions given in the premise, but is not the same either, we infer neutral
    label = "neutral"

print(label)

