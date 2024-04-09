sita_geeta_premise = 12
sita_geeta_hypothesis = 52

# the hypothesis refers to the distance each twin ran
if sita_geeta_hypothesis <= sita_geeta_premise:
    # check if the hypothesis value contradicts the estimate of'sita_geeta_premise'
    label = "contradiction"
elif sita_geeta_premise!= sita_geeta_hypothesis:
    # check if the estimate of'sita_geeta_hypothesis' contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
