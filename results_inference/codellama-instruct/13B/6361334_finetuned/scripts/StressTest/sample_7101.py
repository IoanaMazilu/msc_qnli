miles_driven_premise = 240 + 120
miles_driven_hypothesis = 340

# the hypothesis refers to the total miles driven and the speed at which the last 120 miles were driven
if miles_driven_hypothesis >= miles_driven_premise:
    # check if the hypothesis value contradicts the total miles driven in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the total miles driven and the speed at which the last 120 miles were driven
    # any value of miles driven less than'miles_driven_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
