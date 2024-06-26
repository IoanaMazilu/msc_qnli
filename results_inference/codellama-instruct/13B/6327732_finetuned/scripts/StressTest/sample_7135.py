side_st_premise = 50
side_tv_premise = 50
side_sv_premise = 12

side_st_hypothesis = 10
side_tv_hypothesis = 10
side_sv_hypothesis = 12

# the hypothesis refers to the sides of the triangle, which are mentioned in the premise
if side_st_hypothesis <= side_st_premise and side_tv_hypothesis <= side_tv_premise:
    # check if the hypothesis values contradict the estimates of the premise
    label = "contradiction"
else:
    # the premise gives estimates for the sides of the triangle
    # any values of the sides greater than the estimates are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
