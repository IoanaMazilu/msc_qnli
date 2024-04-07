# Premise: Susan made a block with small cubes of more than 6 cubic cm volume to make a block, 3 small cubes long, 9 small cubes wide and 5 small cubes deep.
# Hypothesis: Susan made a block with small cubes of 8 cubic cm volume to make a block, 3 small cubes long, 9 small cubes wide and 5 small cubes deep.
# Golden Label: neutral

cube_volume_premise = 6
cube_volume_hypothesis = 8

# the hypothesis refers to the volume of the small cubes used to make the block
if cube_volume_hypothesis <= cube_volume_premise:
    # check if the volume of the small cube in the hypothesis contradicts the estimate of more than 'cube_volume_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the volume of the small cubes
    # any volume greater than 'cube_volume_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

