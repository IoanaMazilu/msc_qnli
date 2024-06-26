# define variables for each side of the triangle
side_BC_premise = 3
side_BC_hypothesis = 7
side_CA_premise = 4
side_CA_hypothesis = 4
side_AB_premise = 5
side_AB_hypothesis = 5

# check if the hypothesis values contradict the premise ones
if side_BC_hypothesis!= side_BC_premise or side_CA_hypothesis!= side_CA_premise or side_AB_hypothesis!= side_AB_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
