side_ST_premise = 10
side_TV_premise = 10
side_SV_premise = 12

side_ST_hypothesis = 70
side_TV_hypothesis = 70
side_SV_hypothesis = 12

# the hypothesis refers to the lengths of sides ST, TV and SV of the same triangle mentioned in the premise
if side_ST_hypothesis!= side_ST_premise or side_TV_hypothesis!= side_TV_premise:
    # check if the lengths of sides ST or TV in the hypothesis contradict the lengths of sides ST or TV reported in the premise
    label = "contradiction"
elif side_SV_hypothesis!= side_SV_premise:
    # check if the length of side SV in the hypothesis contradicts the length of side SV reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
