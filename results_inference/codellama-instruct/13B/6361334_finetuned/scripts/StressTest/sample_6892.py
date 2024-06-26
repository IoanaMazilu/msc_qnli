cube_dimensions_premise = 3 * 5 * 5
cube_dimensions_hypothesis = 5 * 5 * 5

# the hypothesis refers to the dimensions of the cube mentioned in the premise
if cube_dimensions_premise <= cube_dimensions_hypothesis:
    # check if the estimate of 'cube_dimensions_hypothesis' contradicts the dimensions of the cube in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the dimensions of the cube
    # any dimensions greater than 'cube_dimensions_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
