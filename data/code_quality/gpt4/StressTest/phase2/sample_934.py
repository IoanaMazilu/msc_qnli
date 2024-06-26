distance_premise = 70
distance_hypothesis = 60
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the same speeds and distances as the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the premise's estimate of less than 'distance_premise'
    label = "contradiction"
elif maxwell_speed_hypothesis != maxwell_speed_premise or brad_speed_hypothesis != brad_speed_premise:
    # check if the speeds in the hypothesis contradict the speeds mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
