st_premise = 10
tv_premise = 10
sv_premise = 12
st_hypothesis = 70
tv_hypothesis = 70
sv_hypothesis = 12

# the hypothesis refers to the sides of a triangle mentioned in the premise
if st_hypothesis + tv_hypothesis < sv_hypothesis:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives the exact values of the sides of the triangle
    # any values for the sides of the triangle in the hypothesis that do not contradict the premise cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
