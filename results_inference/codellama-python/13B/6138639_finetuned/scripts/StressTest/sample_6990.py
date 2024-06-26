distance_sita_geeta_premise = 12
distance_sita_geeta_hypothesis = 52

# the hypothesis refers to the distance run by Sita and Geeta, mentioned in the premise
if distance_sita_geeta_hypothesis <= distance_sita_geeta_premise:
    # check if the estimate of 'distance_sita_geeta_hypothesis' contradicts the distance run in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
