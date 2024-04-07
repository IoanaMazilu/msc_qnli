# Premise: Susan made a block with small cubes of more than 3 cubic cm volume to make a block 7 small cubes long, 7 small cubes wide and 6 small cubes deep.
# Hypothesis: Susan made a block with small cubes of 5 cubic cm volume to make a block 7 small cubes long, 7 small cubes wide and 6 small cubes deep.
# Golden Label: neutral

cube_volume_premise = 3
cube_volume_hypothesis = 5
cubes_long = 7
cubes_wide = 7
cubes_deep = 6

# the hypothesis refers to the volume of the small cubes and the dimensions of the block mentioned in the premise
if cube_volume_hypothesis <= cube_volume_premise:
    # check if the hypothesis value contradicts the estimate of more than 'cube_volume_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the volume of the small cubes
    # any cube volume greater than 'cube_volume_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
