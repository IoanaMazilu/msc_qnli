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
