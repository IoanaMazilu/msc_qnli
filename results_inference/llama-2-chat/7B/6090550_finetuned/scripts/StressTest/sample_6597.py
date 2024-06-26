distance_premise = 15
distance_hypothesis = 35

# the hypothesis refers to the distance between Efrida and Frazer's homes mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the distance in the premise contradicts the estimate of less than 'distance_hypothesis' miles
    label = "contradiction"
elif distance_premise < distance_hypothesis:
    # if the distance in the premise is less than 'distance_hypothesis' miles, we can infer entailment
    label = "entailment"
else:
    # if the distance in the premise is equal to 'distance_hypothesis' miles, we can infer neutrality
    label = "neutral"

print(label)
