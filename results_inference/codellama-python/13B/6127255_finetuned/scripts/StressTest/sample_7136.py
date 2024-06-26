#side_ST_TV_premise = 10
#side_ST_TV_hypothesis = 70
#side_SV_premise = 12
#side_SV_hypothesis = 12

# the hypothesis refers to the sides of the same triangle mentioned in the premise
# if the lengths of sides ST and TV in the hypothesis contradict the lengths mentioned in the premise
if side_ST_TV_hypothesis!= side_ST_TV_premise:
    label = "contradiction"
# if the length of side SV in the hypothesis is the same as in the premise
elif side_SV_hypothesis == side_SV_premise:
    # then the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # if the lengths of sides ST and TV in the hypothesis do not contradict the lengths mentioned in the premise
    # and the length of side SV in the hypothesis is not the same as in the premise
    label = "neutral"

print(label)
#