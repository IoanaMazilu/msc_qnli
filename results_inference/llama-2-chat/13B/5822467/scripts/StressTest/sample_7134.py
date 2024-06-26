side_st_premise = 10
side_tv_premise = 10
side_sv_premise = 12

# the hypothesis talks about the sides of the triangle, referenced also in the premise
if side_st_hypothesis <= 50 and side_tv_hypothesis <= 50 and side_sv_hypothesis == 12:
    # check if the hypothesis values contradict the estimate of the sides of the triangle in the premise
    label = "contradiction"
elif side_st_hypothesis > 50 or side_tv_hypothesis > 50 or side_sv_hypothesis!= 12:
    # check if the hypothesis values contradict the estimate of the sides of the triangle in the premise
    label = "contradiction"
else:
    # the premise gives specific values for the sides of the triangle
    # any values that satisfy the hypothesis and are consistent with the premise, cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
