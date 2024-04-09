watermelons_premise = 136
watermelons_hypothesis = 536

# the hypothesis talks about the number of watermelons left with mike after sally left
if watermelons_hypothesis <= watermelons_premise:
    # check if the hypothesis value contradicts the estimate of 'watermelons_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of watermelons
    # any number of watermelons greater than 'watermelons_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
