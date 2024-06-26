side_st_premise = 50
side_tv_premise = 50
side_sv_premise = 12

side_st_hypothesis = 10
side_tv_hypothesis = 10
side_sv_hypothesis = 12

# the hypothesis refers to the lengths of the sides of the triangle, which are also mentioned in the premise
if side_st_hypothesis > side_st_premise or side_tv_hypothesis > side_tv_premise:
    # check if the hypothesis values contradict the premise estimates
    label = "contradiction"
elif side_sv_hypothesis!= side_sv_premise:
    # check if the hypothesis value for SV contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
