# Premise: After Sally left mike had 136 watermelons.
# Hypothesis: After Sally left mike had less than 136 watermelons.
# Golden Label: contradiction

watermelons_premise = 136
watermelons_hypothesis = 136

# the hypothesis talks about the number of watermelons Mike has after Sally left, also referenced in the premise
if watermelons_hypothesis >= watermelons_premise:
    # check if the hypothesis value contradicts the estimate of less than 'watermelons_hypothesis'
    label = "contradiction"
else:
    # the premise gives only an exact number for the watermelons
    # any number of watermelons less than 'watermelons_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

