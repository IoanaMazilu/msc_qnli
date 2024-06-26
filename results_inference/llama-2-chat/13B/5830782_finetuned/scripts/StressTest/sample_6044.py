distance_premise = 40
distance_hypothesis = 80
maxwell_speed_premise = maxwell_speed_hypothesis = 4
brad_speed_premise = brad_speed_hypothesis = 6

# the hypothesis refers to the same scenario as the premise, but with a different distance between the homes
if distance_premise!= distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif maxwell_speed_premise!= maxwell_speed_hypothesis or brad_speed_premise!= brad_speed_hypothesis:
    # check if the speeds in the hypothesis contradict the speeds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
