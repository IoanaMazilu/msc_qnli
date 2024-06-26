distance_walked_premise = 81
distance_walked_hypothesis = 31

# the hypothesis talks about the distance walked by Yolanda and Bob, which is also mentioned in the premise
if distance_walked_hypothesis >= distance_walked_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
