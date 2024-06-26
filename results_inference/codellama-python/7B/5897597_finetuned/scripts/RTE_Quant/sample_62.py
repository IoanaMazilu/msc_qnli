distance_premise = 50 # km
distance_hypothesis = 50 # km

# the hypothesis talks about the distance of the reflection of the lighthouse which is also mentioned in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
