sita_geeta_premise = 2
sita_geeta_hypothesis = 3

# the hypothesis refers to the distance run by the twin sisters
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
