distance_premise = 35
distance_hypothesis = 15

# the hypothesis refers to the distance between Efrida and Frazer's homes, which is also mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise' miles
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
