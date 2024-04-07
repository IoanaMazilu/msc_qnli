# Premise: During the first two weeks of May, the total rainfall in Springdale was less than 55 inches.
# Hypothesis: During the first two weeks of May, the total rainfall in Springdale was 35 inches.
# Golden Label: neutral

rainfall_premise = 55
rainfall_hypothesis = 35

# the hypothesis provides a value for the total rainfall in Springdale, which is also referenced in the premise
if rainfall_hypothesis >= rainfall_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rainfall_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total rainfall
    # any amount of rainfall less than 'rainfall_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

