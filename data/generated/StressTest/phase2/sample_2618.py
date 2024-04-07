# Premise: Susan made a block with small cubes of 8 cubic cm volume to make a block, 3 small cubes long, 9 small cubes wide and 5 small cubes deep.
# Hypothesis: Susan made a block with small cubes of more than 8 cubic cm volume to make a block, 3 small cubes long, 9 small cubes wide and 5 small cubes deep.
# Golden Label: contradiction

cube_volume_premise = 8
cube_volume_hypothesis = 8
cubes_long = 3
cubes_wide = 9
cubes_deep = 5

# the hypothesis refers to the same block and cubes mentioned in the premise
if cube_volume_hypothesis <= cube_volume_premise:
    # check if the hypothesis estimate contradicts the cube volume in the premise
    label = "contradiction"
else:
    # if the cube volume in the hypothesis does not contradict the premise, we infer entailment
    label = "entailment"

print(label)

