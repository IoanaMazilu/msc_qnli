distance_premise = 505
distance_hypothesis = 505

# the hypothesis talks about the distance of Scott Island from Victoria, which is also mentioned in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance in the premise, we can infer entailment
    label = "entailment"

print(label)
