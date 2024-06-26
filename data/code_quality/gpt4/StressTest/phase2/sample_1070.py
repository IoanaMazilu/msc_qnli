ride_duration_premise = 3
ride_duration_hypothesis = 1

# the hypothesis refers to the duration of James' bike ride mentioned in the premise
if ride_duration_premise != ride_duration_hypothesis:
    # check if the duration in the hypothesis contradicts the duration reported in the premise
    label = "contradiction"
else:
    # the ride duration in the hypothesis matches the one in the premise
    label = "entailment"

print(label)
