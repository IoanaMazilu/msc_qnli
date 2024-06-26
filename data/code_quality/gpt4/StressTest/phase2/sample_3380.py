distance_walked_premise = 10
distance_walked_hypothesis = 10

# the hypothesis talks about the distance walked, which is also mentioned in the premise
if distance_walked_hypothesis > distance_walked_premise:
    # check if the hypothesis value contradicts the exact distance mentioned in the premise
    label = "contradiction"
elif distance_walked_hypothesis < distance_walked_premise:
    # check if the hypothesis value contradicts the exact distance mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
