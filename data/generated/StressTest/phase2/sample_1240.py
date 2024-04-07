# Premise: If Jack walked more than 4 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Hypothesis: If Jack walked 6 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Golden Label: neutral

distance_walked_premise = 4
distance_walked_hypothesis = 6

# the hypothesis replaces the distance walked by Jack which was mentioned in the premise
if distance_walked_hypothesis <= distance_walked_premise:
    # check if the distance walked in the hypothesis contradicts the estimate of more than 'distance_walked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance walked
    # any distance greater than 'distance_walked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

