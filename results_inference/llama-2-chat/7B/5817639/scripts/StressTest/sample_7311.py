miles_per_hour_premise = 6
miles_per_hour_hypothesis = 2

# the hypothesis talks about the speed of two people, referenced also in the premise
if miles_per_hour_hypothesis <= miles_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of'miles_per_hour_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of one person
    # any speed greater than'miles_per_hour_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
