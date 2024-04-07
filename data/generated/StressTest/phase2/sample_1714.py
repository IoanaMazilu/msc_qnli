# Premise: In a covering a distance of more than 10 km, Abhay takes 2 hours more than Sameer.
# Hypothesis: In a covering a distance of 30 km, Abhay takes 2 hours more than Sameer.
# Golden Label: neutral

distance_premise = 10
distance_hypothesis = 30
time_difference = 2

# the premise and the hypothesis both refer to the distance covered and the relative time taken by Abhay and Sameer
if distance_hypothesis <= distance_premise:
    # check if the distance given in the hypothesis contradicts the estimate of more than 'distance_premise' kms
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

