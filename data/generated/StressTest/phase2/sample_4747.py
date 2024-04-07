# Premise: If Glen is less than 430 km away from Hannah at 6 am, and also 130 km away from Hannah at 11 am, then how fast is Hannah driving (in kilometers per hour)?
# Hypothesis: If Glen is 130 km away from Hannah at 6 am, and also 130 km away from Hannah at 11 am, then how fast is Hannah driving (in kilometers per hour)?
# Golden Label: neutral

glen_distance_premise = 430
glen_distance_hypothesis = 130
glen_same_distance_premise = 130
glen_same_distance_hypothesis = 130

# the hypothesis refers to the distance between Glen and Hannah mentioned in the premise
if glen_distance_premise != glen_distance_hypothesis:
    # check if the distance between Glen and Hannah at 6 am in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
elif glen_same_distance_premise != glen_same_distance_hypothesis:
    # check if the distance between Glen and Hannah at 11 am in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

