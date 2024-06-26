raman_travel_premise = 10
raman_travel_hypothesis = 20

# the hypothesis refers to the duration of Raman's travel, mentioned in the premise
if raman_travel_hypothesis >= raman_travel_premise:
    # check if the estimate of 'raman_travel_hypothesis' contradicts the duration of travel in the premise
    label = "contradiction"
else:
    # the premise gives an exact duration of travel
    # any duration less than 'raman_travel_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
