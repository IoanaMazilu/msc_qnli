cube_dimensions_premise = 5 * 5 * 5
cube_dimensions_hypothesis = 1 * 1 * 1

# the hypothesis refers to the dimensions of the cube made by Smita
if cube_dimensions_hypothesis > cube_dimensions_premise:
    # the hypothesis contradicts the premise, as the premise only mentions a 5x5x5 cube
    label = "contradiction"
elif cube_dimensions_hypothesis == cube_dimensions_premise:
    # the hypothesis is neutral, as it does not provide any new information about the dimensions of the cube
    label = "neutral"
else:
    # the premise only mentions a 5x5x5 cube, so any larger cube contradicts the premise
    label = "contradiction"

print(label)
