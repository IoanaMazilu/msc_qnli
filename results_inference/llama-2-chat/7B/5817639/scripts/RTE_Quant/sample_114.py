people_premise = 52
bombers_premise = 4
bombers_hypothesis = 4

# the hypothesis talks about the number of people and bombers killed on a specific date, which is also mentioned in the premise
if bombers_hypothesis == bombers_premise:
    # if the number of bombers in the hypothesis matches the number of bombers in the premise, we can infer entailment
    label = "entailment"
elif bombers_hypothesis!= bombers_premise:
    # if the number of bombers in the hypothesis contradicts the number of bombers in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if neither the number of bombers nor the number of people in the hypothesis contradicts the premise, we can infer neutrality
    label = "neutral"

print(label)
