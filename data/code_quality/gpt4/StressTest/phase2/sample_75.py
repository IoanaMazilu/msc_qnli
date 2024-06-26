distance_apart_premise = 12
distance_apart_hypothesis = 62

# the hypothesis talks about the distance between Efrida and Frazer which is referenced in the premise
if distance_apart_hypothesis < distance_apart_premise:
    # check if the hypothesis value contradicts the estimate of 'distance_apart_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
