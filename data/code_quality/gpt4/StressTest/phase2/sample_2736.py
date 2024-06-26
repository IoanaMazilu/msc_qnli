distance_premise = 104
distance_hypothesis = 504

# the hypothesis refers to the distance that Mohan beats Rohan, also mentioned in the premise
if distance_premise >= distance_hypothesis:
    # check if the distance in the premise contradicts the estimate of less than 'distance_hypothesis'
    label = "contradiction"
else:
    # the premise directly states the distance by which Mohan beats Rohan
    # so any estimate of less than 'distance_hypothesis' greater than 'distance_premise' does not contradict the premise, but also cannot be directly entailed from it
    label = "neutral"

print(label)
