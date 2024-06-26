distance_premise = 800
distance_hypothesis = 100

# the hypothesis refers to the distance between Fred and Sam mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
