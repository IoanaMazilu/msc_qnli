# Premise: If Jack walked 4 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Hypothesis: If Jack walked more than 4 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Golden Label: contradiction

distance_premise = 4
distance_hypothesis = 4

# the hypothesis refers to the distance walked by Jack, also mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the hypothesis value contradicts the exact distance walked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

