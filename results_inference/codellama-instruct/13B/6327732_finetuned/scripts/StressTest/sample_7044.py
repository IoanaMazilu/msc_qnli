raman_travel_premise = 10
raman_travel_hypothesis = 20

# the hypothesis refers to the number of hours travelled by Raman
if raman_travel_hypothesis >= raman_travel_premise:
    # check if the estimate of 'raman_travel_hypothesis' contradicts the number of hours travelled in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of hours travelled by Raman
    # any number of hours less than 'raman_travel_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
