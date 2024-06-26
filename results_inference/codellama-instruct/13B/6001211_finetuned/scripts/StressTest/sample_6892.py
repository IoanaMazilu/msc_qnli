cube_dimensions_premise = 3 * 5 * 5
cube_dimensions_hypothesis = 5 * 5 * 5

# the hypothesis refers to the dimensions of the cube mentioned in the premise
if cube_dimensions_hypothesis <= cube_dimensions_premise:
    # check if the dimensions of the cube in the hypothesis contradict the estimate of more than 'cube_dimensions_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the dimensions of the cube
    # any dimensions greater than 'cube_dimensions_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
