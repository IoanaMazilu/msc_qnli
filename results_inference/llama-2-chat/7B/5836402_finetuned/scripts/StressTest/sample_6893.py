cube_dim_premise = 5
cube_dim_hypothesis = 5
cube_dim_hypothesis_expansion = 5

# the hypothesis refers to the dimensions of the cube Smita was making
# compute the maximum dimensions of the cube in the hypothesis
max_dim_hypothesis = cube_dim_hypothesis_expansion

# the premise gives the dimensions of the cube
# if the dimensions in the hypothesis are less than the premise, it contradicts
if cube_dim_hypothesis < cube_dim_premise:
    label = "contradiction"
else:
    # if the dimensions in the hypothesis are greater or equal to the premise, we can infer entailment
    label = "entailment"

print(label)
