distance_sisters_premise = 2
distance_sisters_hypothesis = 3

# the hypothesis refers to the distance the sisters ran, which is also mentioned in the premise
if distance_sisters_hypothesis <= distance_sisters_premise:
    # check if the hypothesis value contradicts the premise distance
    label = "contradiction"
else:
    # the premise gives an exact distance for the sisters' run
    # any distance greater than 'distance_sisters_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
