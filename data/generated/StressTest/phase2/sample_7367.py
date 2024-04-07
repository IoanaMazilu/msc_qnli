# Premise: If Jack walked 7 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Hypothesis: If Jack walked 3 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Golden Label: contradiction

walk_distance_premise = 7
walk_distance_hypothesis = 3

# the hypothesis refers to the distance walked by Jack mentioned in the premise
if walk_distance_premise != walk_distance_hypothesis:
    # if the distance walked in the premise contradicts the distance walked hypothesized
    label = "contradiction"
else:
    # if the distances walked are equal, then the hypothesis is entailed by the premise
    label = "entailment"

print(label)

