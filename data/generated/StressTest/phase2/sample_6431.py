# Premise: Rosy also matched the London Eye which stands at 443 ft and Las Vegas’High Roller standing at 550 ft.
# Hypothesis: Rosy also matched the London Eye which stands at less than 443 ft and Las Vegas’High Roller standing at 550 ft.
# Golden Label: contradiction

london_eye_premise = 443
london_eye_hypothesis = 443
las_vegas_high_roller_premise = 550
las_vegas_high_roller_hypothesis = 550

# the hypothesis refers to the height of the London Eye and the Las Vegas High Roller mentioned in the premise
if london_eye_hypothesis >= london_eye_premise:
    # check if the estimate of 'london_eye_hypothesis' contradicts the height of the London Eye in the premise
    label = "contradiction"
elif las_vegas_high_roller_hypothesis != las_vegas_high_roller_premise:
    # check if the height of the Las Vegas High Roller in the hypothesis contradicts the height reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
