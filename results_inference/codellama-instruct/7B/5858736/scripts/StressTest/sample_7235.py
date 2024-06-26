sita_geeta_premise = 2
sita_geeta_hypothesis = 3

# the hypothesis refers to the distance each twin sister ran
if sita_geeta_hypothesis <= sita_geeta_premise:
    # check if the estimate of'sita_geeta_hypothesis' contradicts the distance each twin sister ran in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
