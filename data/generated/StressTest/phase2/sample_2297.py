# Premise: Susan made a block with small cubes of 5 cubic cm volume to make a block 7 small cubes long, 7 small cubes wide and 6 small cubes deep.
# Hypothesis: Susan made a block with small cubes of 1 cubic cm volume to make a block 7 small cubes long, 7 small cubes wide and 6 small cubes deep.
# Golden Label: contradiction

cube_volume_premise = 5
cube_volume_hypothesis = 1
cube_length = 7
cube_width = 7
cube_depth = 6

# the hypothesis talks about the volume of the small cubes that Susan used to make a block
# both the premise and the hypothesis mention the dimensions of the block
if cube_volume_premise != cube_volume_hypothesis:
    # check if the volume of the cube in the hypothesis contradicts the volume of the cube in the premise
    label = "contradiction"
else:
    # if the volume of the cube in the hypothesis is the same as the volume of the cube in the premise
    # then the hypothesis does not contradict the premise
    label = "neutral"

print(label)
