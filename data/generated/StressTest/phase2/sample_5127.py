# Premise: If Jack walked 9 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Hypothesis: If Jack walked more than 8 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Golden Label: entailment

distance_walked_premise = 9
distance_walked_hypothesis = 8

# the hypothesis refers to the distance walked by Jack mentioned in the premise
if distance_walked_premise <= distance_walked_hypothesis:
    # check if the estimate of 'distance_walked_hypothesis' contradicts the distance walked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

