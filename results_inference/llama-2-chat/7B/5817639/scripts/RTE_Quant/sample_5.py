premise_distance = 505
hypothesis_distance = 505

# the hypothesis talks about the distance from a specific location (Cape Adare) to the island, which is also mentioned in the premise
if hypothesis_distance == premise_distance:
    # if the distance in the hypothesis matches the distance in the premise, we can infer entailment
    label = "entailment"
elif hypothesis_distance > premise_distance:
    # if the distance in the hypothesis is greater than the distance in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, but the comparison is neutral, we can infer neutrality
    label = "neutral"

print(label)
