# Premise: Susan made a block with small cubes of 8 cubic cm volume to make a block, 3 small cubes long, 9 small cubes wide and 5 small cubes deep.
# Hypothesis: Susan made a block with small cubes of more than 6 cubic cm volume to make a block, 3 small cubes long, 9 small cubes wide and 5 small cubes deep.
# Golden Label: entailment

volume_small_cubes_premise = 8
volume_small_cubes_hypothesis = 6
length_small_cubes_premise = 3
length_small_cubes_hypothesis = 3
width_small_cubes_premise = 9
width_small_cubes_hypothesis = 9
depth_small_cubes_premise = 5
depth_small_cubes_hypothesis = 5

# the hypothesis refers to the volume and dimensions of the small cubes and block mentioned in the premise
if volume_small_cubes_premise <= volume_small_cubes_hypothesis:
    # check if the estimate of 'volume_small_cubes_hypothesis' contradicts the volume of small cubes in the premise
    label = "contradiction"
elif length_small_cubes_hypothesis != length_small_cubes_premise or width_small_cubes_hypothesis != width_small_cubes_premise or depth_small_cubes_hypothesis != depth_small_cubes_premise:
    # check if the dimensions of the block in the hypothesis contradicts the dimensions of the block reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

