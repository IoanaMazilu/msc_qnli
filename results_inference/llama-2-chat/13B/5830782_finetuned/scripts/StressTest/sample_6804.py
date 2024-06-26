distance_premise = 31
distance_hypothesis = 81

# the hypothesis refers to the distance between X and Y mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif distance_premise < distance_hypothesis:
    # check if the distance in the hypothesis is less than the distance reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
