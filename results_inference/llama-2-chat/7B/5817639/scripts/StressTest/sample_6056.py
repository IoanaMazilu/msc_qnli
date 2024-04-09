miles_premise = 0
miles_hypothesis = 4

# the hypothesis talks about the total time spent jogging and walking, which is also referenced in the premise
if miles_hypothesis <= miles_premise:
    # check if the hypothesis value contradicts the estimate of total miles in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total miles,
    # any number of miles greater than'miles_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
