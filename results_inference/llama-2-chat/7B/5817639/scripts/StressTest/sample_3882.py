miles_premise = 0
miles_hypothesis = 0

# the premise gives a range of total hours spent jogging and walking
if miles_hypothesis <= miles_premise:
    # check if the hypothesis value contradicts the estimate of total hours in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total hours,
    # any number of hours less than'miles_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
