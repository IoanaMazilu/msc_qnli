distance_premise = 100
distance_hypothesis = 100

# the premise and hypothesis refer to the same distance
if distance_premise!= distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same distance
    label = "entailment"

print(label)
