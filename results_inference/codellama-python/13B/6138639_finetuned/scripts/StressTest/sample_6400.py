miami_passengers_premise = 8
miami_passengers_hypothesis = 1

# the hypothesis talks about the number of passengers using Miami Airport, referenced also in the premise
if miami_passengers_hypothesis >= miami_passengers_premise:
    # check if the hypothesis value contradicts the estimate of less than'miami_passengers_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers using Miami Airport
    # any number of passengers less than'miami_passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
