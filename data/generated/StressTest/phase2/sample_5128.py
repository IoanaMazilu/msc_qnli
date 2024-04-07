# Premise: If Jack walked more than 8 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Hypothesis: If Jack walked 9 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Golden Label: neutral

walked_distance_premise = 8
walked_distance_hypothesis = 9

# the hypothesis talks about the distance that Jack walked, which is also referenced in the premise
if walked_distance_hypothesis <= walked_distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of more than 'walked_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the walked distance
    # any distance greater than 'walked_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

