distance_premise = 42
distance_hypothesis = 52
ella_speed_premise = 5
ella_speed_hypothesis = 5
ed_speed_premise = 3
ed_speed_hypothesis = 3

# the hypothesis refers to the same distance and walking speeds mentioned in the premise
if distance_premise != distance_hypothesis:
    # check if the hypothesized distance contradicts the distance mentioned in the premise
    label = "contradiction"
elif ella_speed_premise != ella_speed_hypothesis:
    # check if the hypothesized speed for Ella contradicts the speed mentioned in the premise
    label = "contradiction"
elif ed_speed_premise != ed_speed_hypothesis:
    # check if the hypothesized speed for Ed contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
