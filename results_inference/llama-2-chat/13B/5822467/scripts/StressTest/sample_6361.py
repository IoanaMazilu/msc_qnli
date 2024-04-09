watermelons_premise = 700
watermelons_hypothesis = 200

# the hypothesis refers to the number of watermelons Mike had
if watermelons_hypothesis <= watermelons_premise:
    # check if the hypothesis value contradicts the estimate of 'watermelons_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of watermelons
    # any number of watermelons less than 'watermelons_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
