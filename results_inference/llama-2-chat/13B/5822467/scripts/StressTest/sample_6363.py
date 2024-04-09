watermelons_premise = 136
watermelons_hypothesis = 536

# the hypothesis refers to the number of watermelons after Sally left
if watermelons_hypothesis <= watermelons_premise:
    # check if the hypothesis value contradicts the estimate of 'watermelons_premise'
    label = "contradiction"
elif watermelons_hypothesis > watermelons_premise:
    # the hypothesis value is greater than the premise estimate, so we can infer entailment
    label = "entailment"
else:
    # the premise only gives an estimate for the number of watermelons
    # any number of watermelons less than 536 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
