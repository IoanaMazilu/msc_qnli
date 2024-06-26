#side_ST_TV_premise = 26
#side_ST_TV_hypothesis = 66
#side_SV_premise = 20
#side_SV_hypothesis = 20

# the hypothesis refers to the sides of the triangle mentioned in the premise
# if the length of sides ST and TV in the hypothesis is more than the length mentioned in the premise, it contradicts the premise
# if the length of side SV in the hypothesis is not equal to the length mentioned in the premise, it contradicts the premise
if side_ST_TV_premise > side_ST_TV_hypothesis:
    label = "contradiction"
elif side_SV_premise!= side_SV_hypothesis:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
#