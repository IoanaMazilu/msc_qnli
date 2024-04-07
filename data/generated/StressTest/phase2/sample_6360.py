# Premise: Mike had 200 watermelons.
# Hypothesis: Mike had less than 700 watermelons.
# Golden Label: entailment

watermelons_premise = 200
watermelons_hypothesis = 700

# the hypothesis refers to the number of watermelons Mike had, mentioned in the premise
if watermelons_premise >= watermelons_hypothesis:
    # check if the number of watermelons in the premise contradicts the estimate of less than 'watermelons_hypothesis'
    label = "contradiction"
else:
    # the number of watermelons in the premise is less than 'watermelons_hypothesis', hence consistent with the hypothesis
    # but it is not explicitly entailed from the premise
    label = "neutral"

print(label)

