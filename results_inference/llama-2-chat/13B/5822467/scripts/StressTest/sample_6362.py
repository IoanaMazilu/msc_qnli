watermelons_premise = 200
watermelons_hypothesis = 100

# the hypothesis refers to the number of watermelons owned by Mike
if watermelons_premise <= watermelons_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'watermelons_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of watermelons
    # any number of watermelons less than 'watermelons_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
