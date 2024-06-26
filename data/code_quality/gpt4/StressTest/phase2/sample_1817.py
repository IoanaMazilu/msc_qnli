distance_premise = 80
distance_hypothesis = 10
maxwell_speed_premise = maxwell_speed_hypothesis = 4
brad_speed_premise = brad_speed_hypothesis = 6

# the hypothesis talks about the distance between the homes and the walking/running speeds of Maxwell and Brad, same as in the premise
if distance_hypothesis != distance_premise or maxwell_speed_hypothesis != maxwell_speed_premise or brad_speed_hypothesis != brad_speed_premise:
    # check if any of the values in the hypothesis contradict the corresponding values in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
