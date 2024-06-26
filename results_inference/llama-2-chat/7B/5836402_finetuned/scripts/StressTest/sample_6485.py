distance_premise = 20
distance_hypothesis = 20

# the hypothesis refers to the distance between their homes mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif maxwell_speed_hypothesis!= maxwell_speed_premise or brad_speed_hypothesis!= brad_speed_premise:
    # check if the values of Maxwell's and Brad's speeds in the hypothesis contradict the values reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
