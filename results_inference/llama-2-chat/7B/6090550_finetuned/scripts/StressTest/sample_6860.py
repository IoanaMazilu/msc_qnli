distance_premise = 4
distance_hypothesis = 4
time_premise = 1.25
time_hypothesis = 1.25

# the hypothesis talks about the distance and time Jack walked, which are also mentioned in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif time_hypothesis!= time_premise:
    # check if the time in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
