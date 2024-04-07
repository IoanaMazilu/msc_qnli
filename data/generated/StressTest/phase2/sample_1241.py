# Premise: If Jack walked 6 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Hypothesis: If Jack walked 5 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Golden Label: contradiction

distance_walked_premise = 6
distance_walked_hypothesis = 5

# the hypothesis talks about the distance Jack walked, referenced also in the premise
if distance_walked_hypothesis != distance_walked_premise:
    # check if the distance walked in the hypothesis contradicts the distance walked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

