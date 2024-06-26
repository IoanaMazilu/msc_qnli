miles_premise = 4
miles_hypothesis = 3

# the hypothesis refers to the total time spent jogging and walking, which is also mentioned in the premise
if miles_hypothesis >= miles_premise:
    # check if the hypothesis value contradicts the estimate of less than'miles_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total time spent jogging and walking
    # any number of miles less than'miles_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
