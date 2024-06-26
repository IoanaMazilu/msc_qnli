ratio_ab_bc_premise = 6/3
ratio_ab_bc_hypothesis = 2/3

# the hypothesis refers to the ratio of distances between A to B and B to C 
if ratio_ab_bc_hypothesis >= ratio_ab_bc_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio less than 'ratio_ab_bc_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
