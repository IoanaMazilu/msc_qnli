# Premise: Rosy also matched the London Eye which stands at more than 343 ft and Las Vegas’High Roller standing at 550 ft.
# Hypothesis: Rosy also matched the London Eye which stands at 443 ft and Las Vegas’High Roller standing at 550 ft.
# Golden Label: neutral

london_eye_premise = 343
london_eye_hypothesis = 443
high_roller_premise = 550
high_roller_hypothesis = 550

# the hypothesis talks about the height of the London Eye and the High Roller, referenced also in the premise
if london_eye_hypothesis <= london_eye_premise:
    # check if the hypothesis value contradicts the estimate of more than 'london_eye_premise'
    label = "contradiction"
elif high_roller_hypothesis != high_roller_premise:
    # check if the height of the High Roller in the hypothesis contradicts the height reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the height of the London Eye
    # any height greater than 'london_eye_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

