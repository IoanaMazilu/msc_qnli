# Premise: After Sally left mike had 136 watermelons.
# Hypothesis: After Sally left mike had less than 536 watermelons.
# Golden Label: entailment

watermelons_premise = 136
watermelons_hypothesis = 536

# the hypothesis talks about the number of watermelons Mike had, referenced also in the premise
if watermelons_premise >= watermelons_hypothesis:
    # check if the number of watermelons in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # the hypothesis value of less than 'watermelons_hypothesis' includes the premise value
    # so it can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)

